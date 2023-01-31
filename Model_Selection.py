from Data_Splitting import data_splitting
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
from sklearn.neighbors import KNeighborsClassifier
knc = KNeighborsClassifier()
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import pickle
import warnings
warnings.filterwarnings("ignore")
def model_selection():
    scores = []
    x_train, x_test, y_train, y_test = data_splitting()
    knc.fit(x_train, y_train)
    scores.append(knc.score(x_test, y_test))
    rfc.fit(x_train, y_train)
    scores.append(rfc.score(x_test, y_test))
    print(scores)
    y_predict = rfc.predict(x_test)
    precision = precision_score(y_test, y_predict, pos_label='positive', average='micro')
    recall = recall_score(y_test, y_predict, pos_label='positive', average='micro')
    accuracy = accuracy_score(y_test, y_predict)
    f1score = f1_score(y_test, y_predict, pos_label='positive', average='micro')
    print("Precision = ", precision)
    print("f1score = ", f1score)
    print("recall = ", recall)
    print("accuracy = ", accuracy)    
    with open("best_model.pkl", 'wb') as p:
        pickle.dump(rfc,p)
    return scores
model_selection()
