## gta-photo

把旅行、街道、建筑、室内和风景照片，转换成具有现代 GTA 游戏渲染感的场景，搭配《GTA：圣安地列斯》经典主机版布局 HUD。

保留照片里的地点与场景意图，通过游戏化材质、镜头、光照和交互细节，呈现“正在游戏世界中探索”的感觉。

![效果示例 01](docs/examples/example-01.png)

## 效果与功能

- **现代游戏画质：** 精细的实时 3D 渲染风格、中低饱和度、明显的辉光与空气雾、自然暗角和远景空气透视。
- **游戏镜头：** 默认采用约 24mm 广角与近背后跟随视角，主角以头肩和上半身为主。
- **场景驱动的动作：** 根据环境选择站立、跑动、骑行或交互；移动场景加入相应的运动模糊。
- **经典 HUD：** 左下角为平面矢量风格导航地图，右上角显示时间、生命值、装备与随机金额，并可根据状态显示护甲等元素。
- **固定装备素材：** 根据场景选择装备，使用随包图标进行合成，减少 AI 重绘造成的变形。
- **个性化细节：** 根据场景选择任务标记、交互菜单、空中交通或适合的装备状态。
- **上下对照输出：** 上方原图，下方游戏图，方便直接对比。

生成的游戏场景固定为 **16:9 横屏**。上下对照图的两个区域等高，整体比例为 **8:9**；原图完整居中显示，比例不匹配的空白区域填充黑色。

## 主角选择

上传照片时，可以同时输入：

| 指令 | 效果 |
| --- | --- |
| 不指定 | 有明确原主角时保留；没有时默认新增女性主角 |
| 主角男 | 使用男性主角 |
| 主角女 | 使用女性主角 |
| 无人 | 不新增主角，原图中的路人仍保留为 NPC |

![效果示例 03](docs/examples/example-03.png)

只有原图中位于中央、占比明显且确实是焦点主体的人物，才会自动作为原主角。画面边缘或远处的小人物保持为 NPC，不会被随意放大、移到中央或配上装备。

用户明确指定某个人物为主角时，以用户要求为准。

## 安装

本技能需要能够读取完整 Skill 目录、进行图片生成或编辑，并运行 Python 脚本；装备叠加和上下对照排版依赖 Python 与 Pillow。仅能进行文字对话的客户端，无法完成全部流程。

在能够访问 GitHub 并加载本地 Skill 的 Codex / Agent 环境中，复制以下指令，并替换链接：

> 请从 https://github.com/carol911/gta-photo 安装 gta-photo 技能。请安装完整目录，保留 assets、scripts、references 和 agents 文件夹。安装后检查固定装备图标、渲染参考图片及合成脚本是否齐全；如有文件缺失，请明确提示，不要自行用 AI 重绘替代固定装备图标。

安装完成并确认技能已被识别后，上传照片并调用技能。

也可以下载本仓库，将包含 `SKILL.md` 的完整技能文件夹安装到所用客户端的技能目录中。不要只复制 `SKILL.md` 或删除附属素材。

## 使用示例

上传照片后输入：

> 使用 gta-photo 处理这张照片。

也可以加入具体要求：

> 使用 gta-photo，主角女，站在风景前，背着长枪。

> 使用 gta-photo，主角男，沿道路跑动。

> 使用 gta-photo，无人，保留原图中的路人。

> 使用 gta-photo，只输出游戏图，不需要上下对照。

明确的用户要求优先于默认场景判断。可以指定主角、动作、装备、氛围以及输出形式。

![效果示例 05](docs/examples/example-05.png)

![效果示例 04](docs/examples/example-04.png)

![效果示例 02](docs/examples/example-02.png)

## 文件说明

| 文件或文件夹 | 用途 |
| --- | --- |
| `SKILL.md` | 技能入口及核心流程 |
| `references/` | 渲染、镜头、人物、HUD 与输出规则 |
| `assets/gtabase-equipment/` | 固定装备图标 |
| `assets/render-references/` | 游戏渲染参考图片 |
| `scripts/` | 装备图标合成、状态选择及上下对照排版 |
| `agents/` | 技能显示与默认调用配置 |

请保留完整目录结构。缺少素材或脚本，会影响图标准确性、参考读取或最终排版。

## 素材来源与效果说明

装备图标来源于 [GTABase 的 GTA：圣安地列斯装备资料页面](https://www.gtabase.com/gta-san-andreas/weapons/)。渲染参考为第三方游戏画面，具体来源与完整性信息见随包说明。这些素材并非本项目原创。

本项目为非官方照片转换工作流，采用现代游戏渲染风格与经典 HUD 布局。交互细节可能包含适配设计，不保证逐项复刻某一游戏版本的原生画面。

图像生成具有随机性，效果会受到输入照片、用户要求、执行环境及图像工具能力的影响。固定素材合成用于提高装备图标的稳定性，不代表整张图能够完全确定性复现。

## Disclaimer / 免责声明

* **Purpose:** The *Grand Theft Auto* (GTA) related images and reference materials used in this repository are for **non-commercial, educational, and technical demonstration purposes only** (specifically for style-transfer and graphics generation referencing).
* **Intellectual Property:** Grand Theft Auto and related trademarks, game assets, and intellectual property belong to their respective rights holders, including Rockstar Games and Take-Two Interactive. This project is unofficial and is not affiliated with or endorsed by them. No copyright infringement is intended.
* **Originality Statement:** The generated images produced by this project are based on user-submitted travel/personal photographs and are inspired by the iconic GTA artistic style. These generated works are independent creations and do **NOT** represent official artwork, promotional materials, or upcoming leaks from Rockstar Games.

---

* **使用目的：** 本仓库中使用的《侠盗猎车手》(GTA) 相关截图及参考素材，仅用于**非商业性的学术交流、技术演练及图形生成（风格迁移）的参考示范**。
* **版权归属：** 《Grand Theft Auto》相关商标、游戏资产及知识产权归其各自权利人所有，包括 Rockstar Games 与 Take-Two Interactive。本项目为非官方项目，与上述公司不存在隶属、授权或背书关系。本仓库无意冒犯或侵犯任何合法权益。
* **原创性声明：** 本项目所生成的最终图像均基于用户个人旅游/生活照片，仅在艺术风格上向 GTA 致敬。生成作品均为独立创作，**绝不代表** Rockstar Games 官方的艺术画面、宣传物料或未公开的游戏泄露内容。
