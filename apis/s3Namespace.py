from flask_restplus import Namespace, Resource, fields

api = Namespace('S3', description='Api\'s to interact with AWS S3')

import boto3
import json
import logging
s3=boto3.client('s3')

@api.route('/buckets')  
class Buckets(Resource):
    def get(self):
        """
        Get all the buckets
        """
        buckets=s3.list_buckets()
        bucketlist=[]
        for i in buckets['Buckets']:
            bucket= i['Name']
            bucketlist.append(bucket)
        print(bucketlist)
        return {"buckets":bucketlist}
        
@api.route('/objects')
class Objects(Resource):
    def get(self):
        """
        Get all the objects in all buckets
        """
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
    def post(self,bucket_name):
        """
        Create a bucket
        """
        s3.create_bucket(Bucket=str(bucket_name), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
        return "bucket created successfully"
    def delete(self,bucket_name):
        """
        Delete a bucket
        """
        s3.delete_bucket(Bucket=str(bucket_name))
        return "bucket "+ bucket_name + " deleted successfully"

@api.route('/objects/<string:bucket_name>')
class ObjectsOps(Resource):
    def get(self,bucket_name):
        """
        Get all the objects in given bucket
        """
        objectlist=[]
        objects=s3.list_objects_v2(Bucket=str(bucket_name))
        print(objects)
        if(objects['KeyCount']!=0):
            for object in objects['Contents']:
                objectlist.append(object['Key'])
        
    
        return {bucket_name:objectlist}    
