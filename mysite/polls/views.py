from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Data
from django.template import loader
from django.shortcuts import render,get_object_or_404
import datetime
from django.utils import timezone
from django.http import FileResponse, JsonResponse
import json

# Create your views here.

def index(request):
	
	return render(request, 'polls/index2.html')

def test(request):
	print 'Ah'
	response = JsonResponse({"id": 1,
							"text": "I am from Twitter",
							"time" : "",
							"lon": 45,
							"lat": -75})
	return response

def result(request):
	print 'ha'
	response = FileResponse(open('polls/result.json','rb'))
	return response

def detail(request, question_id):
	
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	print "oh"
	response = "You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on question %s." %question_id)

def jquery(request):
	return FileResponse(open('polls/jquery-1.7.2.js','rb'))

def css(request):
	return FileResponse(open('polls/bootstrap.min.css','rb'))

def eventsource(request):
	return FileResponse(open('polls/jquery.eventsource.js','rb'))

def marker(request):
	return FileResponse(open('polls/markerclusterer.js','rb'))

