from flask_restplus import Api

from .s3Namespace import api as s3
from .Ec2Namespace import api as ec2

from .IamNamespace import api as iam
api = Api(
    title='AWS API',
    version='1.0',
    description='Use this API to interact with your AWS services',
   
)

api.add_namespace(s3, path='/s3')
api.add_namespace(ec2, path='/ec2')
api.add_namespace(iam, path='/iam')