from django.shortcuts import render

def home(request):
  return render(request, 'adivina/home.html', {})

#def guess(request)