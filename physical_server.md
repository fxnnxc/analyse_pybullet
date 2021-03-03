
# Physical Server 



<img >

```python
pybullet.connect(pybullet.DIRECT)
pybullet.connect(pybullet.GUI, options="--opengl2")
pybullet.connect(pybullet.SHARED_MEMORY,1234)
pybullet.connect(pybullet.UDP,"192.168.0.1")
pybullet.connect(pybullet.UDP,"localhost", 1234)
pybullet.connect(pybullet.TCP,"localhost", 6667)
pybullet.disconnect(client_id)
```

## Direct 

Physical Server에 Direct 하게 Command를 보내는 방식입니다. GUI를 사용하지 않으며, 결과를 바로 받아옵니다. 

## GUI

`3D OpenGL` 렌더링으로 GUI를 만들어줍니다. Linux와 Window에서는 GUI Rendering을 위한 다른 Thread를 사용하지만, Mac OSX에서는 OS의 제한사항으로 동일한 Thread에서 렌더링을 합니다. 

`Pybullet Clinet` <->  `GUI physics Simulation Server `

## SHARED_MEMORY

동일한 Machine의 다른 Physical Server와 `Shared memory`로 연결을 하는 방법입니다.

## TCP, UDP

remote Machine의 다른 Physical Server와 `Shared memory`로 연결을 하는 방법입니다.