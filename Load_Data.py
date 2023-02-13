import pandas as p

def create_datafarme():
    dataframe = pd.read_csv("Lung_cancer.csv")
    print("changes build")
    print(dataframe.head())
    return dataframe
create_datafarme()
