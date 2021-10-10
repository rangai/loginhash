from django.contrib.auth.decorators import require_http_method
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

@require_http_method
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form':form})