import pybullet as p 
import pybullet_data
import time 
import numpy as np 
import random 
#==============================================
# === Perfect Circle Rotation multiple case ===
#==============================================

# === setup ===
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# === hyper parameters ===
num_agents = 300
radius = [np.random.random()*1+3 for i in range(num_agents)]
theta =  [np.random.random()* np.pi*2 for i in range(num_agents)] 
period = [np.random.randint(100,1000) for i in range(num_agents)]

colors = [[1, 1,0], [255/255,192/255,203/255], [255/255, 153/255, 255/255], [255/255, 204/255, 0]]

# === create object ===
target_pos = [[radius[i] * np.cos(theta[i]), radius[i]* np.sin(theta[i])] for i in range(num_agents)]
target = [p.loadURDF("cube_small.urdf", target_pos[i]+[0], globalScaling=np.random.random()/2+1) for i in range(num_agents)]
for t in target:
    #p.changeVisualShape(t, -1, rgbaColor=[np.random.random(), np.random.random(),np.random.random(), 1])
    p.changeVisualShape(t, -1, rgbaColor=random.choice(colors)+[random.random()/2+0.5])
    
    p.changeDynamics(t, -1, mass=1)
p.setTimeStep(1)


iteration = 0 
while True :
    # === vector calculus === 
    target_pos  = [p.getBasePositionAndOrientation(t)[0][:2] for t in target]
    next_pos = [[r * np.cos(the +np.pi / per *2), r* np.sin(the+np.pi / per *2)] for r, the, per in zip(radius, theta, period)]
    force = [[next_pos[j][i] - target_pos[j][i] for i in range(2)] +[0] for j in range(num_agents)]
    
    # === Physical Engine === 
    for i in range(num_agents):
        p.resetBaseVelocity(target[i], [0,0,0])
        p.applyExternalForce(target[i], -1, 
                            forceObj= force[i],
                            posObj=p.getBasePositionAndOrientation(target[i])[0],
                            flags=p.WORLD_FRAME)
        theta[i] += np.pi / period[i] *2 
    p.stepSimulation()
    time.sleep(0.1)

    iteration +=1 
    