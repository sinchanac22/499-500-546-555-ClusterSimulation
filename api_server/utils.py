import sys
import time

if __name__ == "__main__":
    node_id = sys.argv[1]
    print(f"Simulated Node {node_id} is running...")
    while True:
        time.sleep(5)
        print(f"[{node_id}] Sending heartbeat...")
