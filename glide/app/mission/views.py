from django.shortcuts import render

def mission(request):
	return render(request, 'mission/base.html')
