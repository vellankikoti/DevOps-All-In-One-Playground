import boto3
import json

def ec2_info_to_json(region='us-west-2'):
    ec2 = boto3.client('ec2', region_name=region)
    instances = ec2.describe_instances()
    data = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            data.append({
                'InstanceId': instance['InstanceId'],
                'State': instance['State']['Name'],
                'Type': instance['InstanceType']
            })
    with open('ec2_report.json', 'w') as file:
        json.dump(data, file)

ec2_info_to_json()
