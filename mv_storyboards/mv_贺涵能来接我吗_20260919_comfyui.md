# MV 分镜提示词包 · 贺涵能来接我吗（ComfyUI 自动版）
# 歌曲：贺涵能来接我吗_20260919.mp3 (96BPM R&B)
# 节奏：C / 性别：male
# 生成工具：scripts/generate_mv_storyboard.py
# 生成日期：2026-09-19
# 协议：local-drama-prompts v1（克隆基线 + 4 槽位）

---

## 0. 克隆基线说明
- **歌曲**: `music_output/vocal_贺涵能来接我吗_20260919.mp3`
- **总时长**: 预估 183.2s
- **画幅**: 9:16 竖屏 1080×1920
- **镜数**: **33 镜**（每镜 ≤5s）
- **本包克隆**: 段落切分、时间码、机位/运动、色调、硬切节奏
- **槽位**: `[CHAR]` `[OUTFIT]` `[SCENE]` `[LINE]`

### 安全降级
- 妈妈不出现真人正脸（仅文字 + 语音条）
- 儿子年龄锚点：24 岁成年

## 1. 全局风格前缀 + 负向词
### 风格前缀（每镜逐字复用）
```
1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing
```

### 人物锚点
```
the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit
```

### 负向词
```
loli, child, kid, underage, minor, different face, face swap drift, plastic skin, glossy AI beauty filter, deformed hands, extra fingers, watermark, logo, text overlay, modern smartphone screen glare, neon cyberpunk, anime, cartoon
```

## 2. 槽位表
| 槽位 | 默认值 | 可换示例 |
|---|---|---|
| `[CHAR]` | 24 岁中国男生 IPAdapter 锁脸 | 30 岁熟女 / 自带参考图 |
| `[OUTFIT]` | 棉麻背包客装 | denim jacket / linen kurta |
| `[SCENE]` | 按段落自动选 | 改英文场景描述 |

## 3. 逐镜表（33 镜，每镜 ≤5s）

### Shot 01 ｜ 0.0s - 5.0s ｜ Intro
- **景别/运动**: Intro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC1 Changsha small rental room, morning dim light, alarm clock, desk stacked with exam prep books, dusty window, gray cyan tone], Intro scene`
- **Video motion prompt**: `slow rack focus, soft morning light creeps in, 4 seconds`
- **台词**: 「[慢节奏 R&B 钢琴起]」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 02 ｜ 8.5s - 13.2s ｜ Intro
- **景别/运动**: Intro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC1 Changsha small rental room, morning dim light, alarm clock, desk stacked with exam prep books, dusty window, gray cyan tone], Intro scene`
- **Video motion prompt**: `slow rack focus, soft morning light creeps in, 4 seconds`
- **台词**: 「深夜班雨 打车排长龙」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 03 ｜ 13.2s - 18.0s ｜ Intro
- **景别/运动**: Intro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC1 Changsha small rental room, morning dim light, alarm clock, desk stacked with exam prep books, dusty window, gray cyan tone], Intro scene`
- **Video motion prompt**: `slow rack focus, soft morning light creeps in, 4 seconds`
- **台词**: 「我举着伞 走路回家」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 04 ｜ 18.0s - 23.0s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「下班高峰 风把人吹翻」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 05 ｜ 23.4s - 28.4s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「洞洞鞋在地上 吱吱吱吱乱喊」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 06 ｜ 28.8s - 33.8s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「外卖小哥都比我走得快」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 07 ｜ 34.2s - 39.2s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「只剩我在原地 假装不在意」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 08 ｜ 39.6s - 43.2s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「全世界都在堵」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 09 ｜ 43.2s - 48.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「只有贺涵能无缝切入」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 10 ｜ 48.0s - 53.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「贺涵 贺涵 你能来接我吗」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 11 ｜ 54.0s - 59.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「我的鞋在叫 钱包在哭」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 12 ｜ 60.0s - 65.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「贺涵 贺涵 你能来接我吗」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 13 ｜ 66.0s - 71.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「风雨都还好 心寒是真的」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 14 ｜ 72.0s - 77.0s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「贺涵不到 贺涵永远不到」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 15 ｜ 77.4s - 82.4s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「现实的贺涵都在加班跑道」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 16 ｜ 82.8s - 87.8s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「摄像头看得清 没人在拍我」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 17 ｜ 88.2s - 93.2s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「把伞扔给风 把心扔给酒」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 18 ｜ 94.2s - 98.4s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「全世界还在堵」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 19 ｜ 98.4s - 103.2s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「只有贺涵 没接到任务」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 20 ｜ 103.2s - 108.2s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「贺涵 贺涵 你能来接我吗」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 21 ｜ 109.2s - 114.2s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「我的鞋不叫了 心还在哭」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 22 ｜ 115.2s - 120.2s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「贺涵 贺涵 你能来接我吗」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 23 ｜ 121.2s - 126.2s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「雨停了你还没到」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 24 ｜ 127.2s - 132.2s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「最后还是自己走回家」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 25 ｜ 132.6s - 137.6s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「只是还想被接那么一次」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 26 ｜ 138.0s - 143.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「手机里没消息 现实里没贺涵」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 27 ｜ 143.4s - 148.4s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「只有雨的节拍 还在零落」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 28 ｜ 148.8s - 153.8s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「贺涵 贺涵 还能接我吗」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 29 ｜ 154.8s - 159.8s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「你的羊皮鞋 别怕被水泡」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 30 ｜ 160.8s - 165.8s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「贺涵 贺涵 还能接我吗」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 31 ｜ 166.8s - 171.8s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「下次记得带伞」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 32 ｜ 172.8s - 177.8s ｜ Outro
- **景别/运动**: Outro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 warm apartment or home doorway, golden hour interior light, family reunion moment], Outro scene`
- **Video motion prompt**: `wide shot pulling back, two silhouettes embrace, 3 seconds`
- **台词**: 「贺涵」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 33 ｜ 178.2s - 183.2s ｜ Outro
- **景别/运动**: Outro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 warm apartment or home doorway, golden hour interior light, family reunion moment], Outro scene`
- **Video motion prompt**: `wide shot pulling back, two silhouettes embrace, 3 seconds`
- **台词**: 「记得 带伞」
- **黄卡**: 「无」
- **配音**: BGM 同步

## 4. 字幕与音频规范
- 字幕位置：底部居中，黄字+黑描边
- BGM 一轨锁定原歌曲

## 5. 本地构建工作流
1. z_image 出 40-80 张关键帧 → assets/keyframes/
2. 首帧接 MiniMax H3 节点 → output/shot_N.mp4
3. 剪映/Resolve 拼接 + 字幕 + 黄卡

## 6. 拆段表
| 原镜 | 拆分 | 时长 | 内容 |
|---|---|---|---|
| （如有 >5s 镜） | a/b | 3-5s + 3-5s | 尾帧接首帧 |

## 7. 高光引流版（约 45s）
复用前 9 镜 + 后 3 镜 + 黑屏金句

## 8. 交付清单
- 本分镜包: `mv_storyboards/mv_贺涵能来接我吗_20260919_comfyui.md`
- 歌词时间戳: `lyrics/lyrics_贺涵能来接我吗_20260919.txt`
- 歌词纯文本: `lyrics/lyrics_贺涵能来接我吗_20260919_mcode.txt`
- Master Audio: `music_output/vocal_贺涵能来接我吗_20260919.mp3`

## 9. 验收 checklist
- [ ] 每镜 ≤5s
- [ ] 4 槽位全部标注
- [ ] 妈妈只以文字+语音条出现
- [ ] 风格前缀每镜一致
