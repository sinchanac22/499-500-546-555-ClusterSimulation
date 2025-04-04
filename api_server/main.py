from api_server.utils import launch_node_container

@app.post("/add_node/")
def add_node(cpu_cores: int):
    node_id = node_manager.register_node(cpu_cores)
    launch_node_container(cpu_cores, node_id)
    return {"message": "Node added and container launched", "node_id": node_id}
