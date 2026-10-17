# 🎵 热梗音乐播放器

基于 GitHub Pages 的热梗歌词音乐播放器，支持歌词同步滚动！

## ✨ 功能特点

- 🎤 **歌词同步滚动** - 自动解析 [mm:ss.xx] 时间戳，高亮当前歌词
- ⚡ **速度控制** - 支持 0.5x 到 2x 播放速度
- 📜 **历史记录** - 查看所有历史生成的音乐
- 🎨 **精美界面** - 响应式设计，手机电脑都能用
- ⌨️ **键盘快捷键** - 空格播放/暂停，左右键快进快退

## 🚀 部署说明

### 方式一：推送到现有仓库（推荐）

```bash
# 克隆你的bgm-audio仓库
git clone https://github.com/where20/bgm-audio.git
cd bgm-audio

# 创建gh-pages分支
git checkout -b gh-pages

# 复制所有文件到这个目录
cp /Users/xiaoan/WorkBuddy/2026-05-05-task-3/github-pages/* .

# 推送
git add .
git commit -m "feat: 添加歌词同步播放器"
git push origin gh-pages
```

### 方式二：创建新仓库

1. 在 GitHub 创建新仓库 `bgm-player`
2. 克隆后复制文件
3. 在仓库 Settings > Pages 中选择 `gh-pages` 分支
4. 等待部署完成

## 🌐 访问地址

部署成功后访问：`https://where20.github.io/bgm-player/`

或指定某首历史音乐：
`https://where20.github.io/bgm-player/?id=yang_longxia_20260505`

## 📡 API 更新机制

播放器从 `music.json` 加载音乐数据。每次生成新音乐后，需要更新这个文件：

```json
{
  "latest": {
    "id": "新热梗_id",
    "meme": "热梗名称",
    "date": "2026-05-06",
    "style": "节奏风格",
    "audio": "音频CDN链接",
    "image": "封面图CDN链接",
    "lyrics": "[0.00]歌词内容\n[5.00]下一句歌词"
  },
  "history": [...]
}
```

## 🔧 自动化集成

自动化任务（每天09:00）会：
1. 生成新的热梗音乐
2. 上传到 GitHub CDN
3. 更新 `music.json` 的 latest 和 history
4. 自动推送到 gh-pages 分支

## 📁 文件结构

```
├── index.html          # 播放器主页面
├── music.json          # 音乐数据（latest + history）
├── .github/
│   └── workflows/
│       └── deploy.yml  # GitHub Actions 部署配置
└── README.md
```

## 🎹 键盘快捷键

| 按键 | 功能 |
|------|------|
| 空格 | 播放/暂停 |
| ← | 后退5秒 |
| → | 前进5秒 |

## 💡 歌词格式

歌词文件支持 [mm:ss.xx] 时间戳格式：

```
[0.00]养龙虾啊养龙虾
[4.50]OpenClaw来帮忙
[9.00]AI智能体帮你养
```

---

Made with ❤️ by WorkBuddy
