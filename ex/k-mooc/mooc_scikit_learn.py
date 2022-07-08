from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
import seaborn as sns

iris = load_iris()
iris_data = iris.data
iris_label = iris.target
iris_df = pd.DataFrame(data=iris_data,columns=iris.feature_names)
iris_df['label'] = iris.target

sns.pairplot(iris_df,x_vars=['sepal length (cm)'],
            y_vars=['sepal width (cm)'], hue ='label', height=5)

x_train,x_test,y_train,y_test = train_test_split(iris_data,iris_label,test_size=0.2)

dt_dlf =DecisionTreeClassifier()
knn_clf = KNeighborsClassifier()

dt_dlf.fit(x_train,y_train)
knn_clf.fit(x_train,y_train)

y1_pred = dt_dlf.predict(x_test)
y2_pred = knn_clf.predict(x_test)

print('DecisionTree 예측 정확도: {0: .4f}'.format(accuracy_score(y_test,y1_pred)))
print('K-NN 예측 정확도: {0: .4f}'.format(accuracy_score(y_test,y2_pred)))