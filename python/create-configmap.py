from kubernetes import client, config

def create_configmap(name, namespace, data):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    config_map = client.V1ConfigMap(
        metadata=client.V1ObjectMeta(name=name),
        data=data
    )
    v1.create_namespaced_config_map(namespace=namespace, body=config_map)
    print(f"ConfigMap '{name}' created in namespace '{namespace}'.")

create_configmap('my-config', 'default', {'key1': 'value1', 'key2': 'value2'})
