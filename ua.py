import sqlite3
import pandas as pd

con = sqlite3.connect('ua.db')
wb = pd.read_excel('ua_file.xls', sheet_name=None)

for sheet in wb:
    wb[sheet].to_sql(sheet, con, index=False)
con.commit()
con.close()
