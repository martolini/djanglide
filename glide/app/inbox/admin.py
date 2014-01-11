from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from glide.app.inbox.models import Message, Conversation

class ConversationAdmin(ModelAdmin):
	list_display = ('receiver', 'sender', 'last_message')

class MessageAdmin(ModelAdmin):
	list_display = ('conversation', 'author', 'content', 'date', 'read')
	list_filter = ('author', 'date', 'read')

admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)