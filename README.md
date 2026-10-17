# 🎵 热梗歌词音乐播放器

每天自动生成的热梗歌曲播放器，支持歌词同步滚动。

**线上地址：https://music.220616.xyz**

---

## 架构：Pages 只发 4 个文件，媒体全走 jsDelivr

这是本项目最反直觉、也最重要的一点：

```
浏览器 ──fetch──> https://music.220616.xyz/music.json      (GitHub Pages)
                              │
浏览器 ──直接请求────────────> cdn.jsdelivr.net/gh/where20/bgm-audio@gh-pages/...
       (音频 mp3 / 封面 png)                                  (jsDelivr 读 git 仓库)
```

`index.html` 里的 `resolveAudioUrl()` / `resolveImageUrl()` 会在**浏览器端**
把 `music/xxx.mp3` 这类相对路径拼成 jsDelivr 地址，所以：

- **GitHub Pages 从不传输媒体**，只发 `index.html` + `music.json` + `CNAME` + `.nojekyll`（约 94 KB）
- 音频/封面由 jsDelivr 直接从 git 仓库读取并缓存
- `index.html` 完全自包含：无外链字体、无 favicon、无 data URI

因此 `deploy.yml` 里**绝不能**再写 `path: '.'` —— 那样会把整仓约 700 MB
（`music/` 475 MB + `images/` 116 MB + `videos/` 47 MB + 创作素材 + 工具脚本）
全部发布，既拖垮部署，又把内部文件暴露到公网。

---

## 仓库结构

### 站点文件（会被部署）

| 路径 | 说明 |
|---|---|
| `index.html` | 播放器主页面，完全自包含 |
| `music.json` | 播放列表数据，`playlist` 保留最近 30 首 |
| `CNAME` | 自定义域名 `music.220616.xyz` |
| `.nojekyll` | 禁用 Jekyll 构建 |
| `.github/workflows/deploy.yml` | 部署：组装 `_site/` 后发布 |

### 媒体仓库（只经 jsDelivr，不经 Pages）

| 路径 | 说明 |
|---|---|
| `images/` | 封面图 `cover_{歌名}_{日期}.{ext}` |
| `music/` | 音频 `vocal_{歌名}_{日期}.mp3` 等 |

### 创作素材与工具（不部署）

| 路径 | 说明 |
|---|---|
| `generated-images/` | 配图源文件 —— **自动化的输入参数路径，不要改名或移动** |
| `music_output/` | 生成的音乐中间产物 |
| `videos/` | MV 输出 |
| `mv_storyboards/` | MV 分镜稿 |
| `热梗歌词-*.md` | 歌词稿件 |
| `lyrics_*.txt` / `*.lrc` | 歌词文件 —— 自动化用 `@文件路径` 传入，**不要移动** |
| `update_github_pages.py` | 自动化主脚本（见下） |
| `fix_lyrics.py` / `fix_lyrics_v2.py` | 歌词清洗工具 |
| `scratchpad.md`、`used_memes.json` | 过程记录 |

### 不跟踪

`.workbuddy/`（工具内部记忆与 base64 草稿）、`.DS_Store`、`__pycache__/`、
`/github-pages`（自引用 symlink，会破坏 Jekyll 构建）、根目录杂物。

---

## 自动化（macOS 侧）

`update_github_pages.py` 由 WorkBuddy 每日任务调用，工作目录
`/Users/xiaoan/WorkBuddy/2026-05-05-task-3`：

```bash
python3 update_github_pages.py <热梗> <日期> <风格> <音频> <图片路径> <歌词>
# 歌词支持 @ 开头表示从文件读取，例如 @lyrics/xxx.txt
```

流程：

1. `music.json` 写入新条目（去重后插到队首，只保留最近 30 首）
2. 配图复制到 `images/cover_{歌名}_{日期}.png`
3. `git add .` → commit → **force push 到 `gh-pages` 分支**
4. 把相对路径改写成带 commit hash 的 jsDelivr CDN URL，`amend` 后再次 force push

### ⚠️ 硬编码路径契约

脚本硬编码依赖仓根的 `music.json` / `images/` / `music/` 三个路径，
且自动化任务配置里写死了 `generated-images/` 与歌词文件的路径。

**在 Windows 上单方面调整仓库布局，会让下一个自动化周期直接失败。**
要重组目录必须先改 macOS 侧的自动化任务配置。

---

## ⚠️ 跨平台文件名：歌名不能带 `:`

Windows 文件名非法字符 `< > : " / \ | ? *` 在 macOS 上全部合法，
但同步到 Windows 仓库后，git 在 checkout 阶段会拒绝落盘：

```
error: invalid path 'images/cover_牛:赶紧开学吧_20260904.png'
Merge with strategy ort failed.
```

`update_github_pages.py` 的 `safe_filename()` 已把这些字符替换为 `-`。
**注意它只清洗文件名**：`music.json` 里的 `id` / `meme` 保持原样，站点展示不变。

Windows 上遇到历史遗留的冒号文件时，临时绕过：

```bash
git -c core.protectNTFS=false merge origin/gh-pages
git config core.protectNTFS false    # 固化，否则下次 merge 又炸
```

此时 git 会把内容写成挂在 `images\cover_牛` 上的 NTFS 备用数据流，
`git status` 会常驻一个 0 字节的 `?? images/cover_牛`。**git 树里路径完全正确**，
jsDelivr 与 Pages 不受影响；别 `git add` 它（会被再次拒绝）。

---

## 本地开发

```bash
git clone https://github.com/where20/bgm-audio.git
cd bgm-audio
python3 -m http.server 8080   # 直接打开 http://localhost:8080
```

改了 `index.html` 或 `music.json` 后 push 到 `main`，
GitHub Actions 会自动组装并部署站点产物。

---

## 快捷键

| 按键 | 功能 |
|---|---|
| 空格 | 播放 / 暂停 |
| ← → | 后退 / 前进 5 秒 |
| `[` `]` | 歌词提前 / 延后 0.5 秒（±5 秒，存 localStorage） |

---

Made with ❤️ by WorkBuddy
