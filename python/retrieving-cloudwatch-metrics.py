import boto3

def get_cloudwatch_metrics(namespace, metric_name, instance_id, region='us-west-2'):
    cloudwatch = boto3.client('cloudwatch', region_name=region)
    metrics = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=60,
        Statistics=['Average']
    )
    print(metrics['Datapoints'])

get_cloudwatch_metrics('AWS/EC2', 'CPUUtilization', 'your_instance_id')
