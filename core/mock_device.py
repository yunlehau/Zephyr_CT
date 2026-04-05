import time

class MockZephyrBoard:
    def __init__(self):
        self.commands = {
            "get_status": "OK",
            "get_version": "Zephyr 3.5.0",
            "reset": "REBOOTING",
        }

    def handle_command(self, cmd: str) -> str:
        cmd = cmd.strip()

        # simulate processing delay
        time.sleep(0.1)

        if cmd in self.commands:
            return self.commands[cmd]
        else:
            return "ERROR: Unknown command"