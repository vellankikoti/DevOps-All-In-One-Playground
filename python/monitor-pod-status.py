from kubernetes import client, config, watch

def monitor_pod_status(pod_name, namespace='default'):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    w = watch.Watch()
    for event in w.stream(v1.list_namespaced_pod, namespace=namespace):
        pod = event['object']
        if pod.metadata.name == pod_name:
            print(f"Event: {event['type']}, Pod Status: {pod.status.phase}")

monitor_pod_status('my-pod', 'your-namespace')
