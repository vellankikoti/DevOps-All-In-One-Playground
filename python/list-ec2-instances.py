import boto3

def list_ec2_instances(region='us-west-2'):
    ec2 = boto3.client('ec2', region_name=region)
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

list_ec2_instances()
