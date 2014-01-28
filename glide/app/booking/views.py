from django.shortcuts import render
from glide.app.booking.forms import BookForm
def book_profile(request):
	if request.method == 'POST': # If the form has been submitted...

        form = BookForm(request.POST) # A form bound to the POST data
        if form.is_valid(): 
        	date = form.cleaned_data['date']
        	time = form.cleaned_data['startTime']
        	message = form.cleaned_data['message']
        	seen = False
        	target_sender = request.user
        	target_recipient = 
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = BookForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })