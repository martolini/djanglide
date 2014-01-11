from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from glide.app.contact.models import Improvement
from glide.app.contact.forms import ImprovementForm

def contact(request):
	form = ImprovementForm()
	if request.method == 'POST':
		form = ImprovementForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'contact/thanks.html')

	return render(request, 'contact/base.html', {'form':form})
