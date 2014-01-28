from django.shortcuts import render
from glide.app.booking.forms import BookForm

def book_profile(request):
	 # If the form has been submitted...
    form = BookForm(request.POST)
    if form.is_valid():
        date = form.cleaned_data['date']
        time = form.cleaned_data['startTime']
        message = form.cleaned_data['message']
        seen = False
        target_sender = request.user

    return render(request, 'base.html', {
        'form': form,
    })