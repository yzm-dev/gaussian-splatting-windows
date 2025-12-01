# Gaussian Splatting on Windows

本项目提供了在 Windows 平台上运行 Gaussian Splatting 的完整流程，包括环境配置、数据准备、模型训练（支持视频和图像输入）以及可视化查看。

## 一、获取仓库代码

### 1. 拉取仓库
```bash
git clone https://github.com/yzm-dev/gaussian-splatting-windows.git --recursive

# （可选）若没有--recursive拉取子模块，可用下面命令拉取：
git submodule update --init --recursive
```

### 2. 下载依赖包
请在 Release 中下载 `external.zip` 压缩包，并将其解压到项目根目录下。解压后，项目根目录应包含 `external` 文件夹，其中包含 `ffmpeg`、`colmap` 和 `viewers` 等工具。

## 二、环境安装

推荐使用 Anaconda 创建虚拟环境。

### 1. 安装 PyTorch (CUDA 11.8)
```bash
pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu118
```
*注意：请确保您的显卡驱动支持 CUDA 11.8。*

### 2. 安装其他依赖
```bash
pip install plyfile tqdm
```

### 3. 安装子模块
```bash
pip install -e submodules/simple-knn --no-build-isolation
pip install -e submodules/diff-gaussian-rasterization --no-build-isolation
```

## 三、数据准备与放置位置

建议将训练数据放置在 `data` 目录下。

### 目录结构示例
```
gaussian-splatting-windows/
├── data/
│   └── <dataset_name>/   # 例如: my_dataset
│       ├── <video_name>.mp4  # 如果使用视频训练
│       └── input/            # 如果使用图像训练 (存放图片)
├── external/
├── submodules/
├── output/
├── train_video.py
├── train_images.py
├── SIBR_viewer.py
└── ...
```

## 四、使用说明

本项目提供了三个主要的 Python 脚本来简化训练和查看流程。在使用前，请打开相应的脚本文件修改路径配置。

### 1. 使用视频进行训练 (`train_video.py`)

该脚本会自动将视频切分为图像帧，运行 COLMAP 估算相机位姿，并开始训练。

**使用步骤：**
1.  打开 `train_video.py`。
2.  修改 `video_path` 变量为您视频的绝对路径。
    ```python
    video_path = r"D:\path\to\your\video.mp4"
    ```
3.  (可选) 修改 `fps` 变量设置切帧频率（默认每秒 2 帧）。
4.  运行脚本：
    ```bash
    python train_video.py
    ```
    *脚本会自动在视频同级目录下创建 `input` 文件夹存放图片，并在 `output` 目录下生成训练结果。*

### 2. 使用图像进行训练 (`train_images.py`)

如果您已经有图像数据，可以直接使用此脚本。

**使用步骤：**
1.  将图像放入 `data/<dataset_name>/input` 文件夹中。
2.  打开 `train_images.py`。
3.  修改 `images_path` 变量为图像文件夹的绝对路径。
    ```python
    images_path = r"D:\path\to\your\data\input"
    ```
4.  运行脚本：
    ```bash
    python train_images.py
    ```
    *脚本会运行 COLMAP 并开始训练。*

### 3. 可视化查看结果 (`SIBR_viewer.py`)

训练完成后，使用此脚本查看 3D 高斯泼溅效果。

**使用步骤：**
1.  打开 `SIBR_viewer.py`。
2.  修改 `model_path` 变量为训练输出目录的绝对路径（通常在 `output/<dataset_name>`）。
    ```python
    model_path = r"D:\path\to\your\output\dataset_name"
    ```
3.  运行脚本：
    ```bash
    python SIBR_viewer.py
    ```
    *这将启动 SIBR Viewer 窗口展示渲染结果。*

## 五、注意事项

*   **路径问题**：脚本中使用了绝对路径，请务必根据您的实际文件位置进行修改。
*   **显存要求**：Gaussian Splatting 训练需要较高的显存，建议使用 24GB 显存的显卡（如 RTX 3090/4090），最低可能需要 8GB-12GB（取决于图像分辨率和数量）。
*   **COLMAP**：脚本会自动调用 `external` 目录下的 COLMAP，无需单独安装。

---
*Original README content can be found in `README_ORIGIN.md`.*
