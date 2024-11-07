from kubernetes import client, config

def update_deployment_image(deployment_name, container_name, new_image, namespace='default'):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    deployment = apps_v1.read_namespaced_deployment(name=deployment_name, namespace=namespace)
    for container in deployment.spec.template.spec.containers:
        if container.name == container_name:
            container.image = new_image
    apps_v1.patch_namespaced_deployment(name=deployment_name, namespace=namespace, body=deployment)
    print(f"Updated '{container_name}' in '{deployment_name}' to '{new_image}'.")

update_deployment_image('my-deployment', 'my-container', 'nginx:latest')
