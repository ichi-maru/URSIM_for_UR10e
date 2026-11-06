import time
from rtde_receive import RTDEReceiveInterface as Rcv

IP = "127.0.0.1"
RATE_HZ = 10
PERIOD = 1.0 / RATE_HZ

r = Rcv(IP, frequency=RATE_HZ)
try:
    next_t = time.perf_counter()
    while True:
        q = r.getActualQ()
        tcp = r.getActualTCPPose()
        print(f"q={[round(v, 3) for v in q]}  tcp={[round(v, 3) for v in tcp]}")
        next_t += PERIOD
        time.sleep(max(0.0, next_t - time.perf_counter()))
except KeyboardInterrupt:
    pass
finally:
    r.disconnect()