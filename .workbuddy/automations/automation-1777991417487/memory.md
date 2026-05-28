# 自动化执行记忆 - 热梗歌词音乐生成器

## Prompt多元化改造记录（2026-05-22）

**用户需求**: 歌词歌曲更多元化（原20首歌6首流行抒情+4首波浪，同质化严重）
**改造完成**: ✅ 已更新prompt，下次执行（2026-05-23）生效
**核心变化**:
- 音乐流派: Pop固定 → 7种流派随机(Pop/R&B/Rock/Folk/Electronic/CityPop/Indie)
- 演唱者: 固定female → 联动流派概率随机
- 歌词主题: 联动流派方向(治愈/热血/叙事/抽象/浪漫/反套路)
- 规则: 不连续两次相同流派
- 附带精简prompt解决input length too long问题

---

## 最新完整执行记录（2026-05-29）

### 执行概况
- **执行时间**: 2026-05-29 07:00
- **热梗**: 全职儿女（2026年持续走红的社会现象，指年轻人毕业后全职在家，既照顾父母又备考/求职的状态）
- **节奏风格**: B（中速型，全曲90-100BPM，Hook略快）
- **音乐风格**: R&B 节奏蓝调（Smooth R&B groove, soulful vocals, rich harmonies, rhythmic bassline）
- **演唱者**: male（男声）
- **状态**: ✅ 全部成功

### 输出文件
- 歌词: `热梗歌词-全职儿女-2026-05-29.md`
- 配图: `generated-images/配图1_20260529.png` → 复制到 `github-pages/images/cover_全职儿女_20260529.jpg`
- 音频: `music_output/vocal_全职儿女_20260529.mp3` → 复制到 `github-pages/music/vocal_全职儿女_20260529.mp3`
- GitHub Pages:
  - 音频: https://cdn.jsdelivr.net/gh/where20/bgm-audio@377d327/music/vocal_全职儿女_20260529.mp3
  - 图片: https://cdn.jsdelivr.net/gh/where20/bgm-audio@377d327/images/cover_全职儿女_20260529.jpg
- 播放器: https://where20.github.io/bgm-audio/

### 执行步骤摘要
1. ✅ 读取 used_memes.json（已使用26个热梗）
2. ✅ 选择新热梗："全职儿女"（未使用，2026年持续热议的社会现象）
3. ✅ 随机选择节奏风格：B（中速型）
4. ✅ 随机选择音乐流派：R&B（与上次CityPop不同，符合多元化规则）
5. ✅ 生成歌词（带时间戳，中速型B节奏标注）
6. ✅ 生成配图（mmx image generate, image-2.0）
7. ✅ 生成音乐（mmx music generate, R&B男声, music-2.6）
8. ✅ 复制音频到 github-pages/music/，复制封面到 github-pages/images/
9. ✅ 执行 update_github_pages.py 脚本（commit hash: 377d327，CDN URL已更新）
10. ✅ 更新 used_memes.json（添加"全职儿女"，已使用27个）→ git commit + push origin main (0418e12)
11. ✅ 推送飞书卡片（Webhook 响应成功）

### 随机选择详情
- 节奏风格（5选1，排除上次D）：B（中速型）
- 音乐流派（7选1，排除上次CityPop）：R&B
- 演唱者（R&B流派，60% female / 40% male）：male
- 歌词主题（与R&B联动）：情感、治愈、自我成长

### 飞书推送结果
- Webhook 响应: `{"StatusCode":0,"StatusMessage":"success","code":0,"msg":"success"}`
- 卡片标题: "🎵 今日热梗音乐 | 全职儿女"
- 卡片内容: 热梗简介 + R&B节奏蓝调 + 中速型(B)
- 主按钮链接: https://where20.github.io/bgm-audio/

### 热梗解读
"全职儿女"是2026年持续走红的社会现象梗，指年轻人毕业后不就业，全职在家，一边照顾父母、承担部分家务，一边备考公务员/研究生/找工作的状态。

这个词自带矛盾感：
- 表面是"全职照顾父母"的正当理由
- 实际是"我不想上班/找不到工作"的体面说法
- 既是社会压力下的无奈选择，也是对传统"毕业即就业"观念的无声反抗

歌词用 R&B 的温柔力量，把这种尴尬、愧疚、期待、迷茫交织的情绪唱出来——不是批判，是理解；不是励志，是陪伴。

### 技术问题记录
1. **mmx image generate 文件名问题**：--out 参数指定的文件名被忽略，实际保存为 image_001.jpg，需要手动复制到目标路径。
2. **歌词标签格式**：mmx 只支持英文结构标签（[Intro], [Verse], [Chorus], [Bridge], [Outro]），中文标签（[Verse 1], [Hook]）需要转换。
3. **歌词中的制作说明**：括号里的说明文字（如"转调，人声更情感化，背景和声"）会被 mmx 唱出来，需要提前去掉。

### 多元化验证
- 上次流派：CityPop ✅ 本次：R&B（不同）
- 上次节奏：D渐进型 ✅ 本次：B中速型（不同）
- 歌词主题：情感、治愈、自我成长（与R&B流派联动）

---

## 最新完整执行记录（2026-05-26）

### 执行概况
- **执行时间**: 2026-05-26 00:00
- **热梗**: 夯爆了（2026年5月全网Top热梗，源自方言综艺）
- **节奏风格**: D 渐进型（慢起→渐快→高潮→收尾）
- **音乐风格**: CityPop 复古都市风
- **演唱者**: male（男声）
- **状态**: ✅ 全部成功

### 输出文件
- 歌词: `热梗歌词-夯爆了-2026-05-26.md`
- 配图: `generated-images/配图1_20260526.png`
- 音频: `music_output/vocal_夯爆了_20260526.mp3`
- GitHub Pages:
  - 音频: https://cdn.jsdelivr.net/gh/where20/bgm-audio@1ceb3df/music/vocal_夯爆了_20260526.mp3
  - 图片: https://cdn.jsdelivr.net/gh/where20/bgm-audio@1ceb3df/images/cover_夯爆了_20260526.png
- 播放器: https://where20.github.io/bgm-audio/

### 执行步骤摘要
1. ✅ 读取 used_memes.json（23个热梗）
2. ✅ 搜索并选择新热梗："夯爆了"（2026-05-25全网热搜，未使用）
3. ✅ 随机选择节奏风格：D 渐进型
4. ✅ 随机选择音乐流派：CityPop（与上次Folk不同，符合多元化规则）
5. ✅ 生成歌词（带时间戳，渐进型节奏标注）
6. ✅ 生成配图（mmx image generate, image-2.0）
7. ✅ 生成音乐（mmx music generate, CityPop男声, music-2.6）
8. ✅ 复制文件到github-pages → git commit (c3dd722) → push 成功
9. ✅ update_github_pages.py (commit: 1ceb3df, CDN URL已更新)
10. ✅ used_memes.json更新 (commit: 2dc1a05 main分支)
11. ✅ 飞书卡片推送 (StatusCode: 0)

### 🔧 歌词同步修复（2026-05-26 00:15）
- **问题**: 音频158.8s vs 时间戳225s，差66s，歌词完全不对应
- **根因**: AI音乐自动编曲速度比预估快，手动时间戳不准确
- **修复**: 等比缩放(scale=0.7058)，推送gh-pages (9240291)
- **教训**: 后续生成应考虑实际音频时长，可考虑先等音频生成后再写时间戳

### 多元化验证
- 上次流派：Folk ✅ 本次：CityPop（不同）
- 上次节奏：慢热型(A) ✅ 本次：渐进型(D)（不同）

---

## 最新完整执行记录（2026-05-24）

### 执行概况
- **执行时间**: 2026-05-24 07:00
- **热梗**: 痛文化（2026年小红书Top10热梗）
- **节奏风格**: A 慢热型（慢起→民谣叙事→情感升华）
- **音乐风格**: Folk 民谣
- **演唱者**: female（女声）
- **状态**: ✅ 基本成功（git push used_memes.json 超时）

### 输出文件
- 歌词: `热梗歌词-痛文化-2026-05-24.md`
- 配图: `generated-images/配图1_20260524.png`
- 音频: `music_output/vocal_痛文化_20260524.mp3`
- GitHub Pages:
  - 音频: https://cdn.jsdelivr.net/gh/where20/bgm-audio@a94d917/music/vocal_痛文化_20260524.mp3
  - 图片: https://cdn.jsdelivr.net/gh/where20/bgm-audio@a94d917/music/配图1_20260524.png
- 播放器: https://where20.github.io/bgm-audio/

### 执行步骤摘要
1. ✅ 读取 used_memes.json（已使用21个热梗）
2. ✅ 搜索并选择新热梗："痛文化"（未使用，2026小红书Top10）
3. ✅ 随机选择节奏风格：A 慢热型
4. ✅ 随机选择音乐流派：Folk 民谣（与上次Electronic不同，符合多元化规则）
5. ✅ 生成歌词（带时间戳，慢热型节奏标注）
6. ✅ 生成配图（mmx image generate, image-2.0）
7. ✅ 生成音乐（mmx music generate, Folk女声, music-2.6）
8. ✅ 复制音频+封面到 github-pages/music/ → git commit (a94d917) → push 成功
9. ✅ 手动更新 music.json（Python脚本插入playlist[0]）→ commit (b474dc4) → push 成功
10. ⚠️ 更新 used_memes.json（本地commit成功，但 git push origin main 多次HTTP 408超时）
11. ✅ 推送飞书卡片（成功）

### 飞书推送结果
- Webhook 响应: `{"StatusCode":0,"StatusMessage":"success","code":0,"msg":"success"}`
- 卡片标题: "🎵 热梗歌词今日更新 | 2026-05-24"

### 热梗解读
"痛文化"是2026年小红书Top10热梗，指年轻人用幽默/表情包/段子包装痛苦和负面情绪的文化现象。不是真的想痛，是痛到一定程度反而能笑了。用最轻松的语气说最痛的事情。

### 多元化验证
- 上次流派：Electronic ✅ 本次：Folk（不同）
- 上次节奏：波浪型 ✅ 本次：慢热型（不同）

---

## 最新完整执行记录（2026-05-23）

### 执行概况
- **执行时间**: 2026-05-23 07:00
- **热梗**: 崩老头（2026年走红网络黑话，源自东北方言）
- **节奏风格**: 波浪型（快→慢→快→慢循环）
- **音乐风格**: Electronic 电子
- **演唱者**: female（女声）
- **状态**: ✅ 成功完成

### 输出文件
- 歌词: `热梗歌词-崩老头-2026-05-23.md`
- 配图: `generated-images/配图1_20260523.png`
- 音频: `music_output/vocal_崩老头_20260523.mp3`
- GitHub Pages:
  - 音频: https://cdn.jsdelivr.net/gh/where20/bgm-audio@e39a7bb/music/vocal_崩老头_20260523.mp3
  - 图片: https://cdn.jsdelivr.net/gh/where20/bgm-audio@e39a7bb/images/cover_崩老头_20260523.png
- 播放器: https://where20.github.io/bgm-audio/

### 执行步骤摘要
1. ✅ 读取 used_memes.json（已使用21个热梗）
2. ✅ 搜索并选择新热梗："崩老头"（未使用，2026年5月新梗）
3. ✅ 随机选择节奏风格：波浪型（风格C）
4. ✅ 随机选择音乐流派：Electronic 电子（与上次Pop不同，符合多元化规则）
5. ✅ 生成歌词（带时间戳，波浪型节奏标注）
6. ✅ 生成配图（mmx image generate, image-2.0）
7. ✅ 生成音乐（mmx music generate, Electronic风格, 女声, music-2.6）
8. ✅ 复制音频到 github-pages/music/
9. ✅ 执行 update_github_pages.py 脚本（commit hash: e39a7bb）
10. ✅ 更新 used_memes.json（添加"崩老头"，已使用22个）
11. ✅ 推送飞书卡片（成功）

### 飞书推送结果
- Webhook 响应: `{'StatusCode': 0, 'StatusMessage': 'success', 'code': 0, 'msg': 'success'}`
- 卡片标题: "🎵 今日热梗音乐 | 崩老头"

### 热梗解读
"崩老头"是2026年走红的网络黑话，源自东北方言。"崩"=哄骗、软薅、套取；"老头"≠真老人，特指30-50岁、有稳定收入、情感空虚、背负房贷车贷压力的80/90后中年男性。用幽默外壳包裹沉重的社会议题。

### 多元化改造验证
- 上次流派：Pop ✅ 本次：Electronic（不同）
- 上次节奏：中速型 ✅ 本次：波浪型（不同）
- 歌词主题：社会观察 + 抽象感受 + 能量释放（与Electronic流派联动）

---

## 历史执行记录

### 2026-05-22
- 热梗: 爱你老己（2026年爆火正能量梗，倡导自我关怀）
- 风格: 中速型（风格B）
- 文件: vocal_爱你老己_20260522.mp3
- CDN: @28d0794

---

## 历史执行记录

## 历史执行记录

### 2026-05-19
- 热梗: 如何呢又能怎（源自单依纯改编歌词，2025十大流行语）
- 风格: 波浪型（快→慢→快→慢循环）
- 文件: vocal_如何呢又能怎_20260519.mp3
- CDN: @4e60fe3

### 2026-05-18
- 热梗: 反精致
- 风格: 流行抒情型（中慢速，情感饱满，旋律性强）
- 文件: vocal_反精致_20260518.mp3
- CDN: @5748f5b

### 2026-05-17
- 热梗: 45度人生
- 风格: 流行抒情型
- 文件: vocal_45度人生_20260517.mp3
- CDN: @070adfd

（更多历史记录请查看 used_memes.json）