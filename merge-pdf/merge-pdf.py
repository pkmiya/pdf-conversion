import os
from PyPDF2 import PdfMerger

# 結合するPDFファイルのディレクトリパス
pdf_dir = './input'

# 出力ファイルのパス
output_file_path = 'merged.pdf'

# ディレクトリ内のPDFファイルを取得し、アルファベット順にソート
pdf_files = sorted([os.path.join(pdf_dir, filename) for filename in os.listdir(pdf_dir) if filename.endswith('.pdf')])
# または，特定の文字列＋ナンバリングのファイル名のみ
# pdf_files = [f'./input/compsys3-{i}.pdf' for i in range(x + 1)]  # xを連番の最大値に置き換え


print("Merging pdf files in this order:")
for pdf_file in pdf_files:
    print(pdf_file)

# PDFファイルの結合
pdf_merger = PdfMerger()
for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

# # 結合したPDFファイルを保存
pdf_merger.write(output_file_path)
pdf_merger.close()

print(f'Successfully merged and saved as {output_file_path}.')
