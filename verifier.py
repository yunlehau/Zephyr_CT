from helper_shell import run_cmd_ssh


class CCMVerifier:

    def get_process(self):
        return run_cmd_ssh("ps aux | grep ccm | grep -v grep")

    def get_service_status(self):
        return run_cmd_ssh("systemctl is-active ccm_service")

    def get_logs(self, since="10 sec ago"):
        return run_cmd_ssh(f"journalctl -u ccm_service --since '{since}'")

    def get_device_state(self):
        return run_cmd_ssh("cat /sys/device/state")

    def get_hw_info(self):
        return run_cmd_ssh("cat /etc/hw_info")

    def get_last_ping(self):
        return run_cmd_ssh("cat /tmp/last_ping")