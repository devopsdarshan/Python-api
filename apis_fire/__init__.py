from flask_restplus import Api

from .s3Namespace_fire import api as s3
from .Ec2Namespace_fire import api as ec2

from .IamNamespace_fire import api as iam
from .Route53Namespace_fire import api as route53


api = Api(
    title='AWS API',
    version='1.0',
    description='Use this API to interact with your AWS services',
   
)

api.add_namespace(s3, path='/s3')
api.add_namespace(ec2, path='/ec2')
api.add_namespace(iam, path='/iam')
api.add_namespace(route53, path='/route53')