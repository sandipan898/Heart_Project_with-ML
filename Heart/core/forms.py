from django import forms
select_sex = (("0","Female",), ("1","Male"))
select_cp = (("0","typical angina"),("1","atypical angina"),("2","non-anginal pain"),("3","asymptomatic"))
select_fbs = (("1","Yes"),("2","No"))
select_restecg = (("0","Normal"),("1","Having ST-T wave abnormality"),("2","Showing probable or definite left"))
select_exang = (("1","Yes"),("0","No"))
select_slope = (("1","Upsloping"),("2","Flat"),("3","Downsloping"))
select_ca=(("0","0"),("1","1"),("2","2"),("3","3"))
select_thal = (("0","Normal"),("1","Fixed defect"),("2","Blood flow normal"),("3","Reversible defect"))
class CreateFormForHeart(forms.Form):
    name=forms.CharField(max_length=100 )
    sex=forms.ChoiceField(choices=select_sex)
    cp=forms.ChoiceField(choices=select_cp)
    age=forms.IntegerField()
    trestbps=forms.IntegerField()
    chol=forms.IntegerField()
    fbs=forms.ChoiceField(choices=select_fbs)
    restecg=forms.ChoiceField(choices=select_restecg)
    thalach = forms.IntegerField()
    exang = forms.ChoiceField(choices=select_exang)
    oldpeak=forms.FloatField()
    slope=forms.ChoiceField(choices=select_slope)
    ca=forms.ChoiceField(choices=select_ca)
    thal=forms.ChoiceField(choices=select_thal)
# max_length trestbps