# main.py
from fastapi import FastAPI, Request
from api_server.node_manager import NodeManager
from api_server.utils import launch_node_container

app = FastAPI()
node_manager = NodeManager()

@app.get("/")
def root():
    return {"message": "API Server Running"}

@app.post("/add_node/")
def add_node(cpu_cores: int):
    node_id = node_manager.register_node(cpu_cores)
    return {"message": "Node added", "node_id": node_id}

@app.get("/nodes/")
def get_all_nodes():
    return node_manager.get_nodes()

@app.post("/add_node/")
def add_node(cpu_cores: int):
    node_id = node_manager.register_node(cpu_cores)
    launch_node_container(cpu_cores, node_id)
    return {"message": "Node added and container launched", "node_id": node_id}
