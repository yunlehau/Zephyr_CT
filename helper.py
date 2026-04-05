import time

def send_request(ccm, cmd, payload=None):
    return ccm.handle_request({"cmd": cmd, "payload": payload or {}})

def run_cmd(ccm, cmd):
    mapping = {
        "get_mode": ccm.state["mode"],
        "is_awake": str(ccm.state["awake"]),
        "last_ping": str(ccm.state["last_ping"]),
        "hw_info": ccm.state["hw_info"],
    }
    return mapping.get(cmd, "UNKNOWN")

def wait_until(func, timeout=3):
    start = time.time()
    while time.time() - start < timeout:
        if func():
            return True
        time.sleep(0.1)
    return False
