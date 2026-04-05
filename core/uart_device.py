import time

try:
    import serial
except ImportError:
    serial = None


class UARTDevice:
    def __init__(self, port=None, baud=115200, mock=False):
        self.mock = mock

        if mock:
            from core.mock_device import MockZephyrBoard
            self.dev = MockZephyrBoard()
        else:
            if serial is None:
                raise Exception("pyserial not installed")

            self.ser = serial.Serial(port, baud, timeout=1)

    def send(self, cmd: str):
        if self.mock:
            self.last_cmd = cmd
        else:
            self.ser.write((cmd + "\n").encode())

    def read(self):
        if self.mock:
            return self.dev.handle_command(self.last_cmd)
        else:
            time.sleep(0.3)
            return self.ser.read_all().decode(errors="ignore")

    def get_response(self, cmd: str):
        self.send(cmd)
        return self.read()