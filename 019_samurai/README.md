# Environment for [SAMURAI](https://github.com/yangchris11/samurai)

## How to build

```bash
apptainer build --fakeroot --sandbox ~/usr/env/sandbox_samurai_cu118 samurai_cu118.def
```

```bash
apptainer shell --nv --fakeroot --writable ~/usr/env/sandbox_samurai_cu118
cd sam2
pip install -e .
pip install -e ".[notebooks]"

cd
cd usr/splat_ws/src/Langsplat2/submodules/
cd segment-anything-langsplat/
pip install .
cd ../

```

## How to start

```bash
apptainer shell --nv ~/usr/env/sandbox_samurai_cu118
```
