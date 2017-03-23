from django.template.defaulttags import csrf_token
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.utils import timezone
from .models import Post
from .models import Library
from .models import Floor
from django.core.exceptions import *

def post_list(request):
	libraries = Library.objects.all()
	floors = Floor.objects.all().order_by('floor_number')
	return render(request, 'index/post_list.html', {'libraries': libraries, 'floors': floors})

def submit(request):
		print("called")
		libraries = Library.objects.all()
		floors = Floor.objects.all().order_by('floor_number')
		if request.method == 'POST':	
			if request.POST.get("numRange"):
				curr_ratings = request.POST.get('numRange')
				f = Floor.objects.get(libname = "Marston Science Library", floor_number = 1)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange1"):
				curr_ratings = request.POST.get('numRange1')
				f = Floor.objects.get(libname = "Marston Science Library", floor_number = 2)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange2"):
				curr_ratings = request.POST.get('numRange2')
				f = Floor.objects.get(libname = "Marston Science Library", floor_number = 3)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange3"):
				curr_ratings = request.POST.get('numRange3')
				f = Floor.objects.get(libname = "Marston Science Library", floor_number = 4)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange4"):
				curr_ratings = request.POST.get('numRange4')
				f = Floor.objects.get(libname = "Marston Science Library", floor_number = 5)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange5"):
				curr_ratings = request.POST.get('numRange5')
				f = Floor.objects.get(libname = "Library West", floor_number = 1)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange6"):
				curr_ratings = request.POST.get('numRange6')
				f = Floor.objects.get(libname = "Library West", floor_number = 2)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange7"):
				curr_ratings = request.POST.get('numRange7')
				f = Floor.objects.get(libname = "Library West", floor_number = 3)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange8"):
				curr_ratings = request.POST.get('numRange8')
				f = Floor.objects.get(libname = "Library West", floor_number = 4)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
			elif request.POST.get("numRange9"):
				curr_ratings = request.POST.get('numRange9')
				f = Floor.objects.get(libname = "Library West", floor_number = 6)
				f.changerating(rate = curr_ratings)
				f.changethecapacity(rate = curr_ratings)
		return render(request, 'index/post_list.html', {'libraries': libraries, 'floors': floors})	