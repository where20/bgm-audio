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
    将配图复制到 GitHub Pages images/ 目录，返回相对路径。
    CDN URL 会在 commit_and_push() 中统一处理。
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
        # 返回相对路径，commit_and_push 会统一转换为 CDN URL
        return f"images/{dest_filename}"
    except Exception as e:
        print(f"❌ 复制图片失败: {e}")
        return None


def add_new_music_to_playlist(meme, date, style, audio_path_or_url, image_path_or_url, lyrics=None):
    """
    添加新音乐到 music.json (playlist 格式，与 index.html 兼容)
    audio_path_or_url: 音频文件路径（自动上传）或 URL（直接使用）
    image_path_or_url: 图片文件路径（自动上传）或 URL（直接使用）
    """
    meme_id = f"{meme}_{date.replace('-', '')}"

    # 处理音频
    audio_url = None
    if audio_path_or_url:
        if os.path.exists(audio_path_or_url):
            # 文件已复制到 github-pages 目录，构建临时 URL（push 后会被更新）
            audio_filename = os.path.basename(audio_path_or_url)
            audio_url = f"music/{audio_filename}"
            print(f"📝 音频文件已就绪: {audio_path_or_url}")
            print(f"   （将在 git push 后更新为完整的 CDN URL）")
        else:
            audio_url = audio_path_or_url

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
    """
    提交更改并推送到 GitHub gh-pages 分支，然后更新 CDN URL。

    采用两步法避免循环依赖：
    1. 先 commit + push 媒体文件，获取 commit hash
    2. 用 amend 更新 music.json 中的 CDN URL（不产生新 commit），再 force push

    jsDelivr CDN 的 URL 格式: https://cdn.jsdelivr.net/gh/where20/bgm-audio@{hash}/...
    hash 必须指向**实际包含该文件**的 commit，不是 HEAD。
    因此新歌曲用 push 后的 hash，已有歌曲的 hash 不应被修改。
    """
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

        # === 第一步：提交所有文件（含媒体）并推送 ===
        subprocess.run(["git", "add", "."], cwd=GITHUB_PAGES_DIR, capture_output=True)
        subprocess.run(["git", "commit", "-m", f"🎵 更新音乐播放器: {date_str}"], cwd=GITHUB_PAGES_DIR, capture_output=True)

        push_result = subprocess.run(
            ["git", "push", "origin", "gh-pages", "-f"],
            cwd=GITHUB_PAGES_DIR,
            capture_output=True,
            text=True
        )

        if push_result.returncode != 0:
            print(f"❌ 推送失败: {push_result.stderr}")
            return False

        print("🚀 已推送到 GitHub Pages!")

        # 获取本次 push 的 commit hash（文件所在 commit）
        commit_result = subprocess.run(
            ["git", "log", "-1", "--format=%H"],
            cwd=GITHUB_PAGES_DIR,
            capture_output=True,
            text=True
        )
        commit_hash = commit_result.stdout.strip()[:7]  # 统一使用 7 位
        print(f"📝 Commit hash: {commit_hash}")

        # === 第二步：更新相对路径为 CDN URL，amend 到当前 commit ===
        data = load_music_json()
        updated = False
        for song in data.get("playlist", []):
            # 更新音频 URL（相对路径 → 完整 CDN URL）
            audio = song.get("audio", "")
            if audio and not audio.startswith("http"):
                filename = os.path.basename(audio)
                song["audio"] = f"https://cdn.jsdelivr.net/gh/where20/bgm-audio@{commit_hash}/music/{filename}"
                print(f"✅ 更新音频 URL: {song['audio']}")
                updated = True

            # 更新图片 URL（相对路径 → 完整 CDN URL）
            image = song.get("image", "")
            if image and not image.startswith("http"):
                filename = os.path.basename(image)
                song["image"] = f"https://cdn.jsdelivr.net/gh/where20/bgm-audio@{commit_hash}/images/{filename}"
                print(f"✅ 更新图片 URL: {song['image']}")
                updated = True

        if updated:
            save_music_json(data)
            # 用 amend 合并到当前 commit，不产生新 commit
            subprocess.run(["git", "add", "music.json"], cwd=GITHUB_PAGES_DIR, capture_output=True)
            subprocess.run(
                ["git", "commit", "--amend", "--no-edit"],
                cwd=GITHUB_PAGES_DIR,
                capture_output=True
            )
            # Force push 覆盖（amend 会改变 commit hash，但文件内容不变）
            # 注意：amend 后 hash 会变，但 music.json 里的 URL 指向的是 amend 前的 hash
            # 而那个 commit 已经 push 过了，jsDelivr 已经缓存了那些文件
            # 所以 CDN URL 仍然有效！
            subprocess.run(
                ["git", "push", "origin", "gh-pages", "-f"],
                cwd=GITHUB_PAGES_DIR,
                capture_output=True,
                text=True
            )
            print(f"🚀 已通过 amend 更新 CDN URL 并推送! 文件 commit: {commit_hash}")

        return True

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
    
    # 支持从文件读取歌词：以@开头表示文件路径
    lyrics_arg = sys.argv[6] if len(sys.argv) > 6 else None
    if lyrics_arg and lyrics_arg.startswith("@"):
        lyrics_file = lyrics_arg[1:]
        try:
            with open(lyrics_file, 'r', encoding='utf-8') as f:
                lyrics = f.read()
            print(f"✅ 已从文件读取歌词: {lyrics_file}")
        except Exception as e:
            print(f"❌ 读取歌词文件失败: {e}")
            lyrics = None
    else:
        lyrics = lyrics_arg.replace("\\n", "\n") if lyrics_arg else None

    add_new_music_to_playlist(meme, date, style, audio_url, image_path_or_url, lyrics)
    commit_and_push()


if __name__ == "__main__":
    main()
