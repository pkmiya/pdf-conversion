import glob
import os

folder_path = 'target'
extension = '.jpg'  # 追加する拡張子

for filename in os.listdir(folder_path):
    if filename.isdigit():  # ファイル名が数字の場合
        old_path = os.path.join(folder_path, filename)
        new_filename = filename + extension
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
