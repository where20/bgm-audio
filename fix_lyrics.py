#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从markdown文件提取带时间戳的歌词，更新到music.json
"""

import json
import re
import os

def extract_lyrics_from_md(md_file):
    """从markdown文件提取带时间戳的歌词"""
    if not os.path.exists(md_file):
        return None
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找歌词部分（带时间戳）
    lyrics_lines = []
    
    # 匹配时间戳格式：[MM:SS.mm] 或 [MM:SS]
    # 可能后面跟着 [标签] 或直接是歌词
    pattern = r'\[(\d{1,2}:\d{2}\.\d{1,3})\]\[?.*?\]?(.*)'
    
    lines = content.split('\n')
    in_lyrics_section = False
    
    for line in lines:
        # 检测歌词部分开始
        if '## 歌词' in line or '## 歌词（带时间戳）' in line:
            in_lyrics_section = True
            continue
        
        # 检测歌词部分结束
        if in_lyrics_section and line.startswith('---'):
            break
        
        if in_lyrics_section:
            # 匹配时间戳
            match = re.match(r'\[(\d{1,2}:\d{2}(?:\.\d{1,3})?)\].*?([^\n\[\]]+)$', line)
            if match:
                timestamp = match.group(1)
                lyric = match.group(2).strip()
                if lyric:
                    lyrics_lines.append(f'[{timestamp}]{lyric}')
            elif line.strip() and not line.startswith('#') and not line.startswith('['):
                # 可能是纯歌词行（无时间戳）
                lyrics_lines.append(line.strip())
    
    return '\n'.join(lyrics_lines) if lyrics_lines else None

def fix_music_json():
    """修复music.json中的歌词格式"""
    md_dir = '/Users/xiaoan/WorkBuddy/2026-05-05-task-3'
    json_file = os.path.join(md_dir, 'github-pages', 'music.json')
    
    # 读取music.json
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 为每个歌曲提取歌词
    for song in data['playlist']:
        meme = song.get('meme', '')
        date = song.get('date', '')
        
        # 构建可能的markdown文件名
        md_file = None
        possible_names = [
            f'热梗歌词-{meme}-{date}.md',
            f'热梗歌词内容-{date}.md'
        ]
        
        for name in possible_names:
            path = os.path.join(md_dir, name)
            if os.path.exists(path):
                md_file = path
                break
        
        if md_file:
            lyrics = extract_lyrics_from_md(md_file)
            if lyrics:
                song['lyrics'] = lyrics
                print(f'✅ 更新歌词: {meme}')
            else:
                print(f'⚠️  未找到歌词: {meme}')
        else:
            print(f'❌ 未找到文件: {meme}')
    
    # 写回music.json
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print('\n✅ music.json 已更新')

if __name__ == '__main__':
    fix_music_json()
