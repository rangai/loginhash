import hashlib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from myhash.models import Myhash
from myhash.forms import MyhashForm

def top(request):
    myhash = Myhash.objects.all()
    context = {"myhash": myhash}
    return render(request, "myhash/top.html", context)

@login_required
def hash_new(request):
    if request.method == 'POST':
        form = MyhashForm(request.POST)
        if form.is_valid():
            myhash = form.save(commit=False)
            myhash.hsh = hashlib.sha256(myhash.msg.encode()).hexdigest() 
            myhash.save()
            return redirect(top)
    else:
        form = MyhashForm()
    return render(request, "myhash/myhash_new.html", {'form':form})