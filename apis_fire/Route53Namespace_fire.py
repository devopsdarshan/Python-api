from flask_restplus import Namespace, Resource, fields

from flask import Flask, request
from .firestore import db

api = Namespace('Route53', description='Api\'s to interact with AWS Route53')

import boto3
import json
import logging
#s3=boto3.client('s3')
#users = db.child('profiles').child('madhavi').get()
#route53=boto3.client('route53', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))


@api.route('/healthchecks')  
class HealthChecks(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the healthchecks 
        """
        profile = request.args.get("profile")
        route53=boto3.client('route53', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        
        healthchecks=route53.list_health_checks()
        
        return str(healthchecks)

@api.route('/hostedzones')  
class HostedZones(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the hostedzones
        """
        profile = request.args.get("profile")
        route53=boto3.client('route53', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        
        hostedzones=route53.list_hosted_zones()
        
        return str(hostedzones)

@api.route('/hostedzones/<string:hostedzone_name>')  
class HostedZone(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self,hostedzone_name):
        """
        Get information of specified hostedzone
        """
        profile = request.args.get("profile")
        route53=boto3.client('route53', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        
        hostedzone_info=route53.get_hosted_zone(
            Id=str(hostedzone_name)
        )
        
        return str(hostedzone_info)

@api.route('/trafficpolicies')  
class TrafficPolicies(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the trafficpolicies
        """
        profile = request.args.get("profile")
        route53=boto3.client('route53', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        
        trafficpolicies=route53.list_traffic_policies()
        
        return str(trafficpolicies)
 