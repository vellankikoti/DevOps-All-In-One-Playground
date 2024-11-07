from kubernetes import client, config

def list_pods(namespace='default'):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace)
    for pod in pods.items:
        print(f"Pod: {pod.metadata.name}, Status: {pod.status.phase}, IP: {pod.status.pod_ip}")

list_pods('your-namespace')
