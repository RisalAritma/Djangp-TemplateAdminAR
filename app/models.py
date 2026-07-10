from django.db import models
from django.contrib.auth.models import User


class UserAdminFakultas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username
    
# NOMOR SURAT FAKULTAS
    
class KodeSurat(models.Model):
    id = models.AutoField(primary_key=True)
    jenis = models.CharField(max_length=100, blank=False, null=False)
    kode = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return f"{self.jenis} - {self.kode}"
    

class NoSuratFakultas(models.Model):
    id = models.AutoField(primary_key=True)
    date_in = models.DateTimeField(auto_now_add=True)
    adminp = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="nosuratf_admin")
    tahun = models.CharField(max_length=5, blank=False, null=False)
    nomor = models.IntegerField(blank=False, null=False)
    perihal = models.CharField(max_length=255, blank=False, null=False)
    tujuan = models.CharField(max_length=255, blank=False, null=False)
    kode = models.CharField(max_length=50, blank=False, null=False)
    def __str__(self):
        return f"{self.nomor}/{self.kode}/{self.tahun}"