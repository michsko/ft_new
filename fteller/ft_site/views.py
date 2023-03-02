from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Event, User, ProductionTheater, ProductionStandup
from .forms import EventForm
# Create your views here.


def about(request):
	return render(request, "site/about.html", {})


def add_event(request):
	form = EventForm(request.POST)
	return render(request, 'site/add_event.html', 
		{'form': form, })

def divadlo(request):
	production = ProductionTheater.objects.all()
	return render(request, 'site/divadlo.html', {'production': production,})


def event_delete(request, event_id):
	event = Event.objects.get(pk=event_id)
	event.delete()
	messages.success(request, ('Váš event byl vymazán. Ach jo..'))
	return redirect('program')


def event_update(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		messages.success(request, ('Váš event byl změněn. Good luck.'))
		return redirect('program')

	return render(request, 'site/program_update.html', {'form': form,
		'event': event,})

def film(request):
	return render(request, 'site/film.html', {})


def foto(request):
	return render(request, "site/foto.html", {})
   

def kontakt(request):
	return render(request, 'site/kontakt.html', {})


def home(request):
	return render(request, 'site/home.html', {})

def moderation(request):
	return render(request, 'site/moderation.html', {})

def program(request):
	program = Event.objects.all().order_by('date')
	return render(request, 'site/program.html', {'program': program, })


def program_add(request):
	submitted = False
	if request.method == 'POST': 
		form = EventForm(request.POST)
		if form.is_valid():
			event = form.save()
			messages.success(request, ('Přidali jste event do programu.'))
			return redirect('program')
	else: 
		form = EventForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'site/program_add.html', {'form': form, 
		'submitted': submitted,})


def standup(request):
	production = ProductionStandup.objects.all()
	return render(request, 'site/standup.html', {'production': production,})


def work(request):
	return render(request, 'site/work.html', {})