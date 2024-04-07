import pandas as pd 

def readDataFile(readPath):
    try: 
        if (readPath[-4:] == ".csv"):
            dfFile = pd.read_csv(readPath, header = 0, sep = ',')
        elif (readPath[-4:] == ".xls") or (readPath[-5:] == ".xlsx"):
            dfFile = pd.read_excel(readPath, header = 0)
        elif (readPath[-4:] == ".dat"):
            dfFile = pd.read_csv(readPath, header = 0, sep = ' ')
        else:
            print("Error: File format not supported")
    except Exception as e:
        print("fail to read data file {}".format(str(e)))
        return
    return dfFile

def main():
    readPath = "./data.dat"
    dfFile = readDataFile(readPath)

    print(type(dfFile))
    print(dfFile.shape)
    print(dfFile.head())

    return

if __name__ == "__main__":
    main()
