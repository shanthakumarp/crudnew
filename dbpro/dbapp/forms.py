from django import forms


class PersonForm(forms.Form):
	name = forms.CharField(max_length = 220)
	phone = forms.IntegerField()
	age = forms.IntegerField()

	# def __init__(self, *args, **kwargs):
	# 	prs = kwargs.pop('instance')
	# 	super(PersonForm, self).__init__(*args, **kwargs)