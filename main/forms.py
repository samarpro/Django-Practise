from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label="Name",max_length=255)
    check = forms.BooleanField(required=False)

class DelForm(forms.Form):
    id_val=forms.IntegerField(label="Id Number",max_value=100)
    
class UploadFile(forms.Form):
    text = forms.CharField(max_length=150)
    file_path = forms.FileField()

class AccessForm(forms.Form):
    NameText = forms.CharField(max_length=255)
    