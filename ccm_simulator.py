import time

class CCMSimulator:
    def __init__(self):
        self.state = {
            "awake": False,
            "mode": "IDLE",
            "hw_info": "CCM_V1.0",
            "last_ping": None
        }

    def handle_request(self, req):
        cmd = req.get("cmd")

        if cmd == "wake_up":
            self.state["awake"] = True
            self.state["mode"] = "ACTIVE"
            return {"status": "OK"}

        elif cmd == "get_status":
            return {"status": "OK", "data": self.state["mode"]}

        elif cmd == "ping":
            self.state["last_ping"] = time.time()
            return {"status": "OK", "data": "pong"}

        elif cmd == "get_hw_info":
            return {"status": "OK", "data": self.state["hw_info"]}

        return {"status": "ERROR"}
