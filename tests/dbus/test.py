from helper import send_request, run_cmd, wait_until
from data_set import INVALID_COMMANDS

def test_wake_up(ccm):
    assert send_request(ccm, "wake_up")["status"] == "OK"
    assert wait_until(lambda: run_cmd(ccm, "is_awake") == "True")

def test_ping(ccm):
    resp = send_request(ccm, "ping")
    assert resp["data"] == "pong"

def test_invalid(ccm):
    for cmd in INVALID_COMMANDS:
        assert send_request(ccm, cmd)["status"] == "ERROR"
