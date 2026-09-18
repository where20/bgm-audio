# MV 分镜提示词包 · 电子小猪（ComfyUI 自动版）
# 歌曲：电子小猪_20260918.mp3 (96BPM Electronic)
# 节奏：D / 性别：female
# 生成工具：scripts/generate_mv_storyboard.py
# 生成日期：2026-09-18
# 协议：local-drama-prompts v1（克隆基线 + 4 槽位）

---

## 0. 克隆基线说明
- **歌曲**: `music_output/vocal_电子小猪_20260918.mp3`
- **总时长**: 预估 185.0s
- **画幅**: 9:16 竖屏 1080×1920
- **镜数**: **34 镜**（每镜 ≤5s）
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

## 3. 逐镜表（34 镜，每镜 ≤5s）

### Shot 01 ｜ 0.0s - 5.0s ｜ Intro
- **景别/运动**: Intro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC1 Changsha small rental room, morning dim light, alarm clock, desk stacked with exam prep books, dusty window, gray cyan tone], Intro scene`
- **Video motion prompt**: `slow rack focus, soft morning light creeps in, 4 seconds`
- **台词**: 「[慢节奏 电子氛围起]」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 02 ｜ 8.5s - 13.2s ｜ Intro
- **景别/运动**: Intro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC1 Changsha small rental room, morning dim light, alarm clock, desk stacked with exam prep books, dusty window, gray cyan tone], Intro scene`
- **Video motion prompt**: `slow rack focus, soft morning light creeps in, 4 seconds`
- **台词**: 「屏幕亮 油花跳 我在云端吃夜宵」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 03 ｜ 13.2s - 18.0s ｜ Intro
- **景别/运动**: Intro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC1 Changsha small rental room, morning dim light, alarm clock, desk stacked with exam prep books, dusty window, gray cyan tone], Intro scene`
- **Video motion prompt**: `slow rack focus, soft morning light creeps in, 4 seconds`
- **台词**: 「钱包说 别下单 我就刷刷也很饱」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 04 ｜ 18.0s - 23.0s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「煎饼卷大葱 隔着屏幕闻香味」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 05 ｜ 23.4s - 28.4s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「麻辣小龙虾 弹幕里我干三碗」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 06 ｜ 28.8s - 33.8s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「减肥第一天 计划写到第七页」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 07 ｜ 34.2s - 39.2s ｜ Verse 1
- **景别/运动**: Verse 1 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC3 view through moving train window, countryside scenery, blue gray gradient tone, travel reflection], Verse 1 scene`
- **Video motion prompt**: `fixed window view, scenery rushes past, time-lapse, 5 seconds`
- **台词**: 「体重没下降 我的快乐在直播」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 08 ｜ 39.6s - 44.6s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「手指一划 外卖到了 可是我没下单」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 09 ｜ 45.0s - 50.0s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「钱包捂住 心在呼喊 让我再看看」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 10 ｜ 50.4s - 55.4s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「我是电子小猪 屏幕就是猪圈」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 11 ｜ 55.8s - 60.8s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「看吃播长大 省钱是天赋」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 12 ｜ 61.2s - 66.2s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「云干饭高手 体重不掉队」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 13 ｜ 66.6s - 71.6s ｜ Pre Chorus
- **景别/运动**: Pre Chorus 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SCREEN WeChat chat interface or Moments screenshot, warm cream background, blue WeChat UI, halftone texture], Pre Chorus scene`
- **Video motion prompt**: `over-shoulder close-up, phone screen lights up, 4 seconds`
- **台词**: 「喂饱眼睛 喂瘦钱包 喂饱emo」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 14 ｜ 73.2s - 78.2s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「火锅煮海底 镜头里翻滚着毛肚」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 15 ｜ 78.6s - 83.6s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「烤串滋滋响 弹幕刷过一万遍」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 16 ｜ 84.0s - 89.0s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「朋友约出门 我说下次吧下次」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 17 ｜ 89.4s - 94.4s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「窝在被窝里 美食博主才懂我」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 18 ｜ 94.8s - 99.8s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「手指一划 外卖到了 我又看了三遍」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 19 ｜ 100.2s - 105.2s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「钱包鼓掌 体重鼓掌 节俭人设」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 20 ｜ 105.6s - 110.6s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「我是电子小猪 屏幕就是猪圈」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 21 ｜ 111.0s - 116.0s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「看吃播长大 省钱是天赋」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 22 ｜ 116.4s - 121.4s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「云干饭高手 体重不掉队」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 23 ｜ 121.8s - 126.8s ｜ Verse 2
- **景别/运动**: Verse 2 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC4 Cairo street or pyramid plateau, golden hour light, warm dusty atmosphere, vendor stalls], Verse 2 scene`
- **Video motion prompt**: `tracking shot, character walking, handheld micro-shake, 5 seconds`
- **台词**: 「喂饱眼睛 喂瘦钱包 喂饱emo」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 24 ｜ 127.2s - 132.2s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「妈妈问我在吃啥 我说在吃电子餐」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 25 ｜ 132.6s - 137.6s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「她说你在养啥猪 我说养一只快乐猪」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 26 ｜ 138.0s - 143.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「这只猪不用喂 这只猪不用睡」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 27 ｜ 143.4s - 148.4s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「只用WiFi和电 就能让它笑眯眯」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 28 ｜ 148.8s - 153.8s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「我是电子小猪 屏幕就是猪圈」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 29 ｜ 154.2s - 159.2s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「看吃播长大 省钱是天赋」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 30 ｜ 159.6s - 164.6s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「云干饭高手 体重不掉队」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 31 ｜ 165.0s - 170.0s ｜ Bridge
- **景别/运动**: Bridge 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 Changsha airport arrival hall, warm orange afternoon light, mom figure waiting, backlit silhouette], Bridge scene`
- **Video motion prompt**: `slow push-in, character breathing, 5 seconds`
- **台词**: 「喂饱眼睛 喂瘦钱包 喂饱emo」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 32 ｜ 170.4s - 175.4s ｜ Outro
- **景别/运动**: Outro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 warm apartment or home doorway, golden hour interior light, family reunion moment], Outro scene`
- **Video motion prompt**: `wide shot pulling back, two silhouettes embrace, 3 seconds`
- **台词**: 「钱包鼓了吗 没有」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 33 ｜ 175.8s - 180.0s ｜ Outro
- **景别/运动**: Outro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 warm apartment or home doorway, golden hour interior light, family reunion moment], Outro scene`
- **Video motion prompt**: `wide shot pulling back, two silhouettes embrace, 3 seconds`
- **台词**: 「人快乐吗 快乐」
- **黄卡**: 「无」
- **配音**: BGM 同步

### Shot 34 ｜ 180.0s - 185.0s ｜ Outro
- **景别/运动**: Outro 段落自动镜头
- **Image prompt**: `1980s retro travel film aesthetic, Kodak Portra 160 film stock, heavy 35mm film grain, halftone print dots, scan line offsets, slightly desaturated warm golden tones, vintage anamorphic lens flares, nostalgic documentary mood, vertical 9:16 framing, the same 24-year-old Chinese young adult from the reference image, mature adult proportions, short black hair, lean build, tired but warm eyes, weathered backpacker outfit, [OUTFIT cotton linen shirt + canvas backpack], [SCENE SC6 warm apartment or home doorway, golden hour interior light, family reunion moment], Outro scene`
- **Video motion prompt**: `wide shot pulling back, two silhouettes embrace, 3 seconds`
- **台词**: 「这就是 互联网 养猪人」
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
- 本分镜包: `mv_storyboards/mv_电子小猪_20260918_comfyui.md`
- 歌词时间戳: `lyrics/lyrics_电子小猪_20260918.txt`
- 歌词纯文本: `lyrics/lyrics_电子小猪_20260918_mcode.txt`
- Master Audio: `music_output/vocal_电子小猪_20260918.mp3`

## 9. 验收 checklist
- [ ] 每镜 ≤5s
- [ ] 4 槽位全部标注
- [ ] 妈妈只以文字+语音条出现
- [ ] 风格前缀每镜一致
