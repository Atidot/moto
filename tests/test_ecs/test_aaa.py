from __future__ import unicode_literals
from datetime import datetime

from botocore.exceptions import ClientError
import boto3
import sure  # noqa
import json
from moto.ec2 import utils as ec2_utils
from uuid import UUID

from moto import mock_ecs
from moto import mock_ec2
def add_env_vars_in_docker(*args, **kwargs):
    overrides = kwargs.get('overrides', None)
    try:
        print(kwargs)
    except Exception as e:
        print(e)
@mock_ec2()
@mock_ecs(callback=add_env_vars_in_docker)
def aaa():
    client = boto3.client("ecs", region_name="us-east-1")
    ec2 = boto3.resource("ec2", region_name="us-east-1")
    response = client.run_task(
        cluster="test_ecs_cluster",
        overrides={},
        taskDefinition="test_ecs_task",
        count=2,
        startedBy="moto",
   )

if __name__ == '__main__':
    aaa()