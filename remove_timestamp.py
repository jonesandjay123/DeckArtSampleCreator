import os

def remove_timestamp_from_filenames(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.png'):
            # 將檔名分割成檔名和檔案擴展名
            name, extension = os.path.splitext(filename)
            # 移除檔名中的時間戳記部分
            new_name = name.split('_')[0] + extension
            # 產生舊檔名和新檔名的完整路徑
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            # 對檔案進行重新命名
            os.rename(old_path, new_path)

# 如果這個腳本被直接執行，則執行移除時間戳記的函數
if __name__ == "__main__":
    folder_path = "data"  # 指定要處理的資料夾路徑
    remove_timestamp_from_filenames(folder_path)
    print("Timestamps removed from filenames in the 'data' folder.")
