from django.contrib import admin

# Register your models here.
from .models import UserAdminFakultas, KodeSurat, NoSuratFakultas


admin.site.register(UserAdminFakultas)
admin.site.register(KodeSurat)
admin.site.register(NoSuratFakultas)
