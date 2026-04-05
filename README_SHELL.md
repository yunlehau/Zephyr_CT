# Zephyr_CT - UART Test Framework for Zephyr RTOS

## Project Overview

This project is a lightweight UART-based test automation framework designed to validate Zephyr RTOS devices.

It supports:
- Real hardware testing via UART
- Mock testing without hardware
- Command-response validation

---

## Architecture

Test PC → UART → Zephyr Board → Response → Test Validation

---

## Key Components

### 1. UARTDevice
Abstraction layer for:
- Sending commands
- Receiving responses
- Supporting both real and mock devices

### 2. MockZephyrBoard
Simulates Zephyr shell behavior:
- Used for local testing
- No hardware required

### 3. Test Cases
Simple API:

get_response("command")


---

## How to Use

### Run with Mock (no hardware)

```python
dev = UARTDevice(mock=True)
resp = dev.get_response("get_status")
Run with Real Device
dev = UARTDevice(port="/dev/ttyUSB0", mock=False)
Example Commands
Command	Response
get_status	OK
get_version	Zephyr 3.5.0
reset	REBOOTING
Testing Strategy
Black-box testing via UART CLI
Command-response validation
Retry + logging supported
AI Context (for automation / agents)

This project simulates a UART-based embedded testing environment.

Key API:

get_response(cmd: str) -> str

Behavior:

Sends command to device
Waits for response
Returns output string

Supports:

mock=True → simulated device
mock=False → real UART device
Future Improvements
pytest integration
CI/CD pipeline
Multi-device support
log parser + report

---

# 🚀 8. Kết quả bạn đạt được

👉 Sau khi thêm code này:

- ✅ Test local không cần board  
- ✅ API cực đơn giản: `get_response()`  
- ✅ Có thể scale thành framework thật  
- ✅ Dễ integrate CI  

---

# 👉 Nếu bạn muốn nâng cấp tiếp

Mình có thể giúp bạn:

- Convert sang **pytest full framework**
- Thêm **timeout + regex parser**
- Tạo **HTML report**
- Mapping luôn vào project GitHub của bạn

Chỉ cần nói:  
👉 *“upgrade lên production-level framework”*