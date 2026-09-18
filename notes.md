2026/09/17
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
