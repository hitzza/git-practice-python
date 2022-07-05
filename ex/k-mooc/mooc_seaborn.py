import seaborn as sns
'''
iris = sns.load_dataset("iris")
sns.displot(iris["sepal_width"],
        kde=True,
        rug=True)
'''
#countplot
'''
titanic = sns.load_dataset('titanic')
sns.countplot(x='class',data= titanic)
'''
#relplot
'''
tips =sns.load_dataset('tips')
sns.relplot(x='total_bill', y='tip',hue ='smoker', data =tips, kind='line')
sns.relplot(x='total_bill', y='tip', hue='smoker',col='time',data=tips)
'''
#catplot
'''
tips = sns.load_dataset('tips')
sns.catplot(x='day',y='total_bill',data = tips)
sns.catplot(x='day',y='total_bill',hue='smoker',kind='bar',data=tips)
sns.catplot(x='day',y='total_bill',hue='smoker',kind='violin',data=tips)
'''
#boxenplot
'''
tips = sns.load_dataset('tips')
sns.boxenplot(x='day',y='total_bill',data=tips)
'''
#jointplot
'''
tips = sns.load_dataset('tips')
sns.jointplot(x='total_bill',y='tip',data=tips)
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
'''
#pairplot
'''
iris = sns.load_dataset('iris')
sns.pairplot(iris)
sns.pairplot(iris,vars=['sepal_length','sepal_width'])
'''
#heatmap
'''
flights = sns.load_dataset('flights')
flight = flights.pivot('month','year','passengers')
sns.heatmap(flight,annot=True,fmt='d')#annot=true숫자표시여부,fmt='d'정수형 데이터
'''