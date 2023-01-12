from django.contrib import admin
from portofolio.models import *

# Register your models here.

class FotoAdmin(admin.ModelAdmin):
    list_display = ['judul', 'keterangan']
    search_fields = ['judul', 'keterangan']
    list_per_page = 4


admin.site.register(Foto, FotoAdmin)