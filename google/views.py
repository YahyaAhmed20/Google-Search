from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def google(request):
    
    return render(request, 'google/google.html')
def home_view(request):
    return render(request, 'google/home.html')

@login_required
def gmail_view(request):
    # Example user-specific data
    user_data = {'emails': ['Welcome to Gmail!', 'New login from Chrome']}
    return render(request, 'google/gmail.html', user_data)

@login_required
def images_view(request):
    # Example user-specific data
    user_data = {'images': ['img1.jpg', 'img2.jpg']}
    return render(request, 'google/images.html', user_data)