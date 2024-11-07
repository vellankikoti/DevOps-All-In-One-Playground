from kubernetes import client, config

def delete_pod(pod_name, namespace='default'):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    v1.delete_namespaced_pod(name=pod_name, namespace=namespace)
    print(f"Pod '{pod_name}' deleted from namespace '{namespace}'.")

delete_pod('my-pod', 'your-namespace')
