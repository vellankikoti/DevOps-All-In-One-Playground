from kubernetes import client, config

def get_pod_logs(pod_name, namespace='default'):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
    print(f"Logs for pod '{pod_name}':\n{logs}")

get_pod_logs('my-pod', 'your-namespace')
