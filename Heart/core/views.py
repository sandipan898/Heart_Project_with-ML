from django.shortcuts import render,HttpResponse
from .forms import CreateFormForHeart
import sklearn
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score,mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

heart=pd.read_csv('D:\Machine Learning\Project\heart.csv')
x=heart
y=heart.target
x.drop('target',axis=1,inplace=True)
sc = StandardScaler()
X = sc.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=10,test_size=0.3,shuffle=True)

# this is for KNN
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)




# Create your views here.
def form_view(request):
    if request.method=="POST":
        print(request.POST)
        fm=CreateFormForHeart(request.POST)
        
        if fm.is_valid():
            user=fm.cleaned_data['name']
            age=fm.cleaned_data['age']
            sex=fm.cleaned_data['sex']
            cp=fm.cleaned_data['cp']
            trestbps=fm.cleaned_data['trestbps']
            chol=fm.cleaned_data['chol']
            fbs=fm.cleaned_data['fbs']
            restecg=fm.cleaned_data['restecg']
            thalach=fm.cleaned_data['thalach']
            exang=fm.cleaned_data['exang']
            oldpeak=fm.cleaned_data['oldpeak']
            slope=fm.cleaned_data['ca']
            thal=fm.cleaned_data['thal']
            ca=fm.cleaned_data['ca']
    #             index = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
    #    'exang', 'oldpeak', 'slope', 'ca', 'thal']

    #             for list in index:
    #                  print( list=fm.cleaned_data[index[list]])

            X_DT=np.array([[age ,sex, cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,thal,ca]])
            X_DT=sc.transform(X_DT)
            X_DT_prediction=dt.predict(X_DT)
            print(X_DT_prediction[0])
    else:
        fm=CreateFormForHeart()
    return render(request ,'Mainapp/index.html',{'form':fm})


def resault_view(request):
    return render(request ,'Mainapp/resault.html')