# Physical Engine in Pybullet


```python
import pybullet as p
import pybullet_data
```

|code|effect|
|---|---|
|```physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version```python|return the physical client id|
|`p.disconnect()`|disconnect to the server. |
| `p.setAdditionalSearchPath(pybullet_data.getDataPath())`| link to the `pybullet_data` package|
|`p.setGravity(0,0,-10)`| set the environment gravity |
|`id = p.loadURDF("plane.urdf")`| return the object id|
|`ori = p.getQuaternionFromEuler([0,0,0])` | get orientation|
|`boxId = p.loadURDF("r2d2.urdf",startPos, startOrientation)`|construct with pos and ori|
|`p.stepSimulation()`|run one step simulation|
|pos, ori = `p.getBasePositionAndOrientation(boxId)`|get position and orientation of the object|

