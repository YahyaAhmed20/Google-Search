from django.shortcuts import render

# Create your views here.
def google(request):
    
    return render(request, 'google/google.html')


