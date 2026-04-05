import pytest
from helper import send_request, wait_until
from verifier import CCMVerifier

verifier = CCMVerifier()


# =========================
# 1. Process check
# =========================
def test_ccm_process_alive():
    output = verifier.get_process()
    assert "ccm" in output


# =========================
# 2. Service status
# =========================
def test_ccm_service_status():
    status = verifier.get_service_status()
    assert status == "active"


# =========================
# 3. Wake up state (shell verify)
# =========================
def test_wakeup_state_shell(ccm):
    send_request(ccm, "wake_up")

    assert wait_until(
        lambda: verifier.get_device_state() == "ACTIVE"
    )


# =========================
# 4. HW info consistency
# =========================
def test_hw_info_consistency(ccm):
    resp = send_request(ccm, "get_hw_info")
    hw_shell = verifier.get_hw_info()

    assert resp["data"] == hw_shell


# =========================
# 5. Ping + log verification
# =========================
def test_no_error_after_ping(ccm):
    send_request(ccm, "ping")

    logs = verifier.get_logs("10 sec ago")
    assert "error" not in logs.lower()


# =========================
# 6. Stress test
# =========================
def test_stress_ping_with_log_check(ccm):
    for _ in range(50):
        send_request(ccm, "ping")

    logs = verifier.get_logs("30 sec ago")
    assert "segmentation fault" not in logs.lower()


# =========================
# 7. Service restart recovery
# =========================
def test_service_restart_recovery():
    from helper_shell import run_cmd_ssh

    run_cmd_ssh("systemctl restart ccm_service")

    status = verifier.get_service_status()
    assert status == "active"


# =========================
# 8. File update after ping
# =========================
def test_file_updated_after_request(ccm):
    send_request(ccm, "ping")

    assert wait_until(
        lambda: verifier.get_last_ping() != ""
    )