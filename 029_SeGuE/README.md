# Environment for [SeGuE]()

## How to build

```bash
apptainer build --fakeroot --sandbox ~/usr/env/sandbox_segue_cu121 segue_cu121.def
```

```bash
apptainer shell --nv --fakeroot --writable ~/usr/env/sandbox_segue_cu121

```

## How to start

```bash
apptainer shell --nv ~/usr/env/sandbox_segue_cu121
```
