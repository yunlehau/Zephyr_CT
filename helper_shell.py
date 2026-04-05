import subprocess


def run_cmd_ssh(cmd, host="root@192.168.1.10"):
    """
    Execute shell command on remote CCM via SSH
    """
    full_cmd = f"ssh {host} '{cmd}'"
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def run_cmd_local(cmd):
    """
    Execute local shell command (for debug / simulation)
    """
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()