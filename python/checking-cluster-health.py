from kubernetes import client, config

def check_cluster_health():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    nodes = v1.list_node()
    for node in nodes.items:
        conditions = node.status.conditions
        for condition in conditions:
            if condition.type == "Ready":
                print(f"Node: {node.metadata.name}, Status: {condition.status}")

check_cluster_health()
