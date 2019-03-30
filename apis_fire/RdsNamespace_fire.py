from flask_restplus import Namespace, Resource, fields

from flask import Flask, request
from .firestore import db

api = Namespace('Rds', description='Api\'s to interact with AWS RDS')

import boto3
import json
import logging
#s3=boto3.client('s3')
#users = db.child('profiles').child('madhavi').get()
#rds=boto3.client('rds', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))


@api.route('/healthchecks')  
class HealthChecks(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the healthchecks 
        """
        profile = request.args.get("profile")
        rds=boto3.client('rds', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))        
        healthchecks=rds.list_health_checks()
        
        return str(healthchecks)
