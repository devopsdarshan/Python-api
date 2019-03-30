from flask_restplus import Namespace, Resource, fields
from flask import Flask, request
api = Namespace('EC2', description='Api\'s to interact with AWS EC2')

import boto3
import json
import logging
ec2 = boto3.client('ec2')

docker_script ="""#!/bin/bash
sudo apt update
sudo apt install -y docker.io
sudo apt install -y docker-compose
"""
nginx_script ="""#!/bin/bash
sudo apt update
sudo apt install -y docker.io
sudo apt install -y docker-compose
sudo docker run -d -p 80:80 nginx
"""
jenkins_script ="""#!/bin/bash
sudo apt update
sudo apt install -y docker.io
sudo apt install -y docker-compose
sudo docker run -d -p 8080:8080 jenkinsci/blueocean
"""
elk_script ="""#!/bin/bash
sudo apt update
sudo apt install -y docker.io
sudo apt install -y docker-compose
cd ~
git clone https://github.com/deviantony/docker-elk.git
cd docker-elk
sudo docker-compose up -d
"""

mean_script ="""#!/bin/bash
sudo apt update
sudo apt install -y docker.io
sudo apt install -y docker-compose
docker run -i -t -d -p 80:3000 maccam912/meanjs 
"""

osdict={"Amazon_Linux":"ami-0937dcc711d38ef3f","Ubuntu":"ami-0d773a3b7bb2bb1c1","Red Hat Enterprise Linux 7.5":"ami-5b673c34"}
userdatadict={"Docker":docker_script,"Nginx":nginx_script,"Jenkins":jenkins_script,"Elk":elk_script,"Mean":mean_script}

@api.route('/instances')    
class Instances(Resource):
    def get(self):
        """
        Get all the instances
        """
        serverdict={}
        serverlist=[]
        count=0
        servers=ec2.describe_instances()
        for reservation in servers['Reservations']:
            for inst in reservation['Instances']:
                count+=1
                name=inst['InstanceId']
                state=inst['State']['Name']
                print(name)
                print(state)
                serverid="server"+str(count)
                serverlist.append({ "instance id":name,"state":state})
         
            
        return {"servers":serverlist}

    @api.doc(params={'os': 'Operating System','instance_type': 'Instance Type','count': 'No of Instances','keyname': 'Keypair Name','app': 'Application name'})
    def post(self):
        """
        Create instance
        """
        os = request.args.get("os")
        instance_type = request.args.get("instance_type")
        count = request.args.get("count")
        keyname = request.args.get("keyname")
        app = request.args.get("app")
        response=ec2.run_instances( ImageId=str(osdict[str(os)]),
        InstanceType=str(instance_type),MaxCount=int(count),
        MinCount=int(count),KeyName=str(keyname),UserData=userdatadict[app])
        return "instance ran successfully"+os 
            
        
@api.route('/instances/<string:instance_id>')

class InstanceOps(Resource):
    def delete(self,instance_id):
        """
        Terminate the instances
        """
        ec2.terminate_instances(InstanceIds=[str(instance_id)])
        return "Server terminated"

@api.route('/instances/<string:instance_id>/<string:running_state>')  
class InstanceStartStop(Resource):     
    def post(self,instance_id,running_state):
        """
        Start or Stop a server 
        """
        if(str(running_state)=="running"):
            ec2.start_instances(InstanceIds=[
            str(instance_id)
            ])
            return "Server Started"
        elif(str(running_state)=="stopped"):
            ec2.stop_instances(InstanceIds=[
            str(instance_id)
            ])
            return "Server Stopped"

        return "Invalid running state"

@api.route('/keypairs')
class Keypair(Resource):
    def get(self):
        """
        Get all the keypairs in this region
        """    
        keypairdict={}
        keypairlist=[]
        keypairs=ec2.describe_key_pairs()
        for keypair in keypairs['KeyPairs']:
            keypairlist.append(keypair['KeyName'])
        
        return {"keypairs":keypairlist}
        