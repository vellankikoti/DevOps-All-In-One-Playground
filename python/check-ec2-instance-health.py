import boto3

def check_instance_health(instance_id, region='us-west-2'):
    ec2 = boto3.client('ec2', region_name=region)
    statuses = ec2.describe_instance_status(InstanceIds=[instance_id])
    for status in statuses['InstanceStatuses']:
        print(f"Instance {instance_id} is {status['InstanceState']['Name']}, Health: {status['InstanceStatus']['Status']}")

check_instance_health('your_instance_id')
