import json

def add_default_tags(file_path, default_tag='tech'):
    # 尝试打开并读取现有的笔记数据
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return
    except json.JSONDecodeError:
        print(f"文件 {file_path} 不是有效的 JSON 格式。")
        return

    # 为没有tags的笔记添加默认标签
    updated = False
    for note in notes:
        if 'tags' not in note:
            note['tags'] = [default_tag]
            updated = True

    # 如果有更新，则将数据写回文件
    if updated:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print("笔记已更新。")
    else:
        print("没有需要更新的笔记。")

# 定义文件路径并调用函数
file_path = "./timeline_note/notes.json"
add_default_tags(file_path)
