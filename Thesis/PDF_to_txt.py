import os
import pdfplumber

file_dir = r'resources'
file_list = []
for files in os.walk(file_dir):
    for file in files[2]:
        if os.path.splitext(file)[1] == '.pdf' or os.path.splitext(file)[1] == '.PDF':
            file_list.append(file_dir + '\\' + file)

text_all = []
for i in range(len(file_list)):
    print("正在读取" + file_list[i])
    pdf = pdfplumber.open(file_list[i])
    pages = pdf.pages
    for page in pages:
        text = page.extract_text()
        text_all.append(text)
    text_all.append("---------------------------------------------------------------------------------")

text_all = ' '.join(text_all)
# print(text_all)

file = open('paper.txt', mode='a', encoding='utf-8')
file.write(text_all)

# # 重新遍历文件列表，提取参考文献并写入新的文件
# for file_path in file_list:
#     file_name = os.path.splitext(os.path.basename(file_path))[0]  # 提取文件名
#     references = ""
#     with open('paper.txt', mode='r', encoding='utf-8') as f:
#         text = f.read()
#         index = text.find("参考文献：")
#         if index == -1:
#             index = text.find("References:")
#         if index != -1:
#             references = text[index:]
#             end_index = references.find(
#                 '---------------------------------------------------------------------------------')
#             references = references[:end_index]
#
#     # 写入到新文件中
#     output_file_path = os.path.join(file_dir, f"{file_name}_references.txt")
#     with open(output_file_path, mode='w', encoding='utf-8') as f:
#         f.write(references)
