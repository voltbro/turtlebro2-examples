from robot_msgs.msg import CPUInfo

msg = CPUInfo()
msg.temp = 55.1
msg.cpu0_freq = 1600000
msg.cpu1_freq = 1600000
msg.cpu2_freq = 1600000
msg.cpu3_freq = 1600000


print(msg)