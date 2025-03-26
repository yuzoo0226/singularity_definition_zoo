# For Nerf repositories

## Environment for [NeRF-Studio](https://github.com/nerfstudio-project/nerfstudio)

### How to build

```bash
apptainer build --fakeroot --sandbox ~/usr/env/sandbox_nerfstudio_cu118 nerfstudio_base_cu118.def
```

### How to start

```bash
apptainer shell --nv ~/usr/env/sandbox_nerfstudio_cu118
```

### How to use nerfstudio

```bash
git clone https://github.com/nerfstudio-project/nerfstudio.git
ns-download-data nerfstudio --capture-name=poster
ns-train nerfacto --data data/nerfstudio/poster
```

- Open `http://localhost:7007` in your browser.

## Environment For Lerf

```bash
apptainer build --fakeroot --sandbox ~/usr/env/sandbox_lerf_cu118 nerfstudi0_lerf_cu118.def
```

### Update Nerfstudio

```bash
apptainer shell --nv --fakeroot --writable ~/usr/env/sandbox_lerf_cu118
source /entrypoint.sh
ns-install-cli
```

### How to start lerf

```bash
apptainer shell --nv ~/usr/env/sandbox_lerf_cu118
```

### How to use lerf

#### Train

```bash
git clone https://github.com/nerfstudio-project/nerfstudio.git
ns-train lerf --data data/nerfstudio/poster
```

#### Render

```bash
ns-render camera-path --load-config outputs/figurines/lerf-lite/2025-03-25_161604/config.yml --camera-path-filename ~/usr/splat_ws/baseline/nerfstudio_lerf/eval_iou_path.json --output-path renders/figurines/eval_iou_path/ --output-format images --rendered-output-names relevancy_0 --image-format png
```

#### Use custome data

```bash
ns-process-data images --data /mnt/home/yuga-y/usr/splat_ws/datasets/3d_ovs/sofa/images --output-dir /mnt/home/yuga-y/usr/splat_ws/datasets/lerf_3d_ovs/sofa --no-gpu
```
