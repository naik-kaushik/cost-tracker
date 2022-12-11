import pandas as pd

read_file = pd.read_csv (r'D:\!scrap\Logitech G331-Leatherette.txt')
read_file.to_excel (r'D:\!scrap\Logitech G331-Leatherette.xlsx', index=None)