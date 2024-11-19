from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/')  # Redirect to your home page
    else:
        form = SignupForm()
    return render(request, 'signup/signup.html', {'form': form})
