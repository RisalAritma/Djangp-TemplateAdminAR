from django.contrib import messages

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
    return render(request, 'app/dashboard.html', context)


@login_required
def alert(request):
    user = request.user

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "success":
            messages.success(request, "Data berhasil disimpan.")

        elif action == "danger":
            messages.error(request, "Terjadi kesalahan saat menyimpan data.")

        elif action == "warning":
            messages.warning(request, "Periksa kembali data yang Anda masukkan.")

        elif action == "info":
            messages.info(request, "Ini adalah pesan informasi.")
    
    context = {
        'user': user,
        'title': 'Alert',
    }
    return render(request, 'app/alert.html', context)   



@login_required
def button(request):
    user = request.user
    
    context = {
        'user': user,
        'title': 'Button',
    }
    return render(request, 'app/button.html', context)   

@login_required
def table(request):
    user = request.user
    
    context = {
        'user': user,
        'title': 'Table',
    }
    return render(request, 'app/table.html', context)   


@login_required
def icon(request):
    user = request.user
    
    context = {
        'user': user,
        'title': 'Icon',
    }
    return render(request, 'app/icon.html', context)   
