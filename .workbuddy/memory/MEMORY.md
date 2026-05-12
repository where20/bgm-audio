# MEMORY.md - 长期记忆

## 项目配置
- GitHub仓库: where20/bgm-audio (gh-pages分支)
- GitHub Pages地址: https://where20.github.io/bgm-audio/
- 播放器页面: player.html, 数据文件: music.json
- git push代理: `https_proxy=http://127.0.0.1:7897 git push origin gh-pages`（SSH key未配置，直接HTTPS超时）
- jsDelivr CDN格式: `https://cdn.jsdelivr.net/gh/where20/bgm-audio@{commit_hash}/{path}`
- jsDelivr必须用commit hash，不能用@gh-pages分支引用
- **当前最新commit**: `4be5498`（修复班味id字段，2026-05-12）

## 播放器技术要点
- 歌词偏移量：每首歌独立，存localStorage (key: bgm_lyrics_offset_{songId})，±0.5s步进，±5s限制
- 封面图容错：无图或加载失败显示渐变色+歌名默认封面
- 毫秒解析修复：`.5`→500ms, `.50`→500ms, `.500`→500ms（原错误解析为5ms/50ms/500ms）

## 工作流注意事项
- 新增歌曲后需更新music.json并推送到GitHub，然后用新commit hash更新CDN URL
- 活人感、邪修外耗的封面图是程序生成的渐变封面，非AI生成
