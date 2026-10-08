# 渲染参考选择与来源

## 使用方式
新场景转换时先按场景从下表选1张环境/镜头参考，必要时另选1张角色或光照参考，实际查看选中的文件。图片编辑工具支持多参考时，将用户照片放第一位、选中的参考放后；明确只借用渲染与设计特征，不搬运人物身份、建筑、原场景构图组合、招牌、武器或HUD。不可一次传入整套参考；不支持多图时使用文字规则，说明未使用附加视觉参考，不伪称已加载。

对已认可成图只修图标/金额等局部元素时，以该成图为主参考，只查看相应图标规则，不加载无关环境或人物参考以免触发全图重绘。

这些图片是用户提供并允许纳入此技能的GTA视觉参考；游戏画面权利归相应权利人，不属于本工作流原创。用户称它们来自官方；已核查Rockstar存在官方媒体入口，但未逐帧核验每张上传图的来源/修改情况，不把此包称为官方授权素材库。
官方来源核查入口：https://www.rockstargames.com/VI/media
GTA V入口：https://www.rockstargames.com/V/
不要根据文件名或画面里的HUD断言具体正式版本、原生菜单或运行平台。不要移除原图上的任何来源标识。公开分发本技能时应如实标明这些是第三方参考，不能将“官方发布”表述为“开放授权”；未核实再分发许可。

## 文件与作用
所有文件位于 assets/render-references/。这些仅校准3D渲染，不覆盖hud-spec。

| 文件 | 只提取这些特征 |
|---|---|
| character-outfit.webp | 角色层次、花衬衫与配饰、体积；不要复制海报站姿、枪或车 |
| night-follow.webp | 腿脚出画的近背后跟随、街灯光池和暗部；不搬入路人或街道 |
| daylight-follow.webp | 头肩至躯干的近背侧跟随、室内外亮度差、肩背体积；不搬入汽车 |
| cloth-environment.webp | 衣物受力褶皱、建模植被、皮肤与车漆材质差异 |
| social-outfits.webp | 坐姿、修身服装与多人物空间；不默认正面聚餐机位 |
| character-surface.webp | 脸部体积、轻微皮肤纹理、发束和布料；仅近景材质参考 |
| daylight-motion.webp | 腰胯出画的近跟随、白色建筑局部溢光、短款球衣和斜挎包轮廓；不复制武器、星星或现有文字 |
| beach-material.webp | 沙地、皮肤、遮阳伞的材质区分；不把所有地点改海滩 |
| city-depth.jpg | 远景蓝色空气透视、道路模型与植被层次；不复制洛圣都地标 |
| interior-bloom.webp | 近过肩、暗前景对亮门口、灯管局部辉光；不复制持枪姿势、武器或准星 |
| sun-glare.webp | 太阳附近局部眩光、暖灰远景、近处深色体块；步行场景不复制车辆跟随和速度模糊 |
| terrace-light.webp | 克制的大面积色彩、明亮建筑与遮蔽前景的曝光层次 |
| skyline-air.webp | 远楼空气层次、克制调色与少量空中交通；不复制横幅或地标 |

## 代表图校准
优先用 city-depth.jpg、terrace-light.webp、skyline-air.webp 校准整体调色和空气层次，按场景选其中1张，必要时另配镜头/人物参考，总数仍为1–2张。
- terrace-light：暖色受光建筑与深色遮蔽前景有明显曝光差；四周暗部不能全部解释为后期暗角。大面积色彩克制，气球等局部仍鲜艳。
- skyline-air：远景低对比、淡灰蓝空气层次；天空存在直升机和拖横幅小飞机，但静帧不能证明高速或战斗。不要复制横幅文字。
- city-depth：蓝灰距离雾强烈，远楼弱对比，近处植被体块清楚；并非所有区域都低饱和，也没有明显重暗角。
自然镜头亮度衰减、增强辉光与移动NPC模糊是本工作流的风格设定，不宣称三张图逐项证明这些效果；暗角强度与禁止黑框的要求以lighting-rules为准。

## 可复核的视觉观察
- 日景中建筑受光面清楚，阴影不是统一黑色；近处材质有细节，远处对比度随距离下降。
- 皮肤有柔和高光和少量纹理，肩臂有真实体积；头发由发束与细丝共同形成，不是塑料头盔。
- 服装不是越宽大越有街头感：合身上装与宽松下装、短外套与内搭、项链/耳环/腕表/帽子/包形成设计层次。
- 跟随镜头中的角色有足够屏幕分量；近景、过肩和远景各有任务，不把所有图当同一种固定机位。
- 游戏感来自共同的资产、着色与相机语言；删光微细节、狂加饱和度、强行硬阴影都不是普适答案。
- 参考里的菜单、通缉、矩形雷达不作为SA主机版UI依据；背景有人、枪或汽车也不要求输出复制这些元素。

## 完整性标识
本发布包的PNG渲染参考已转换为无损WebP，未裁切、缩放或重绘，解码RGBA像素逐张比对一致；city-depth.jpg保留原始字节。下列SHA-256用于核对分发资产，另列原始PNG校验值；它们不是来源真实性证明。
- `character-outfit.webp`: `f54c42a2c039f3a48b62436f59618703639e733589d27211bfc53b525dec0aaa`（原始PNG SHA-256：`4d91dc30d50d90a33afc0538d6f0a8836897dc9176dd20e5af7aa628de15d027`）
- `night-follow.webp`: `8c42c21fdc92eb0c6ce3d3deb19f4dbedcb39d353735a5e3778a9d54e1d89423`（原始PNG SHA-256：`1ff0d6a9abeeee15bd8d959fe9d0f0cd9e087e6ac760e504ec629b583626c704`）
- `daylight-follow.webp`: `17546b542afcc18095b3776a1e186e5da161bb288c7285a0b548bd5d296f2852`（原始PNG SHA-256：`1985bf1e2ee45d09287f4f7d6f721fa0d6d9a2226dca7aba533ee4f37428078a`）
- `cloth-environment.webp`: `af69faa896f53a0615bb77fda45876bcb537ab4b59fd351e501ca26bbc8bb391`（原始PNG SHA-256：`12c0751a01940cccd920a4c4f52991f591081acbaa102f78e408be03cd56931a`）
- `social-outfits.webp`: `7b3afc2293feea64d1946347600d06fc7c215966da527dfccd8576770206888f`（原始PNG SHA-256：`0047b990d69b199f9c6f74e6bbdc98d88752b5e834a8a2929ac617228bd4544a`）
- `character-surface.webp`: `f54990f57097062c3b068d05bc870ac88981262c11d3fc61efc9d8346b2a0d58`（原始PNG SHA-256：`81f96eeadb0bdd5efc0c120a1ced5355760f8a5d429f5da636f2c1072568f107`）
- `daylight-motion.webp`: `9e5aae28c653ebc97b7c57e3b98ad110fc1c510801ea24c43dbd0b1ee5e63584`（原始PNG SHA-256：`e8f4956fde659abc7d5876a47bf2dc8fd4dc47101ac1f303b395ad728e55162c`）
- `beach-material.webp`: `b774d3214f2ab72638d15341eb15de0b7aef114fc3f8ce9b48852909e26b8348`（原始PNG SHA-256：`50069daf8514a2a448c078af671c30022c064ca161e1543f77da2b40fcafe416`）
- `city-depth.jpg`: `2b49e9c96617a7fe7d52c4c1d04f479b270178ea53017a7ab3cc269989f7cb37`
- `interior-bloom.webp`: `8e673dcb453b04a033cbc7512b1208bc7880f2676a0dfe7a5390da3c95780d5d`（原始PNG SHA-256：`972b6bbfe3939578a0b9acee467d5fc739bb7eb433402828f99b47095fc236b7`）
- `sun-glare.webp`: `26a002fcb24e40ce69336d3d3e7478f82a6db5618c6c7c5a47446182813b7397`（原始PNG SHA-256：`6b94e368d7b08a894ce9948b8cff3642dd2171658ec6ba896b995ef52c1f1e4e`）
- `terrace-light.webp`: `201bfef55a22be80e484a2b4b750022993f39a09cccbd3fe5819665160b975d7`（原始PNG SHA-256：`9d4696dc555b92ecc71969537366e9b9e6a557e8f49cd8ad54ea4a3020d969b9`）
- `skyline-air.webp`: `c7804891b44c431709a8e57171a57e7b26109e84ad6dfe84ef053b3a294d188b`（原始PNG SHA-256：`d20713235d9a1f920eda6e0ef8936c23ffac0304db7fba00fc8b1bf354cc2a13`）
