from sklearn import preprocessing
le = preprocessing.LabelEncoder()
from datavisualization import data_visualization
def feature_engineering():
    dataset = data_visualization()
    for col in dataset.columns:
        print(col, len(dataset[col].unique()))
    dataset['level'] = le.fit_transform(dataset.level)
    print(dataset.head())
    dataset = dataset.drop(["patient_id", "index"], axis =1)    
    print(dataset.head())
    dataset.to_csv('cleaned.csv')
    return dataset
feature_engineering()
