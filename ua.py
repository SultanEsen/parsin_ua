import sqlite3
import pandas as pd

# con = sqlite3.connect('ua3.db')
# wb = pd.read_excel('ua2.xls', sheet_name='Реєстр', usecols=[0, 1, 2, 3, 4, 5, 9])

con = sqlite3.connect('ua3.db')
wb = pd.read_excel('ua2.xls', sheet_name=None, usecols=[0, 1, 2, 3, 4, 5, 9])

for sheet in wb:
    wb[sheet].to_sql(sheet, con, index=False)
con.commit()
con.close()

print(wb)
