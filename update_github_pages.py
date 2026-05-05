#!/usr/bin/env python3
"""
更新 GitHub Pages 音乐播放器数据
将新生成的音乐添加到 music.json 并推送到 GitHub
"""

import json
import os
import subprocess
from datetime import datetime

WORKSPACE = "/Users/xiaoan/WorkBuddy/2026-05-05-task-3"
GITHUB_PAGES_DIR = os.path.join(WORKSPACE, "github-pages")
MUSIC_JSON_PATH = os.path.join(GITHUB_PAGES_DIR, "music.json")

def load_music_json():
    """加载当前的 music.json"""
    with open(MUSIC_JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_music_json(data):
    """保存 music.json"""
    with open(MUSIC_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_new_music(meme, date, style, audio_url, image_url, lyrics):
    """添加新音乐到 music.json"""
    # 生成ID
    meme_id = f"{meme}_{date.replace('-', '')}"
    
    new_music = {
        "id": meme_id,
        "meme": meme,
        "date": date,
        "style": style,
        "audio": audio_url,
        "image": image_url,
        "lyrics": lyrics
    }
    
    # 加载并更新
    data = load_music_json()
    
    # 更新 latest
    data["latest"] = new_music
    
    # 添加到 history（如果不存在）
    existing_ids = [m["id"] for m in data.get("history", [])]
    if meme_id not in existing_ids:
        data.setdefault("history", []).insert(0, new_music)
    
    # 只保留最近30条历史
    data["history"] = data["history"][:30]
    
    # 保存
    save_music_json(data)
    
    print(f"✅ 已添加新音乐: {meme}")
    print(f"   ID: {meme_id}")
    print(f"   音频: {audio_url}")
    
    return new_music

def commit_and_push():
    """提交更改并推送到 GitHub gh-pages 分支"""
    try:
        # 检查是否有更改
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=GITHUB_PAGES_DIR,
            capture_output=True,
            text=True
        )
        
        if not result.stdout.strip():
            print("📝 没有需要提交的更改")
            return False
        
        # 配置 git（如果需要）
        subprocess.run(["git", "config", "user.email", "workbuddy@automated.dev"], cwd=GITHUB_PAGES_DIR, capture_output=True)
        subprocess.run(["git", "config", "user.name", "WorkBuddy Auto"], cwd=GITHUB_PAGES_DIR, capture_output=True)
        
        # 提交
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(["git", "add", "."], cwd=GITHUB_PAGES_DIR, capture_output=True)
        subprocess.run(["git", "commit", "-m", f"🎵 更新音乐播放器: {date_str}"], cwd=GITHUB_PAGES_DIR, capture_output=True)
        
        # 推送到 gh-pages
        result = subprocess.run(
            ["git", "push", "origin", "gh-pages", "-f"],
            cwd=GITHUB_PAGES_DIR,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("🚀 已推送到 GitHub Pages!")
            return True
        else:
            print(f"❌ 推送失败: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Git 操作失败: {e}")
        return False

def main():
    """主函数 - 从自动化任务调用"""
    import sys
    
    if len(sys.argv) < 7:
        print("用法: python3 update_github_pages.py <热梗> <日期> <风格> <音频URL> <图片URL> <歌词>")
        sys.exit(1)
    
    meme = sys.argv[1]
    date = sys.argv[2]
    style = sys.argv[3]
    audio_url = sys.argv[4]
    image_url = sys.argv[5]
    lyrics = sys.argv[6].replace("\\n", "\n")  # 处理换行符
    
    # 添加新音乐
    add_new_music(meme, date, style, audio_url, image_url, lyrics)
    
    # 提交并推送
    commit_and_push()

if __name__ == "__main__":
    main()
