from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect   

# from .models import Device, Data

@login_required
def dashboard(request):
    user = request.user
    
    if user.last_name == 'Admin Fakultas':
        redirect_url = 'app:dashboard_fakultas'  # Ganti dengan URL yang sesuai untuk dashboard admin fakultas
    elif user.last_name == 'Admin Jurusan':
        redirect_url = 'app:dashboard_jurusan'  # Ganti dengan URL yang sesuai untuk dashboard admin jurusan
    elif user.last_name == 'Dosen':
        redirect_url = 'app:dashboard_dosen'  # Ganti dengan URL yang sesuai untuk dashboard dosen
    elif user.last_name == 'Mahasiswa':
        redirect_url = 'app:dashboard_mhs'  # Ganti dengan URL yang sesuai untuk dashboard mahasiswa
    else:
        redirect_url = 'app:dashboard_blank'  # Ganti dengan URL yang sesuai untuk dashboard default atau halaman kosong

    return redirect(redirect_url)   