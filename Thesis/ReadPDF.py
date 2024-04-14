from pdfminer.high_level import extract_text
from openpyxl import Workbook
from datetime import datetime
import os

# 读取resource目录下的所有PDF文件
pdf_folder = 'resources'
pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith('.pdf')]

# 创建空列表存储论文信息
papers_info = []

# 遍历每个PDF文件
for file_name in pdf_files:
    paper_id = len(papers_info) + 1  # 论文编号从1开始
    paper_name = os.path.splitext(file_name)[0]  # 去除文件后缀名作为论文名字
    paper_references = []

    # 提取PDF文本
    pdf_path = os.path.join(pdf_folder, file_name)
    text = extract_text(pdf_path)

    # 查找参考文献部分
    if '参考文献' or 'References' in text:
        reference_index = text.find('参考文献')
        references_text = text[reference_index + 4:]  # 从“参考文献”关键词之后开始提取
        references_list = references_text.split('\n')  # 根据换行符分割成列表
        paper_references.extend(references_list)

    # 添加论文信息到列表中
    papers_info.append({'编号': paper_id, '名字': paper_name, '参考文献': paper_references})

# 生成时间戳
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# 创建Excel工作簿
wb = Workbook()
ws = wb.active

# 写入表头
ws.append(['论文编号', '论文名字', '参考文献'])

# 写入论文信息
for paper_info in papers_info:
    ws.append([paper_info['编号'], paper_info['名字'], '\n'.join(paper_info['参考文献'])])

# 保存Excel文件
excel_file_name = f'论文引用关系_{timestamp}.xlsx'
wb.save(excel_file_name)

print(f"Excel文件已创建成功: {excel_file_name}")
