# install pandas, xlrd

import pandas as pd

def readTFT(filepath):
    tft = pd.read_excel(filepath)
    return tft

def main():
    readTFT("Lipidyzer_TFT1.xlsx")

if __name__ == "__main__":
    main()
