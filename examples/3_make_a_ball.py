import pybullet as p 
import pybullet_data 
import numpy as np 
import time 

# === setup ===
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# === objects ===
agent = p.loadURDF("cube_small.urdf", globalScaling=2)
target = p.loadURDF("cube_small.urdf", [3,3,0], globalScaling=2)
p.changeVisualShape(agent, -1,  rgbaColor=[0,255,255,1])
p.changeVisualShape(target, -1, rgbaColor=[255,255,0,1])
p.changeDynamics(agent, -1, mass=0.001)

# === move params === 
f = 10.0
dx = [0,0,f,-f]
dy = [f,-f,0,0]

# === Run Simulation === 
while True:
    action = np.random.randint(4)
    p.applyExternalForce(agent, -1, 
                        forceObj=[dx[action],dy[action],0],
                        posObj=p.getBasePositionAndOrientation(agent)[0],
                        flags=p.WORLD_FRAME)
    p.resetBaseVelocity(agent, [0,0,0])
    p.stepSimulation()
    #print(p.getBasePositionAndOrientation(agent), end=" ")
    #print(p.getBasePositionAndOrientation(target))
    
    # === realtime control ===
    time.sleep(1)
p.disconnect()