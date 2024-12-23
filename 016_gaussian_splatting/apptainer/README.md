# Gaussian Splatting

## Support

- [LangSplatting](https://github.com/minghanqin/LangSplat)

## テスト環境

- Ubuntu20.04
- Cuda 11.7

## buildコマンド

```bash
cd 016_gaussian_splatting/apptainer/
apptainer build --fakeroot --sandbox sandbox_langsplat langsplat_ros2.def

apptainer shell --nv sandbox_langsplat
source /entrypoint.sh
cd langSplat/submodules/simple-knn
python -m pip install -e .
```

## Model/Datasets Downloads

- download the checkpoints of SAM Model (sam_vit_h_4b8939.pth) from [here](https://github.com/facebookresearch/segment-anything?tab=readme-ov-file#model-checkpoints) to `ckpts/.`
- download test dataset form [here](https://drive.google.com/drive/folders/1kdV14Gu5nZX6WOPbccG7t7obP_aXkOuC?usp=sharing)

## How to run

```bash
apptainer shell --nv sandbox_langsplat
source /entrypoint.sh
```
