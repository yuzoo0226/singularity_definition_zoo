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

```bash
git clone https://github.com/nerfstudio-project/nerfstudio.git
ns-train lerf --data data/nerfstudio/poster
```
