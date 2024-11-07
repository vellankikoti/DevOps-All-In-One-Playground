from kubernetes import client, config

def check_pod_health(namespace='default'):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace=namespace)
    for pod in pods.items:
        print(f"Pod {pod.metadata.name} is {pod.status.phase}")

check_pod_health()
