"""
URL configuration for aam project.
"""
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView, CreateView
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Import form custom Anda
from aam.form import CustomUserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Fitur Register (Diletakkan di atas agar prioritas utama)
    path('accounts/register/', type('CustomRegisterView', (SuccessMessageMixin, CreateView), {
        'template_name': 'registration/register.html',
        'form_class': CustomUserCreationForm,
        'success_url': reverse_lazy('login'),
        'success_message': "Akun berhasil dibuat! Silakan masuk."
    }).as_view(), name='register'),

    # 2. Fitur Login dengan Notifikasi (Penting: override LoginView bawaan)
    path('accounts/login/', type('CustomLoginView', (SuccessMessageMixin, auth_views.LoginView), {
        'redirect_authenticated_user': True,
        'success_message': "Selamat datang kembali! Anda berhasil masuk.",
        # Logika khusus agar SuccessMessageMixin bekerja pada LoginView
        'get_success_message': lambda self, cleaned_data: self.success_message,
    }).as_view(), name='login'),

    # 3. URL Auth bawaan (Diletakkan di bawah agar tidak menimpa custom login/register)
    path('accounts/', include('django.contrib.auth.urls')),

    # 4. URL Utama
    path('', RedirectView.as_view(url='app/dashboard/', permanent=True)),
    path('app/', include('app.urls')),
]