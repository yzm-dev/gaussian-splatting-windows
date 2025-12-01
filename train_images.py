import os
import subprocess

# 数据集所在的绝对路径
images_path = r"D:\yuzhm01\Desktop\gaussian-splatting-windows\data\ggbond\input"

folder_path = os.path.dirname(images_path)
# 数据集名称文件夹 ggbond
dataset_name = os.path.basename(folder_path)

# COLMAP估算相机位姿
command = f'python convert.py -s {folder_path}'
subprocess.run(command, shell=True)

# 模型训练脚本，训练从folder_path/sparse/0/中读取相机位姿，模型会保存在项目output/dataset_name
output_path = os.path.join(os.path.dirname(os.path.dirname(folder_path)), 'output', dataset_name)
command = f'python train.py -s {folder_path} -m {output_path}'
subprocess.run(command, shell=True)
