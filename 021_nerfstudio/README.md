# Environment for [Nerf-Studio](https://github.com/Kunhao-Liu/3D-OVS)

## How to build

```bash
apptainer build --fakeroot --sandbox ~/usr/env/sandbox_ovs_cu118 3d_ovs_cu118.def
```

## How to start

```bash
apptainer shell --nv ~/usr/env/sandbox_ovs_cu118
```

## How to use

- 3d_ovsをgitからcloneする
- Datasetをダウンロードし， `./data`フォルダ内に配置する
- 以下のコマンドを実行すると，`bed`での認識が実行される

```bash
bash scripts/test_segmentation.sh ~/usr/splat_ws/third_party/3D-OVS/checkpoints/bed.th configs/bed.txt 0
```
