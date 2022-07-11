from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
import pandas as pd

def svc_parm_selection(X,y,nfold):#그리드 서치를 이용한 최적의 파라미터값과 결과를 출력과 리턴해주는 함수
    svm_pararmeters = [{'kernel' : ['rbf'],
            'gamma' : [0.00001, 0.0001, 0.001, 0.01, 0.1, 1],#감마 값
            'C' : [0.01, 0.1,1,10,100,1000]}]#코스트 값
    clf = GridSearchCV(SVC(), svm_pararmeters, cv = nfold)#그리드 서치를 이용해서 최적의 파라미터값을 출력
    clf.fit(X,y)
    print(clf.best_params_)
    return clf

df = pd.read_csv("https://raw.githubusercontent.com/wikibook/machine-learning/2.0/data/csv/basketball_stat.csv")
train, test = train_test_split(df,test_size=0.2)#테스트와 트레이닝 데이터를 8:2비율로 나눔

X_train = train[['3P', 'BLK']]#3점슛과 블락수를 학습
y_train = train[['Pos']]#포지션으로 분류
clf = svc_parm_selection(X_train, y_train.values.ravel(), 10)#10은 교차검증 횟수

X_test = test[['3P', 'BLK']]
y_test = test[['Pos']]

y_true, y_pred = y_test, clf.predict(X_test)

print(classification_report(y_true, y_pred))
print()
print('accuracy'+str(accuracy_score(y_true,y_pred)))

print('-'*30)

comparison = pd.DataFrame({'prediction': y_pred,
            'ground_truth': y_true.values.ravel()})

print(comparison)