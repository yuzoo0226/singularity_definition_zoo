# Environment for [Object Tracking](https://github.com/Kunhao-Liu/3D-OVS)

## How to build

```bash
apptainer build --fakeroot --sandbox ~/usr/env/sandbox_cutie_noetic_cu117 cutie_noetic_cu117.def
```

```bash
apptainer shell --fakeroot --writable --nv ~/usr/env/sandbox_cutie_noetic_cu117

cd ros_ws/src/
git clone git@github.com:yuzoo0226/cutie-ros.git
cd cutie-ros
git checkout devel/noetic
cd src
pip install .
```

## How to start

```bash
apptainer shell --nv ~/usr/env/sandbox_cutie_noetic_cu117
```

## How to use

```bash
rosrun cutie_ros cutie_service_node.py
```
