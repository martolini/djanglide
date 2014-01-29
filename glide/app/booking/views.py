from django.shortcuts import redirect, get_object_or_404
from glide.app.booking.forms import BookForm
from django.http import HttpResponseRedirect
from glide.core.profiles.models import Profile
from glide.core.notifications.models import Notification
def book_profile(request,id):
    if request.method == 'POST':# If the form has been submitted...
        form = BookForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.target_sender = get_object_or_404(Profile, user=request.user)
            item.target_recipient = get_object_or_404(Profile, pk=id)
            item.save()
            new_notification = Notification(actionType="book",target_recipient=item.target_recipient.user,target_sender=item.target_sender.user)
            new_notification.save()
        print form.errors
    return redirect(Profile.objects.get(user=request.user))