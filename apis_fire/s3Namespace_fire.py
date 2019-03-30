from flask_restplus import Namespace, Resource, fields

from flask import Flask, request
from .firestore import db

api = Namespace('S3', description='Api\'s to interact with AWS S3')

import boto3
import json
import logging
#s3=boto3.client('s3')
#users = db.child('profiles').child('madhavi').get()


#s3=boto3.client('s3', region_name='ap-south-1', aws_access_key_id=str(users.val()['access_key']), aws_secret_access_key=str(users.val()['secret_access_key']))

@api.route('/buckets')  
class Buckets(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the buckets
        """
        profile = request.args.get("profile")
        s3=boto3.client('s3', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        buckets=s3.list_buckets()
        bucketlist=[]
        for i in buckets['Buckets']:
            bucket= i['Name']
            bucketlist.append(bucket)
        print(bucketlist)
        return {"buckets":bucketlist}
        
@api.route('/objects')
class Objects(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the objects in all buckets
        """
        profile = request.args.get("profile")
        s3=boto3.client('s3', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        buckets=s3.list_buckets()
        bucketlist=[]
    
        objectdict={}
        for i in buckets['Buckets']:
            bucket= i['Name']
            bucketlist.append(bucket)
            for bucket in bucketlist:
                print(bucket)
                objectlist=[]
                objects=s3.list_objects(Bucket=str(bucket))
                print(objects)

                for object in objects['Contents']:
                    objectlist.append(object['Key'])
                objectdict.update({bucket:objectlist})
        

        return objectdict
    
@api.route('/buckets/<string:bucket_name>')  
class BucketsOps(Resource): 
    @api.doc(params={'profile': 'profile_name'})
    def post(self,bucket_name):
        """
        Create a bucket
        """
        profile = request.args.get("profile")
        s3=boto3.client('s3', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        s3.create_bucket(Bucket=str(bucket_name), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
        return "bucket created successfully"
    @api.doc(params={'profile': 'profile_name'})    
    def delete(self,bucket_name):
        """
        Delete a bucket
        """
        profile = request.args.get("profile")
        s3=boto3.client('s3', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        s3.delete_bucket(Bucket=str(bucket_name))
        return "bucket "+ bucket_name + " deleted successfully"

@api.route('/objects/<string:bucket_name>')
class ObjectsOps(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self,bucket_name):
        """
        Get all the objects in given bucket
        """
        profile = request.args.get("profile")
        s3=boto3.client('s3', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        objectlist=[]
        objects=s3.list_objects_v2(Bucket=str(bucket_name))
        print(objects)
        if(objects['KeyCount']!=0):
            for object in objects['Contents']:
                objectlist.append(object['Key'])
        
    
        return {bucket_name:objectlist}    
