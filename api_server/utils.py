# api_server/utils.py
import subprocess

def launch_node_container(cpu_cores, node_id):
    container_name = f"node_{node_id}"
    subprocess.run([
        "docker", "run", "-d", "--name", container_name,
        "-e", f"CPU_CORES={cpu_cores}", 
        "your-node-image-name"
    ])

