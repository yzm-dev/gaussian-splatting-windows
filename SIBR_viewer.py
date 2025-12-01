import subprocess

# output保存路径
model_path = r'D:\yuzhm01\Desktop\gaussian-splatting-windows\output\ggbond'

# 脚本执行
command = f'SIBR_gaussianViewer_app.exe -m {model_path}'
run_path = 'external/viewers/bin'
subprocess.run(command, shell=True, cwd=run_path)
