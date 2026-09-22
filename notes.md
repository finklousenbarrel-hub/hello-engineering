2026/09/17 晴
为什么git bash不能用Ctrl+V粘贴！真是麻烦

一些基础操作流程
1. 配置账号
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

2. 仓库镜像到本地
mkdir -p ~/Documents/ai-engineering && cd ~/Documents/ai-engineering
git clone https://github.com/你的用户名/hello-engineering.git
cd hello-engineering

3. 本地内容更改之后提交到github
git add notes.md
git commit -m "content"
git push

4. 常用命令
git status    # 看看现在有哪些变化还没存档（改完文件先跑这个）
git diff      # 精确显示你改了哪几行——封存前最后核对一遍


2026/09/18
## Day 2 学到的命令
1. 创立分支
cd ~/Documents/ai-engineering/hello-engineering
git switch -c feature/day2-notes

2. 分支上改东西
git add notes.md
git commit -m "docs: 添加day2分支练习笔记"

3. 切换主线
git switch main

4. 合并主线
git switch main
git merge feature/day2-notes
git push

5. 查找与找回
git log --all --oneline
git reflog
git show （哈希值）

2026/0919
git clone 别人的项目
cd 项目
python -m venv .venv           # 给他单独盖间厨房
.venv\Scripts\Activate.ps1     # 进厨房
pip install -r requirements.txt # 照他的菜谱备料

2026/09/22
## 断点调试
作用：适用于某处函数或者循环卡住了，然后一步步去拆解

launch.json的作用
调试谁？在哪调试？如何起跑？

调试操作：在行数前打红点（点击），F10单步执行，F11钻进函数里看，F5运行至下一个断点（包括起手也是F5）

## logging（给自己看的输出）
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logging.info
logging.warning