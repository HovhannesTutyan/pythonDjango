from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse("Woman appliacation page")
def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1> Articles by categories </h1><p>{catid}</p>") #http://127.0.0.1:8000/cats/55/
def archive(request, year):
    if int(year) > 2021:
        # raise Http404
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1> Articles by years </h1><p>{year}</p>")
def pageNotFound(request, exception):
    return HttpResponseNotFound("Response not found")