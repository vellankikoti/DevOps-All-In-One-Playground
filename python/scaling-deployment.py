from kubernetes import client, config

def scale_deployment(deployment_name, namespace, replicas):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    body = {"spec": {"replicas": replicas}}
    apps_v1.patch_namespaced_deployment_scale(name=deployment_name, namespace=namespace, body=body)
    print(f"Deployment '{deployment_name}' scaled to {replicas} replicas.")

scale_deployment('my-deployment', 'default', 3)
