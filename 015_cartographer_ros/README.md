# Cartgrapher

- [cartographer](https://github.com/cartographer-project/cartographer)

## テスト環境

- Ubuntu20.04
- Cuda 11.7

## buildコマンド

```bash
cd 015_cartographer_ros/
singularity build --fakeroot --sandbox <path>/singularity_definition_zoo/015_cartographer_ros/sandbox_cartographer Definitionfile.def 
```

## 起動コマンド

```bash
singularity shell --nv -B /run/user/1000,/var/lib/dbus/machine-id env/sandbox_cartographer/
source /entrypoint.sh
```

## 参考文献

- [cartographer-rosをcatkin buildでbuildする](https://qiita.com/Decwest/items/ac1a701a2217dd05e1fb)