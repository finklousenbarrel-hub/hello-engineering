# Agent 协作规范 v1
&gt; 2026-10-13 ｜ 实测环境：Cursor / Kimi Code CLI / 网页版 Kimi

## 〇、为什么需要规范
协作规范可以有效避免Agent出现的几类问题--幻觉/假完成/越权写入/精度不足照做/验收盲区等，保证任务执行的上限

## 一、需求侧：任务简报规范
- brief-template.md为任务简报模板，其中包含五要素
- 目标 需要让Agent做什么，不做什么
- 环境 项目架构+python与各依赖的版本
- 限制 明确说明Agent不做什么，一般配合universal-rules.md一起使用
- 改动边界 在该任务中可以新建和修改的文件清单，防止Agent越权写入和修改（案例：简报007 第一版限制与验收矛盾）
- 验收标准 正向条款和至少一条反向条款
- 自查清单 在交付agent执行之前人工检查可能存在的高频错误

## 二、执行侧：双层规则
- 通用铁律（引用 universal-rules.md：假完成防御、越权写入防御）
- 项目特化层（AGENTS.md 铁律 + .cursor/rules 机器执行层）
    AGENTS执行任务时会先阅读到AGENTS.md的正本，随后再由正本的链接阅读到引用的universal-rules.md，最后在执行前还会阅读.cursor/rules
- 说明：.cursor/rules/为cursor的私有格式，其它agents执行任务时并不会触发（除非在prompt里明确告知），所以需要一个AGENTS.md来提高普适性，在放入通用铁律之后，可以为项目添加只属于该项目的铁律

## 三、验收侧：独立复核原则
- 不信任执行者自述；
- 正向条款+反向条款（防止Agent出现静默丢失的情况）；
- 保留率验收；
- 迁移后必跑验收命令（防止文件迁移之后出现其它文件引用错误的问题）（案例：2026-10-02 data/patches 迁移后代码指向旧路径）;

## 四、失效治理：案例库制度
- 案例格式：失效类型+现象+原因+对策
- taxonomy：幻觉/假完成/越权写入/精度不足照做/验收盲区
- 案例→规则的立法流程：案例先录入案例库，根据是否具备普适性录入universal-rules或AGENTS.md
- 防御成功案例类别：在.cursor/rules写入文件名称规范与检查后，AGENTS能够自主识别出简报中存在的错误（2026-10-09 naming 规则拦截"fecth"笔误）

## 五、工具无关性
- 现象：agents主动跑 pytest / 自发幂等验证 / 边界自觉声明 / AGENTS.md 同步
- 实测结论：规范写在项目里而不是对话框里,只要规则足够完善，可以实现跨Agent协作，协作规范具备普适性。

## 附录：文件地图
- 案例库位置：hello-engineering/docs/agent-failure-log.md
- 通用铁律位置：hello-engineering/docs/universal-rules.md
- 简报模板位置：hello-engineering/docs/brief-template.md