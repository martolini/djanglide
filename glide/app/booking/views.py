from django.shortcuts import redirect, get_object_or_404
from glide.app.booking.forms import BookForm
from glide.app.booking.models import BookRequest
from django.http import HttpResponseRedirect
from glide.core.profiles.models import Profile
def book_profile(request,id):
    if request.method == 'POST':# If the form has been submitted...
        form = BookForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['startTime']
            message = form.cleaned_data['message']
            seen = False
            target_sender = get_object_or_404(Profile, request.user.pk)
            target_recipient = get_object_or_404(Profile, pk=id)
            new_request = BookRequest(date=date,startTime=time,message=message,seen=seen,target_sender=target_sender,target_recipient=target_recipient)
            new_request.save()
    return redirect(Profile.objects.get(user=request.user))