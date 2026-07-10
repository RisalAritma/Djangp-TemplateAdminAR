from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect   

# from .models import Device, Data

@login_required
def dashboard(request):
    user = request.user
    
    context = {
        'user': user,
        'title': 'Dashboard',
    }
    return render(request, 'fakultas/dashboard.html', context)