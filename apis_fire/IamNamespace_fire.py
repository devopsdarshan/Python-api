from flask_restplus import Namespace, Resource, fields
from flask import Flask, request
api = Namespace('IAM', description='Api\'s to interact with AWS IAM')
import os
import boto3
import json
import logging
from .firestore import db
#iam = boto3.client('iam')


@api.route('/users')    
class Users(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the Users in your account
        """ 
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        userdict={}
        count=0
        users=iam.list_users()
        userlist=[]
        print(users)
        for user in users['Users']:
            count+=1
            name=user['UserName']
            userid="user"+str(count)
            userlist.append({"Username":name})
            
        return {"users":userlist}

@api.route('/users/<string:user_name>')        
class UserOps(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def post(self,user_name):
        """
        Create an User in your account
        """ 
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        iam.create_user(UserName=str(user_name))
        return "User "+user_name+" created"
    @api.doc(params={'profile': 'profile_name'})
    def delete(self,user_name):
        """
        Delete an User in your account
        """
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        iam.delete_user(
        UserName=str(user_name)
        )
        return "User "+user_name+" deleted"

@api.route('/groups')    
class Groups(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the groups in your account
        """ 
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        groups=iam.list_groups()
        grouplist=[]
        
        for group in groups['Groups']:
            
            name=group['GroupName']
            arn=group['Arn']
            grouplist.append({"Name":name,"ARN":arn})
            
        return {"groups":grouplist}

@api.route('/groups/<string:group_name>')        
class GroupOps(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def post(self,group_name):
        """
        Create a Group in your account
        """
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        iam.create_group(GroupName=str(group_name))
        return "Group"+group_name+" created"
    @api.doc(params={'profile': 'profile_name'})
    def get(self,group_name):
        """
        Get the group details
        """
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        group_details=iam.get_group(
         GroupName=str(group_name)
        )
        return {"group details":str(group_details)}
    @api.doc(params={'profile': 'profile_name'})
    def delete(self,group_name):
        """
        Delete an group in your account
        """
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        iam.delete_group(
        GroupName=str(group_name)
        )
        return "Group "+group_name+" deleted"
@api.route('/groups/<string:group_name>/<string:user_name>')        
class GroupsUsers(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def post(self,group_name,user_name):
        """
        Add an user to a Group 
        """
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        iam.add_user_to_group(
        GroupName=str(group_name),
        UserName=str(user_name)
        )
        return "User"+user_name+"added to"+ "Group"+group_name

@api.route('/roles')    
class Roles(Resource):
    @api.doc(params={'profile': 'profile_name'})
    def get(self):
        """
        Get all the roles in your account
        """
        profile = request.args.get("profile")
        iam=boto3.client('iam', region_name=str(db.child('profiles').child(str(profile)).get().val()['region']), aws_access_key_id=str(db.child('profiles').child(str(profile)).get().val()['access_key']), aws_secret_access_key=str(db.child('profiles').child(str(profile)).get().val()['secret_access_key']))
        roles=iam.list_roles()
        roleslist=[]
        
        for role in roles['Roles']:
            
            name=role['RoleName']
            description=role['Description']
            roleslist.append({"Name":name,"Description":description})
            
        return {"roles":roleslist}


##############test feature to later on add new profiles in the aws credentials file
@api.route('/credentials')    
class Credentials(Resource):
    @api.doc(params={'os': 'Operating System'})
    def post(self):
        os = request.args.get("os")
        with open("./hello", "a") as myfile:
            myfile.write("appended text" + str(os))
        return "Successful"
