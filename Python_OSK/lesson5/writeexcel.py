# openpyxl: 外部ライブラリ
# 
# pip install openpyxl でinstall

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.worksheets[0]
sheet.title = 'サンプル'
sheet['C1'] = 'XXX'
sheet['E1'] = 'new'
wb.save('sample.xlsx')