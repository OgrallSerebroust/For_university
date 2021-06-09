from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import TheatreForm, ShowsForm, VisitorForm
from .models import Theatre, Show, Visitor


def index(request):
    return render(request, "index.html")


def data_page(request):
    theatres = Theatre.objects.all()
    shows = Show.objects.all()
    visitors = Visitor.objects.all()
    return render(request, "data_page.html", {"theatres": theatres, "shows": shows, "visitors": visitors})


def insert_page(request):
    theatre_form, shows_form, visitors_form = TheatreForm(), ShowsForm(), VisitorForm()
    return render(request, "insert_page.html", {"theatre_form": theatre_form, "shows_form": shows_form, "visitors_form": visitors_form})


def add_theatres_data(request):
    if request.method == "POST":
        theatre = Theatre()
        theatre.name = request.POST.get("name")
        theatre.place = request.POST.get("place")
        theatre.save()
    return HttpResponseRedirect("/")


def add_shows_data(request):
    if request.method == "POST":
        show = Show()
        show.name = request.POST.get("name")
        show.visitors = request.POST.get("visitors")
        id_of_theatre = request.POST.get("theatre")
        theatre = get_object_or_404(Theatre, pk=id_of_theatre)
        show.theatre = theatre
        show.save()
    return HttpResponseRedirect("/")


def add_visitors_data(request):
    if request.method == "POST":
        visitor = Visitor()
        visitor.name = request.POST.get("name")
        visitor.age = request.POST.get("age")
        id_of_show = request.POST.get("show")
        show = get_object_or_404(Show, pk=id_of_show)
        visitor.show = show
        visitor.save()
    return HttpResponseRedirect("/")


def edit_theatre(request, id_theatre):
    theatre = get_object_or_404(Theatre, pk=id_theatre)
    if request.method == "POST":
        theatre.name = request.POST.get("name")
        theatre.place = request.POST.get("place")
        theatre.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "edit_theatre.html", {"theatre": theatre})


def edit_show(request, id_show):
    show = get_object_or_404(Show, pk=id_show)
    if request.method == "POST":
        show.name = request.POST.get("name")
        show.visitors = request.POST.get("visitors")
        theatre_from_show = request.POST.get("theatre")
        theatre = Theatre.objects.get(name=theatre_from_show)
        show.theatre = theatre
        show.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "edit_show.html", {"show": show})


def edit_visitor(request, id_visitor):
    visitor = get_object_or_404(Visitor, pk=id_visitor)
    if request.method == "POST":
        visitor.name = request.POST.get("name")
        visitor.age = request.POST.get("age")
        show_from_visitor = request.POST.get("show")
        show = Show.objects.get(name=show_from_visitor)
        visitor.show = show
        visitor.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "edit_visitor.html", {"visitor": visitor})


def delete_theatre(request, id_theatre):
    try:
        theatre = Theatre.objects.get(id=id_theatre)
        theatre.delete()
        return HttpResponseRedirect("/")
    except Theatre.DoesNotExist:
        return HttpResponseNotFound("<h2>Theatre not found</h2>")


def delete_show(request, id_show):
    try:
        show = Show.objects.get(id=id_show)
        show.delete()
        return HttpResponseRedirect("/")
    except Show.DoesNotExist:
        return HttpResponseNotFound("<h2>Show not found</h2>")


def delete_visitor(request, id_visitor):
    try:
        visitor = Visitor.objects.get(id=id_visitor)
        visitor.delete()
        return HttpResponseRedirect("/")
    except Visitor.DoesNotExist:
        return HttpResponseNotFound("<h2>Visitor not found</h2>")
