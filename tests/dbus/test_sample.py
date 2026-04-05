from core.uart_device import UARTDevice

# dùng mock = True để test local
dev = UARTDevice(mock=True)


def test_get_status():
    resp = dev.get_response("get_status")
    assert "OK" in resp


def test_invalid_command():
    resp = dev.get_response("abc123")
    assert "ERROR" in resp