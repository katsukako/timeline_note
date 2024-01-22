# 首先，我们将定义一些基本的功能和类

import json
import re
from datetime import datetime
import os

class Note:
    """笔记类，用于存储单个笔记的内容、时间和ID。"""
    def __init__(self, content, date,note_id, tags):
        self.content = content
        self.date = date
        self.id = note_id
        self.tags = tags

class NoteManager:
    """笔记管理类，用于处理添加、保存、展示和搜索笔记。"""
    def __init__(self):
        self.file_path =  "./timeline_note/notes.json" 
        self.notes = []
        self.new_notes = []  # 用于存储尚未保存的新笔记
        self.current_id_index = 0
        self.load_notes()

    def add_note(self, content, date, tags):
        """添加笔记"""
        note_id = self.generate_id()
        note = Note(content, date, note_id, tags)
        self.notes.append(note)
        self.new_notes.append(note)  # 将新笔记添加到新笔记列表
        return note_id

    def generate_id(self):
        """生成唯一ID"""
        id_range = (ord('z') - ord('a') + 1) * 10000
        if self.current_id_index >= id_range:
            raise Exception("已达到ID分配上限")
        base_id = self.current_id_index
        letter = chr(ord('a') + base_id // 10000)
        number = base_id % 10000
        self.current_id_index += 1
        return f"{letter}{number:04d}"

    def save_notes(self):
        """保存笔记到文件"""
        """保存笔记到文件，保留现有数据"""
        if self.new_notes:
            existing_notes = []
            if os.path.exists(self.file_path):
                with open(self.file_path, "r", encoding="utf-8") as file:
                    if os.path.getsize(self.file_path) > 0:
                        existing_notes = json.load(file)

            all_notes = existing_notes + [note.__dict__ for note in self.new_notes]
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(all_notes, file, ensure_ascii=False, indent=4)
            
            self.new_notes = []  # 清空新笔记列表


    def load_notes(self):
        """从文件中加载笔记"""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                notes_data = json.load(file)
                for note_data in notes_data:
                    # 检查每个笔记数据是否包含tags
                    tags = note_data.get("tags", [])  # 如果不存在tags，则默认为空
                    note = Note(note_data["content"], note_data["date"], note_data["id"], tags)
                    self.notes.append(note)
                    # 更新ID计数器以保证ID的唯一性
                    self.current_id_index = max(self.current_id_index, int(note.id[1:]) + 1)

    def display_notes(self):
        """展示笔记，每页显示20条"""
        # 排序笔记
        sorted_notes = sorted(self.notes, key=lambda x: x.date)
        for i, note in enumerate(sorted_notes):
            if i % 20 == 0 and i != 0:
                input("按任意键继续...")
            print(f"ID: {note.id} | 日期: {note.date} | 内容: {note.content} | 标签: {note.tags}\n")

    def search_notes(self, keyword):
        """根据关键词搜索笔记"""
        matching_notes = [note for note in self.notes if keyword in note.content]
        if matching_notes:
            for note in matching_notes:
                print(f"ID: {note.id} | 日期: {note.date} | 内容: {note.content} | 标签: {note.tags}\n")
        else:
            print("不存在匹配的笔记。")
    
    def jump_to_note(self, note_id):
        """跳转到特定ID的笔记"""
        found_note = next((note for note in self.notes if note.id == note_id), None)
        if found_note:
            print(f"ID: {found_note.id} | 日期: {found_note.date} | 内容: {found_note.content} | 标签: {found_note.tags}\n")
        else:
            print("未找到指定ID的笔记。")


# 接下来我们将定义主界面逻辑和交互部分
# 注意：由于环境限制，以下代码无法直接运行，仅供参考
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def main():
    note_manager = NoteManager()  # 创建实例时传入文件路径
    while True:
        command = input("请输入命令（I：添加笔记,并自动保存）D：展示笔记，SC：搜索笔记，CD：跳转笔记，ESC：退出）：")
        if command == "I":
            # 添加笔记的逻辑
            date = input("请输入日期 (YYYY-MM-DD)：")
            while not is_valid_date(date):
                print("日期格式错误，请重新输入。")
                date = input("请输入日期 (YYYY-MM-DD)：")
            content = input("请输入笔记内容：")
            tags_input = input("请输入标签（用逗号分隔）：")
            tags = tags_input.split(',')  # 将输入的标签字符串分割为列表           
            note_id = note_manager.add_note(content, date, tags)
            print(f"笔记已添加，ID为：{note_id}")
            note_manager.save_notes()
            print("笔记已保存。")
        # 其他命令的处理逻辑将在后续添加
        elif command == "D":
            # 展示笔记的逻辑
            # 展示笔记的逻辑
            note_manager.display_notes()
        elif command == "SC":
            # 搜索笔记的逻辑
            keyword = input("请输入搜索关键词：")
            note_manager.search_notes(keyword)
        elif command == "CD":
            # 跳转到特定笔记的逻辑
            note_id = input("请输入笔记ID：")
            note_manager.jump_to_note(note_id)
        elif command == "ESC":
            # 退出程序
            break

# 辅助功能尚未实现
main()
print('notes end.')