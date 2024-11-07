from kubernetes import client, config

def list_services(namespace='default'):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    services = v1.list_namespaced_service(namespace=namespace)
    for service in services.items:
        print(f"Service Name: {service.metadata.name}, Cluster IP: {service.spec.cluster_ip}, Ports: {service.spec.ports}")

list_services('your-namespace')
