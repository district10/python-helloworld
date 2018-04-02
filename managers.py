import sys
import pandas as pd

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'res/managers.xlsx'
    xl = pd.ExcelFile(filename)
    print(xl.sheet_names)
