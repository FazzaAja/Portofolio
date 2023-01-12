
from django.contrib import admin
from django.urls import path
from portofolio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dash, name='dash'),
    path('tambah-foto/', tambah_foto, name='tambah-foto'),
    path('', index),
    path('foto/ubah/<int:id_foto>', ubah_foto, name='ubah_foto'),
    path('foto/hapus/<int:id_foto>', hapus_foto, name="hapus_foto" ),
]
