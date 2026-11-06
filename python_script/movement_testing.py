from rtde_control import RTDEControlInterface as Ctrl
from rtde_receive import RTDEReceiveInterface as Rcv

c = Ctrl("127.0.0.1")
r = Rcv("127.0.0.1")

q0 = r.getActualQ()
q1 = list(q0)
q1[0] += 0.2          # rotate the base joint by 0.2 rad (about 11 degrees)

c.moveJ(q1, 0.3, 0.3)  # speed rad/s, acceleration rad/s^2
c.moveJ(q0, 0.3, 0.3)  # return to the start

c.stopScript()
c.disconnect()
r.disconnect()