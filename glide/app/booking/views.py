from django.shortcuts import redirect, get_object_or_404, render
from glide.app.booking.forms import BookForm
from django.http import HttpResponseRedirect
from glide.core.profiles.models import Profile
from glide.core.notifications.models import Notification
from glide.app.booking.models import BookRequest, Meetup
def book_profile(request,id):
    if request.method == 'POST':# If the form has been submitted...
        form = BookForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.target_sender = get_object_or_404(Profile, user=request.user)
            item.target_recipient = get_object_or_404(Profile, pk=id)
            item.save()
            target_recipient = item.target_recipient
            new_notification = Notification(actionType="book",target_recipient=target_recipient.user,target_sender=item.target_sender.user)
            new_notification.save()
            book_request = BookRequest(meetup=item,target_recipient=target_recipient)
            book_request.save()
        print form.errors
    return redirect(Profile.objects.get(user=request.user))

def book_requests(request):
    return render(request, 'booking/bookings.html')

def accept_button(request,id):
    book_req = get_object_or_404(BookRequest, pk=id)
    book_req.response = True
    book_req.save()
    meetup = get_object_or_404(Meetup, pk=book_req.get_meetup().pk)
    return HttpResponseRedirect('/book/')

def decline_button(request,id):
    book_req = get_object_or_404(BookRequest, pk=id)
    book_req.response = False
    book_req.save()
    meetup = get_object_or_404(Meetup, pk=book_req.get_meetup().pk)
    return HttpResponseRedirect('/book/')