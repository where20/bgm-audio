# MV 分镜提示词包 · 永远不要用力走向任何人（ComfyUI 自动版）
# 歌曲：永远不要用力走向任何人_20260921.mp3 (96BPM Electronic)
# 节奏：D / 性别：female
# 生成工具：scripts/generate_mv_storyboard.py
# 生成日期：2026-09-21
# 协议：local-drama-prompts v1（克隆基线 + 4 槽位）

---

## 0. 克隆基线说明
- **歌曲**: `music_output/vocal_永远不要用力走向任何人_20260921.mp3`
- **总时长**: 预估 305.0s
- **画幅**: 9:16 竖屏 1080×1920
- **镜数**: **32 镜**（每镜 ≤5s）
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

## 3. 逐镜表（32 镜，每镜 ≤5s）

### Shot 01 ｜ 5.0s - 10.0s ｜ Intro
- **景别/运动**: Intro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC1 Changsha small rental room, morning dim light, alarm clock, desk stacked with exam prep books, dusty window, gray cyan tone], Intro scene`
- **Video motion prompt**: `slow rack focus, soft morning light creeps in, 4 seconds`
- **台词**: 「霓虹灯 模糊了一整条街」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 02 ｜ 10.0s - 15.0s ｜ Intro
- **景别/运动**: Intro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC1 Changsha small rental room, morning dim light, alarm clock, desk stacked with exam prep books, dusty window, gray cyan tone], Intro scene`
- **Video motion prompt**: `slow rack focus, soft morning light creeps in, 4 seconds`
- **台词**: 「我也曾用力握紧 谁的手」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 03 ｜ 20.0s - 25.0s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「人群走过 没人停下来」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 04 ｜ 30.0s - 35.0s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「我用尽全力 也只是路过」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 05 ｜ 40.0s - 45.0s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「手机亮着 没一条新消息」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 06 ｜ 50.0s - 55.0s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「街角的便利店 收银员不看我」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 07 ｜ 60.0s - 65.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「我们都用尽了力气」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 08 ｜ 65.0s - 70.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「却换来一句算了吧」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 09 ｜ 70.0s - 75.0s ｜ Chorus
- **景别/运动**: Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 vast Sahara desert, golden orange sky, sun on horizon, warm cinematic light, lens flare], Chorus scene`
- **Video motion prompt**: `wide shot slow dolly-in, sun on horizon, 5 seconds`
- **台词**: 「永远不要用力走向任何人」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 10 ｜ 80.0s - 85.0s ｜ Chorus
- **景别/运动**: Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 vast Sahara desert, golden orange sky, sun on horizon, warm cinematic light, lens flare], Chorus scene`
- **Video motion prompt**: `wide shot slow dolly-in, sun on horizon, 5 seconds`
- **台词**: 「真正同频的人 会自己走来」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 11 ｜ 90.0s - 95.0s ｜ Chorus
- **景别/运动**: Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 vast Sahara desert, golden orange sky, sun on horizon, warm cinematic light, lens flare], Chorus scene`
- **Video motion prompt**: `wide shot slow dolly-in, sun on horizon, 5 seconds`
- **台词**: 「握不住的沙 就让它随风」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 12 ｜ 100.0s - 105.0s ｜ Chorus
- **景别/运动**: Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 vast Sahara desert, golden orange sky, sun on horizon, warm cinematic light, lens flare], Chorus scene`
- **Video motion prompt**: `wide shot slow dolly-in, sun on horizon, 5 seconds`
- **台词**: 「不必用力 缘分自会安排」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 13 ｜ 110.0s - 115.0s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「咖啡凉了 还坐着发呆」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 14 ｜ 120.0s - 125.0s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「回信写着 又全部删掉」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 15 ｜ 130.0s - 135.0s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「朋友圈里 谁的喜帖在传」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 16 ｜ 140.0s - 145.0s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「我点个赞 也算一种参与」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 17 ｜ 150.0s - 155.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「我们都不愿意将就」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 18 ｜ 155.0s - 160.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「却又在等那个刚好」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 19 ｜ 160.0s - 165.0s ｜ Chorus
- **景别/运动**: Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 vast Sahara desert, golden orange sky, sun on horizon, warm cinematic light, lens flare], Chorus scene`
- **Video motion prompt**: `wide shot slow dolly-in, sun on horizon, 5 seconds`
- **台词**: 「永远不要用力走向任何人」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 20 ｜ 170.0s - 175.0s ｜ Chorus
- **景别/运动**: Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 vast Sahara desert, golden orange sky, sun on horizon, warm cinematic light, lens flare], Chorus scene`
- **Video motion prompt**: `wide shot slow dolly-in, sun on horizon, 5 seconds`
- **台词**: 「真正同频的人 会自己走来」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 21 ｜ 180.0s - 185.0s ｜ Chorus
- **景别/运动**: Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 vast Sahara desert, golden orange sky, sun on horizon, warm cinematic light, lens flare], Chorus scene`
- **Video motion prompt**: `wide shot slow dolly-in, sun on horizon, 5 seconds`
- **台词**: 「握不住的沙 就让它随风」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 22 ｜ 190.0s - 195.0s ｜ Chorus
- **景别/运动**: Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 vast Sahara desert, golden orange sky, sun on horizon, warm cinematic light, lens flare], Chorus scene`
- **Video motion prompt**: `wide shot slow dolly-in, sun on horizon, 5 seconds`
- **台词**: 「不必用力 缘分自会安排」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 23 ｜ 200.0s - 205.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「用力喊出的话 对方听不见」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 24 ｜ 210.0s - 215.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「用力靠近的人 我先退了」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 25 ｜ 220.0s - 225.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「用力维系的一切 最后散了」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 26 ｜ 230.0s - 235.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「用力爱过的自己 我先接住」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 27 ｜ 240.0s - 245.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「永远不要用力走向任何人」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 28 ｜ 250.0s - 255.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「真正同频的人 会自己走来」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 29 ｜ 260.0s - 265.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「握不住的沙 就让它随风」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 30 ｜ 270.0s - 275.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「不必用力 缘分自会安排」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 31 ｜ 290.0s - 295.0s ｜ Outro
- **景别/运动**: Outro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 warm apartment or home doorway, golden hour interior light, family reunion moment], Outro scene`
- **Video motion prompt**: `wide shot pulling back, two silhouettes embrace, 3 seconds`
- **台词**: 「轻轻走 慢慢来」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 32 ｜ 300.0s - 305.0s ｜ Outro
- **景别/运动**: Outro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 warm apartment or home doorway, golden hour interior light, family reunion moment], Outro scene`
- **Video motion prompt**: `wide shot pulling back, two silhouettes embrace, 3 seconds`
- **台词**: 「不用力 一切都会来」
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
- 本分镜包: `mv_storyboards/mv_永远不要用力走向任何人_20260921_comfyui.md`
- 歌词时间戳: `lyrics/lyrics_永远不要用力走向任何人_20260921.txt`
- 歌词纯文本: `lyrics/lyrics_永远不要用力走向任何人_20260921_mcode.txt`
- Master Audio: `music_output/vocal_永远不要用力走向任何人_20260921.mp3`

## 9. 验收 checklist
- [ ] 每镜 ≤5s
- [ ] 4 槽位全部标注
- [ ] 妈妈只以文字+语音条出现
- [ ] 风格前缀每镜一致
