Dưới đây là nội dung bạn có thể **copy trực tiếp vào `README.md`** (đã viết bằng tiếng Anh, rõ ràng, chuẩn cho project):

---

# 🧪 Shell Command Usage in Testing

## 🎯 Purpose

In this project, shell commands are used to **verify the real system state (ground truth)** after sending requests from the test PC to the CCM (Central Computing Module).

Instead of trusting only the response from CCM, we validate the actual system behavior at OS/HW level.

---

## 🧠 Testing Concept

```text
Test PC (pytest) → send request → CCM → response
                                      ↓
                               system state (real)
                                      ↓
                              verified via shell
```

---

## 🔍 What We Verify Using Shell Commands

### 1. System State

Check internal state of the system:

```bash
cat /sys/motor/state
cat /tmp/temperature
```

Mock equivalent:

```python
run_cmd(ccm, "get_mode")
```

---

### 2. Device Status (Awake / Mode)

```bash
cat /sys/device/state
```

Mock:

```python
run_cmd(ccm, "is_awake")
```

---

### 3. Hardware Information

```bash
cat /etc/hw_info
```

Mock:

```python
run_cmd(ccm, "hw_info")
```

---

### 4. Activity / Event Tracking (e.g. Ping)

```bash
cat /tmp/last_ping
```

Mock:

```python
run_cmd(ccm, "last_ping")
```

---

### 5. System Logs (Critical for Debugging)

```bash
journalctl -u ccm_service
```

Used to:

* Detect hidden errors
* Debug failing tests
* Verify system stability

---

## 🧪 Test Pattern

### Standard Pattern

```python
resp = send_request(...)
assert resp["status"] == "OK"

# Verify real state via shell
state = run_cmd(...)
assert state == expected
```

---

### Async Handling (Recommended)

```python
assert wait_until(lambda: run_cmd(...) == expected)
```

---

## ⚠️ Common Issues

### 1. Timing / Async Behavior

System may not update immediately.

❌ Avoid:

```python
assert run_cmd(...) == "ON"
```

✔️ Use:

```python
wait_until(...)
```

---

### 2. Output Formatting

Shell output may contain newline:

```text
"ON\\n"
```

✔️ Always clean:

```python
output.strip()
```

---

### 3. Permission Issues

Some commands require root access:

```bash
sudo cat /sys/...
```

---

### 4. Flaky Tests

Caused by:

* Async processing
* Timing issues
* Race conditions

✔️ Solution:

* Use retry / wait logic
* Avoid fixed sleep

---

## 🚀 Best Practices

### 1. Wrap Shell Commands

```python
def get_motor_state():
    return run_cmd("cat /sys/motor/state")
```

---

### 2. Avoid Hardcoding in Tests

❌

```python
run_cmd("cat /sys/motor/state")
```

✔️

```python
verifier.get_motor_state()
```

---

### 3. Combine Multiple Verifications

```python
assert resp["status"] == "OK"
assert state == "ON"
assert "error" not in logs
```

---

### 4. Always Handle Async

```python
wait_until(...)
```

---

## 🧠 Key Insight

> **"Response is what the system says. Shell is what the system actually does."**

---

## 📌 Summary

Shell commands are used to:

1. Verify real system state (OS / hardware level)
2. Validate behavior after sending requests
3. Debug issues using logs

---

## 🔜 Future Extension

This project currently uses a mock (`run_cmd`).
In real systems, this can be replaced with:

* SSH commands:

```bash
ssh root@ccm "cat /sys/..."
```

* Real DBus communication
* Hardware interaction

---

Nếu bạn muốn, mình có thể giúp bạn viết thêm phần:

* **“Real System Integration (DBus + SSH)”** để README của bạn nhìn giống project production hơn 🚀
