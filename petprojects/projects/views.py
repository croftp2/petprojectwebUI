from django.shortcuts import render

from django.http import HttpResponse

from pprint import pprint, pformat

from projects.models import Catagory, Project

def index(request):
	catagories = Catagory.objects.all()
	main_projects = Project.objects.all()
#	return HttpResponse(main_projects[0].catagory)
	catagorymap = {}
	for project in main_projects:
		if project.catagory in catagorymap:
			catagorymap[project.catagory].append(project)
		else:
			catagorymap[project.catagory] = []

	htmlnames = dict(zip(main_projects, [i.name.replace(' ','_') for i in main_projects]))

	return render(request, 'projects/index.html',\
		{"catagories":catagorymap, "htmlnames":htmlnames})

