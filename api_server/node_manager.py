import uuid

class NodeManager:
    def __init__(self):
        self.nodes = {}  # Dictionary: node_id → info

    def register_node(self, cpu_cores):
        node_id = str(uuid.uuid4())[:8]
        self.nodes[node_id] = {
            "cpu_cores": cpu_cores,
            "available_cores": cpu_cores,
            "status": "healthy",
            "pods": []
        }
        return node_id

    def get_nodes(self):
        return self.nodes
