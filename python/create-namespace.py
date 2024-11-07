from kubernetes import client, config

def create_namespace(name):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=name))
    v1.create_namespace(namespace)
    print(f"Namespace '{name}' created successfully.")

create_namespace('my-new-namespace')
