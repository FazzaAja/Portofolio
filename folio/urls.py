from django.contrib import admin
from django.urls import path
from portofolio.views import *
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dash, name='dash'),
    path('tambah-foto/', tambah_foto, name='tambah-foto'),
    path('', index),
    path('foto/ubah/<int:id_foto>', ubah_foto, name='ubah_foto'),
    path('foto/hapus/<int:id_foto>', hapus_foto, name="hapus_foto" ),
    path('masuk/', LoginView.as_view(), name='masuk' ),
    path('keluar/', LogoutView.as_view(next_page='/'), name='keluar' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)