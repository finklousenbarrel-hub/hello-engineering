1. 工具迁移时要逐项验证旧环境的自动化行为是否还在，不能默认平移（例如虚拟环境）
2. Keep ALL 之前需要逐条跑验收命令

3. 关于$PROFILE的用法

- 检查是否存在
bash'''
$PROFILE                 # 打印路径，一般在 Documents\WindowsPowerShell\ 下
Test-Path $PROFILE       # True = 已存在，False = 还没建
'''

- 一键建立
bash'''
New-Item -ItemType File -Force $PROFILE
'''

- 打开编辑
bash'''
notepad $PROFILE
'''
添加一键启动虚拟环境命令
bash'''
function venv { .\.venv\Scripts\Activate.ps1 }
'''
