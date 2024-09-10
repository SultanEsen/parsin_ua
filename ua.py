import sqlite3
import pandas as pd
# from xlrd import sheet, book


con = sqlite3.connect('ua3.db')
# wb = pd.read_excel('ua2.xls', sheet_name='Реєстр', usecols=[0, 1, 2, 3, 4, 5, 9], header=0)
# wb = wb['Unnamed: 0'].str.replace('і', 'и')
# for sheet in wb:
#     print(sheet)
# print(type(wb))
# print(wb.columns)
# print(wb)
# db = sqlite3.connect(':memory:')
dfs = pd.read_excel('ua2.xls', sheet_name=None, usecols=[0, 1, 2, 3, 4, 5, 9])
for table, df in dfs.items():
    df.to_sql(table, con)

    # print(df)
# for sheet in wb:
#     wb[sheet].to_sql(sheet, con, index=False)
#     print(wb)
con.commit()
con.close()
