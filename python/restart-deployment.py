from kubernetes import client, config

def restart_deployment(deployment_name, namespace='default'):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    deployment = apps_v1.read_namespaced_deployment(name=deployment_name, namespace=namespace)
    deployment.spec.template.metadata.annotations = {
        "kubectl.kubernetes.io/restartedAt": datetime.datetime.now().isoformat()
    }
    apps_v1.patch_namespaced_deployment(name=deployment_name, namespace=namespace, body=deployment)
    print(f"Deployment '{deployment_name}' restarted.")

restart_deployment('my-deployment', 'default')
