import time
import hashlib

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}

    def is_allowed(self, device_id):
        current_time = int(time.time())
        for timestamp in list(self.requests.keys()):
            if current_time - timestamp > self.time_window:
                del self.requests[timestamp]
        if len(self.requests) >= self.max_requests:
            return False
        self.requests[current_time] = device_id
        return True

    def get_device_id(self, device_id):
        hashed_device_id = hashlib.sha256(device_id.encode()).hexdigest()
        return hashed_device_id

# Misol:
rate_limiter = RateLimiter(max_requests=5, time_window=60)  # 5 ta so'rov 1 daqiqa ichida
device_id = "1234567890"
hashed_device_id = rate_limiter.get_device_id(device_id)
if rate_limiter.is_allowed(hashed_device_id):
    print("So'rov qabul qilindi")
else:
    print("So'rov qabul qilinmadi")
