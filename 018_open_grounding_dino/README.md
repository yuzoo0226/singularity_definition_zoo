# [Open Grounding DINO](https://github.com/longzw1997/Open-GroundingDino)

```bash
apptainer build --fakeroot --sandbox sandbox_gdino_cu121 open_grounding_dino.def
```

# [Lang-SAM (sam2)](https://github.com/yuzoo0226/lang-segment-anything-langsplat2.git)

## How to build

```bash
apptainer build --fakeroot --sandbox sandbox_langsam_cu124 open_grounding_dino.def
```

## How to run

```bash
apptainer shell --nv sandbox_langsam_cu124
git clone https://github.com/yuzoo0226/lang-segment-anything-langsplat2.git
cd lang-segment-anything
python test.py
```
