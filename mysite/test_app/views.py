from django.shortcuts import render
from .forms import QuestionForm, ChoiceForm

"""
def index(request):
	return HttpResponse('Welcome to your first view!')

"""
def creat_Question(request):
	if request.model == 'POST':
		form = QuestionForm(request.POST)
		if form.is.valid():
			access_object = form.save()
			quantity = form.cleaned_data['quantity']
		
