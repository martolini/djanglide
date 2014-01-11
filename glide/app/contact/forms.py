from django.forms import forms
from django.forms.models import ModelForm
from glide.app.contact.models import Improvement

class ImprovementForm(ModelForm):
	class Meta:
		model = Improvement
		exclude = ('solved',)
		widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title here (e.g: "Problem sending messages")'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your email adress'}),
        }
