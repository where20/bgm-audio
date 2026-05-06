#!/usr/bin/env python3
"""
更新 GitHub Pages 音乐播放器数据
将新生成的音乐和配图添加到 music.json (playlist格式) 并推送到 GitHub
"""

import json
import os
import subprocess
import shutil
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


def upload_image_to_github(image_path, meme_id):
    """
    将配图复制到 GitHub Pages images/ 目录
    返回图片的 CDN URL (使用 gh-pages 分支)
    """
    if not image_path or not os.path.exists(image_path):
        print(f"⚠️ 图片文件不存在: {image_path}")
        return None

    ext = os.path.splitext(image_path)[1] or '.png'
    dest_filename = f"cover_{meme_id}{ext}"
    dest_path = os.path.join(GITHUB_PAGES_DIR, "images", dest_filename)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    try:
        shutil.copy2(image_path, dest_path)
        print(f"✅ 已复制图片到: {dest_path}")
        # 获取当前 commit hash 用于 CDN URL（比分支名更稳定）
        try:
            result = subprocess.run(
                ["git", "log", "-1", "--format=%H"],
                cwd=GITHUB_PAGES_DIR,
                capture_output=True,
                text=True
            )
            commit_hash = result.stdout.strip()[:12] if result.returncode == 0 else "gh-pages"
        except Exception:
            commit_hash = "gh-pages"

        cdn_url = f"https://cdn.jsdelivr.net/gh/where20/bgm-audio@{commit_hash}/images/{dest_filename}"
        return cdn_url
    except Exception as e:
        print(f"❌ 复制图片失败: {e}")
        return None


def add_new_music_to_playlist(meme, date, style, audio_url, image_path_or_url, lyrics=None):
    """
    添加新音乐到 music.json (playlist 格式，与 index.html 兼容)
    image_path_or_url: 图片文件路径（自动上传）或 URL（直接使用）
    """
    meme_id = f"{meme}_{date.replace('-', '')}"

    # 处理图片
    image_url = None
    if image_path_or_url:
        if os.path.exists(image_path_or_url):
            image_url = upload_image_to_github(image_path_or_url, meme_id)
        else:
            image_url = image_path_or_url

    new_song = {
        "id": meme_id,
        "meme": meme,
        "date": date,
        "style": style,
        "audio": audio_url,
        "image": image_url or "",
    }
    if lyrics:
        new_song["lyrics"] = lyrics

    data = load_music_json()

    # 确保 playlist 存在
    data.setdefault("playlist", [])

    # 去除旧条目（相同 id）后插入到最前面
    data["playlist"] = [s for s in data["playlist"] if s.get("id") != meme_id]
    data["playlist"].insert(0, new_song)

    # 只保留最近 30 首
    data["playlist"] = data["playlist"][:30]

    # 更新 meta
    data["meta"] = {
        "lastUpdated": date,
        "totalSongs": len(data["playlist"]),
        "description": "热梗歌词音乐播放列表 - 每天自动更新"
    }

    save_music_json(data)

    print(f"✅ 已添加新音乐: {meme}")
    print(f"   ID: {meme_id}")
    print(f"   音频: {audio_url}")
    if image_url:
        print(f"   图片: {image_url}")

    return new_song


def commit_and_push():
    """提交更改并推送到 GitHub gh-pages 分支"""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=GITHUB_PAGES_DIR,
            capture_output=True,
            text=True
        )

        if not result.stdout.strip():
            print("📝 没有需要提交的更改")
            return False

        subprocess.run(["git", "config", "user.email", "workbuddy@automated.dev"], cwd=GITHUB_PAGES_DIR, capture_output=True)
        subprocess.run(["git", "config", "user.name", "WorkBuddy Auto"], cwd=GITHUB_PAGES_DIR, capture_output=True)

        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run(["git", "add", "."], cwd=GITHUB_PAGES_DIR, capture_output=True)
        subprocess.run(["git", "commit", "-m", f"🎵 更新音乐播放器: {date_str}"], cwd=GITHUB_PAGES_DIR, capture_output=True)

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
        print("用法: python3 update_github_pages.py <热梗> <日期> <风格> <音频URL> <图片路径或URL> <歌词>")
        print("\n示例: python3 update_github_pages.py 酸黄瓜 2026-05-06 波浪型 ... ...")
        sys.exit(1)

    meme = sys.argv[1]
    date = sys.argv[2]
    style = sys.argv[3]
    audio_url = sys.argv[4]
    image_path_or_url = sys.argv[5]
    lyrics = sys.argv[6].replace("\\n", "\n") if len(sys.argv) > 6 else None

    add_new_music_to_playlist(meme, date, style, audio_url, image_path_or_url, lyrics)
    commit_and_push()


if __name__ == "__main__":
    main()
