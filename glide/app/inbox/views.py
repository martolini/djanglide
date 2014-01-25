from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from glide.app.inbox.models import Message, Conversation
from glide.app.inbox.forms import ReplyMessageForm, NewMessageForm
from django.db.models import Q
from django.http import HttpResponsePermanentRedirect
from glide.core.profiles.models import Profile
from glide.core.notifications.models import Notification
@login_required
def inbox(request):
	conversations = Conversation.objects.filter(Q(receiver=request.user) | Q(sender=request.user)).order_by('-last_message')
	return render(request, 'inbox/inbox.html', {'conversations':conversations})

def mark_as_read(user, conversation):
	messages = Message.objects.filter(conversation=conversation).exclude(read=True).exclude(author=user)
	for message in messages:
		message.read = True
		message.save()

@login_required
def view_conversation(request, id):
	conversation = get_object_or_404(Conversation, pk=id)
	mark_as_read(request.user, conversation)
	messages = Message.objects.filter(conversation=conversation).order_by('-date')
	return render(request, 'inbox/conversation.html', {'messages':messages,
														'conversation':conversation})

@login_required
def reply(request):
	if request.method == 'POST':
		form = ReplyMessageForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.author = request.user
			item.save()
			conversation = item.conversation
			conversation.save()
			return HttpResponsePermanentRedirect(conversation.get_absolute_url())

@login_required
def new_message(request, id):
	profile = get_object_or_404(Profile, pk=id)
	receiver = profile.user
	conversation = None
	if conversation == None:
		try:
			conversation = Conversation.objects.get(sender=request.user, receiver=receiver)
			return view_conversation(request, conversation.pk)
		except:
			pass
	if conversation == None:
		try:
			conversation = Conversation.objects.get(sender=receiver, receiver=request.user)
			return view_conversation(request, conversation.pk)
		except:
			pass

	form = NewMessageForm()
	if request.method == 'POST':
		form = NewMessageForm(request.POST)
		if form.is_valid():
			conversation = Conversation(sender=request.user, receiver=receiver)
			conversation.save()
			item = form.save(commit=False)
			item.conversation = conversation
			item.author = request.user
			item.save()
			return view_conversation(request, conversation.pk)
	return render(request, 'inbox/form.html', {'form':form})

