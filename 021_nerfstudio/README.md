# Environment for [Nerf-Studio](https://github.com/nerfstudio-project/nerfstudio)

## How to build

```bash
apptainer build --fakeroot --sandbox ~/usr/env/sandbox_nerfstudio_cu118 nerfstudio_cu118.def
```

## How to start

```bash
apptainer shell --nv ~/usr/env/sandbox_nerfstudio_cu118
```

## How to use

```bash
git clone https://github.com/nerfstudio-project/nerfstudio.git
ns-download-data nerfstudio --capture-name=poster
ns-train nerfacto --data data/nerfstudio/poster
```

- Open `http://localhost:7007` in your browser.
