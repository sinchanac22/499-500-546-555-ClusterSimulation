from fastapi import FastAPI
from api_server.node_manager import NodeManager

app = FastAPI()
node_manager = NodeManager()

@app.get("/nodes/")
def get_nodes():
    return node_manager.get_all_nodes()

@app.post("/add_node/")
def add_node(cpu_cores: int):
    node_id = node_manager.register_node(cpu_cores)
    return {"node_id": node_id, "message": "Node successfully added."}
