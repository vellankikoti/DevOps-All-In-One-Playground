import boto3

def list_regions(service='ec2'):
    client = boto3.client(service)
    regions = client.describe_regions()
    for region in regions['Regions']:
        print(region['RegionName'])

list_regions()
