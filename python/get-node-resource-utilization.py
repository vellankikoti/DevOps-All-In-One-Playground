from kubernetes import client, config

def get_node_utilization():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    nodes = v1.list_node()
    for node in nodes.items:
        print(f"Node: {node.metadata.name}")
        for usage in node.status.capacity:
            print(f"  {usage}: {node.status.capacity[usage]}")

get_node_utilization()
