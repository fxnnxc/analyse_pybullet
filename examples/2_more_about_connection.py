import time 
import pybullet as p 

p.connect(p.DIRECT)
print(p.getConnectionInfo())
print(p.isConnected())
p.setTimeOut(100)
