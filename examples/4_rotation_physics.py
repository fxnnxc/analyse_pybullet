import pybullet as p 
import pybullet_data
import time 
import numpy as np 

#================================
# === Perfect Circle Rotation ===
#================================

# === setup ===
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# === hyper parameters ===
radius = np.random.random()*5+2
theta =  np.random.random()* np.pi*2 
period = 100

# === create object ===
target_pos = [radius * np.cos(theta), radius* np.sin(theta)]
target = p.loadURDF("cube_small.urdf", target_pos+[0], globalScaling=5)
p.changeVisualShape(target, -1, rgbaColor=[255,255,0,1])
p.changeDynamics(target, -1, mass=1)
p.setTimeStep(1)


iteration = 0 
while True :
    # === vector calculus === 
    target_pos, _  = p.getBasePositionAndOrientation(target)
    next_pos = [radius * np.cos(theta+np.pi / period *2), radius* np.sin(theta+np.pi / period *2)]
    force = [next_pos[i] - target_pos[i] for i in range(2)] +[0]
    
    # === Physical Engine === 
    p.resetBaseVelocity(target, [0,0,0])
    p.applyExternalForce(target, -1, 
                        forceObj= force,
                        posObj=p.getBasePositionAndOrientation(target)[0],
                        flags=p.WORLD_FRAME)
    theta += np.pi / period *2 
    p.stepSimulation()
    time.sleep(0.05)

    iteration +=1 
    