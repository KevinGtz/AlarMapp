from django.shortcuts import render
from .forms import registro
from .models import User

def registrar(request):
	form = registro() 
	if request.method == 'GET':
		return render(request, 'AlarmApp/login.html', {'form': form}) 
	return render(request, 'AlarmApp/login.html', {'form': form}) 

# Create your views here.
