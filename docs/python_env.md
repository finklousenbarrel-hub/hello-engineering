## 从0开始建立虚拟环境
1. 新建
    .gitignore
2. 写入
    __pycache__/
    *.pyc
    .venv/
    .vscode/
3. 激活
    .venv\Scripts\Activate.ps1
4. requirements.txt
    pip freeze > requirements.txt
5. 验证是否在虚拟环境
    python -c "import sys; print(sys.executable)"

## 再次激活（梅开二度）
1. .venv\Scripts\Activate.ps1
2. .venv\Scripts\python.exe -m pip install requests
3. 写自动化脚本
    function venv { .\.venv\Scripts\Activate.ps1 }
    3.1 建立 $PROFILE
        3.1.1 在不在
            $PROFILE                 # 打印路径，一般在 Documents\WindowsPowerShell\ 下
            Test-Path $PROFILE       # True = 已存在，False = 还没建
        3.1.2 如果是 False，一条命令建出来
            New-Item -ItemType File -Force $PROFILE
        3.1.3 打开编辑
            notepad $PROFILE
            打开编辑后 function venv { .\.venv\Scripts\Activate.ps1 }

## freeze出来字符带空格
现象：freeze 出来字符带空格
原因：PowerShell > 默认 UTF-16
解法：pip freeze | Out-File -Encoding utf8 requirements.txt