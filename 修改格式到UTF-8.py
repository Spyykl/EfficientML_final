import os  
import chardet  
import shutil  
  
def detect_encoding(file_path):  
    with open(file_path, 'rb') as f:  
        raw_data = f.read()  
    return chardet.detect(raw_data)['encoding']  
  
def convert_to_utf8(src_folder, dst_folder):  
    if not os.path.exists(dst_folder):  
        os.makedirs(dst_folder)  
  
    for file_name in os.listdir(src_folder):  
        if file_name.endswith('.txt'):  
            src_file_path = os.path.join(src_folder, file_name)  
            dst_file_path = os.path.join(dst_folder, file_name)  
              
            encoding = detect_encoding(src_file_path)  
            if encoding != 'utf-8':  
                with open(src_file_path, 'r', encoding=encoding, errors='ignore') as f:  
                    content = f.read()  
                  
                with open(dst_file_path, 'w', encoding='utf-8') as f:  
                    f.write(content)  
                print(f"Converted {file_name} from {encoding} to UTF-8.")  
            else:  
                # If the file is already UTF-8, just copy it to the destination folder  
                shutil.copy2(src_file_path, dst_file_path)  
                print(f"Copied {file_name} (already UTF-8).")  
  
# Replace with your source and destination folders  
src_folder = 'E:/Resources/本科学习/统计学学习资料/深度学习&数据可视化/数据可视化final/所有txt文件'  
dst_folder = 'E:/Resources/本科学习/统计学学习资料/深度学习&数据可视化/数据可视化final/所有txt文件/修改后'  
  
convert_to_utf8(src_folder, dst_folder)