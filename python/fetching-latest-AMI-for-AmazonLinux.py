import boto3

def get_latest_ami(region='us-west-2'):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_images(
        Owners=['amazon'],
        Filters=[{'Name': 'name', 'Values': ['amzn2-ami-hvm-*-x86_64-gp2']}]
    )
    images = sorted(response['Images'], key=lambda x: x['CreationDate'], reverse=True)
    return images[0]['ImageId'] if images else None

print(get_latest_ami())
