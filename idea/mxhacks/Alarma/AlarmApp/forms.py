from django import forms


class registro(forms.Form):  
	name = forms.CharField(label="Nombre", max_length = 100)
	email =  forms.CharField(label="Mail", max_length = 100)
	password = forms.CharField(label="Pass", max_length = 100)

	

