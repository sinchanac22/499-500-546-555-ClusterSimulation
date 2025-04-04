import uuid
import subprocess

class NodeManager:
    def __init__(self):
        self.nodes = {}

    def register_node(self, cpu_cores):
        node_id = str(uuid.uuid4())[:8]
        self.nodes[node_id] = {
            "cpu_cores": cpu_cores,
            "status": "active"
        }
        self._launch_node_container(node_id)
        return node_id

    def get_all_nodes(self):
        return self.nodes

    def _launch_node_container(self, node_id):
        subprocess.Popen([
            "docker", "run", "-d", "--name", f"node_{node_id}",
            "--rm", "node_sim", node_id
        ])
