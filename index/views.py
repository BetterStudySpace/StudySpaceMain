from django.shortcuts import render
from django.utils import timezone
from django.template import Template, Context
from .models import Post
from .models import Library
from .models import Floor

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	libraries = Library.objects.all()
	floors = Floor.objects.all().order_by('floor_number')
	return render(request, 'index/post_list.html', {'posts': posts, 'libraries': libraries, 'floors': floors})