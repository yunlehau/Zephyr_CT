from helper import send_request
from verifier import CCMVerifier
from utils import retry, wait_until

verifier = CCMVerifier()


@retry(times=1, delay=1)
def test_ccm_process_alive():
    output = verifier.get_process()
    assert "ccm" in output


@retry(times=1, delay=1)
def test_ccm_service_status():
    status = verifier.get_service_status()
    assert status == "active"


def test_wakeup_state_shell(ccm):
    send_request(ccm, "wake_up")

    assert wait_until(
        lambda: verifier.get_device_state() == "ACTIVE"
    )


@retry(times=3, delay=1)
def test_no_error_after_ping(ccm):
    send_request(ccm, "ping")

    logs = verifier.get_logs("10 sec ago")
    assert "error" not in logs.lower()


def test_stress_ping_with_log_check(ccm):
    for _ in range(50):
        send_request(ccm, "ping")

    logs = verifier.get_logs("30 sec ago")
    assert "segmentation fault" not in logs.lower()