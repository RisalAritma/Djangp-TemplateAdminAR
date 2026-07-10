# Di dalam file forms.py (buat file baru di folder aplikasi Anda jika belum ada)
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mengubah label tanpa mengubah nama field
        self.fields['username'].label = "Usaername"
        self.fields['username'].help_text = "Masukkan Username"
        self.fields['password1'].help_text = "Gunakan kombinasi huruf, angka, dan simbol untuk keamanan yang lebih baik."
        self.fields['password2'].help_text = "Ulangi password yang telah Anda masukkan."

