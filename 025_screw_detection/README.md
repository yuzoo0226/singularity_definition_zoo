# Environment for [Screw Detection](https://github.com/yuzoo0226/screw_detection)

## How to build

```bash
apptainer build --fakeroot --sandbox ~/usr/env/sandbox_screw_detection_cu117 screw_detection_cu117.def
```

```bash
git clone https://github.com/eyildiz-ugoe/screw_detection.git
apptainer shell --fakeroot --writable --nv ~/usr/env/sandbox_screw_detection_cu117
cd screw_detection
python setup.py
```

## How to start

```bash
apptainer shell --nv ~/usr/env/sandbox_screw_detection_cu117
```

## How to use

```bash
python scripts/check_xception.py
```
