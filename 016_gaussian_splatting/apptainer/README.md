# Gaussian Splatting

## Support

- [LangSplatting](https://github.com/minghanqin/LangSplat)
- [OpenGaussian](https://github.com/yanmin-wu/OpenGaussian)

## テスト環境

- Ubuntu22.04
- Cuda 11.8

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
- download opengaussian/langsplat dataset [here](https://github.com/yanmin-wu/OpenGaussian?tab=readme-ov-file#2-data-preparation)

## How to run

```bash
apptainer shell --nv sandbox_langsplat
source /entrypoint.sh
```

## LangSplatの動かし方

- ダウンロードしたデータセットに対して，Colmapを適用する

```bash
git clone --recursive https://github.com/graphdeco-inria/gaussian-splatting.git
cd gaussian-splatting
python -m pip install submodules/diff-gaussian-rasterization
python train.py -s ../../datasets/lerf_ovs/teatime/ --checkpoint_iterations 7000 30000
```

- 以下のエラーが出たときはこの[issue](https://github.com/graphdeco-inria/gaussian-splatting/issues/1032)を参考に

```bash
 > python train.py -s ../../datasets/lerf_ovs/teatime/ --checkpoint_iterations 7000 30000
Optimizing 
Output folder: ./output/182da88b-f [24/12 02:54:36]
Reading camera 177/177 [24/12 02:54:36]
Loading Training Cameras [24/12 02:54:36]
Loading Test Cameras [24/12 02:54:38]
Number of points at initialisation :  25503 [24/12 02:54:38]
Training progress:   0%|                                                   | 0/30000 [00:00<?, ?it/s]Traceback (most recent call last):
  File "/home/tamhome/usr/gs_ws/src/gaussian-splatting/train.py", line 282, in <module>
    training(lp.extract(args), op.extract(args), pp.extract(args), args.test_iterations, args.save_iterations, args.checkpoint_iterations, args.start_checkpoint, args.debug_from)
  File "/home/tamhome/usr/gs_ws/src/gaussian-splatting/train.py", line 111, in training
    render_pkg = render(viewpoint_cam, gaussians, pipe, bg, use_trained_exp=dataset.train_test_exp, separate_sh=SPARSE_ADAM_AVAILABLE)
  File "/home/tamhome/usr/gs_ws/src/gaussian-splatting/gaussian_renderer/__init__.py", line 36, in render
    raster_settings = GaussianRasterizationSettings(
TypeError: <lambda>() got an unexpected keyword argument 'antialiasing'
Training progress:   0%|                                                   | 0/30000 [00:00<?, ?it/s]
```

- Langsplatのautoencoderを学習する

```bash
cd LangSplat
python preprocess.py --dataset_path ../../datasets/3d_ovs/table/
cd autoencoder
python train.py --dataset_name table --encoder_dims 256 128 64 32 3 --decoder_dims 16 32 64 128 256 256 512 --lr 0.0007 --dataset_path ../../../datasets/3d_ovs/table/
python test.py --dataset_name table --dataset_path ../../../datasets/3d_ovs/table/

cd ../
python train.py -s ../../datasets/3d_ovs/table/ -m output/table_test01 --start_checkpoint ../../datasets/lerf_ovs/teatime/output/teatime_v1/chkpnt30000.pth --feature_level 1 
```
