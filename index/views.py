from django.shortcuts import render

def post_list(request):
	return render(request, 'index/post_list.html', {})