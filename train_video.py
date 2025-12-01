import os
import subprocess

# 视频绝对路径
video_path = r"D:\yuzhm01\Desktop\gaussian-splatting-windows\data\ggbond\ggbond.mp4"

# 切分帧数，每秒多少帧
fps = 2

# 获取当前工作路径
current_path = os.getcwd()

folder_path = os.path.dirname(video_path)
# 数据集保存路径 data/ggbond/input
images_path = os.path.join(folder_path, 'input')
os.makedirs(images_path, exist_ok=True)
# 数据集名称文件夹 ggbond
dataset_name = os.path.basename(folder_path)

ffmpeg_path = os.path.join(current_path, 'external', r'ffmpeg/bin/ffmpeg.exe')

# 视频切分脚本
command = f'{ffmpeg_path} -i {video_path} -qscale:v 1 -qmin 1 -vf fps={fps} {images_path}\\%04d.jpg'
subprocess.run(command, shell=True)

# COLMAP估算相机位姿
command = f'python convert.py -s {folder_path}'
subprocess.run(command, shell=True)

# 模型训练脚本，训练从folder_path/sparse/0/中读取相机位姿，模型会保存在项目output/dataset_name
output_path = os.path.join(os.path.dirname(os.path.dirname(folder_path)), 'output', dataset_name)
command = f'python train.py -s {folder_path} -m {output_path}'
subprocess.run(command, shell=True)
