from django.shortcuts import render, redirect
from portofolio.models import *
from portofolio.forms import FormFoto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings



def index(req):
    
    fotos = Foto.objects.all()

    konteks = {
        'fotos' : fotos
    }

    return render(req, 'index.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def dash(req):
    fotos = Foto.objects.all()

    konteks = {
        'fotos' : fotos
    }

    return render(req, 'dash.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_foto(request):
    if request.POST:
        form = FormFoto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormFoto()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return redirect('dash')
    else:
        form = FormFoto()

        konteks = {
            'form' : form,
        }

    return render(request, 'tambah-foto.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def ubah_foto(request, id_foto):
    foto = Foto.objects.get(id=id_foto)
    template = 'ubah-foto.html'
    if request.POST:
        form = FormFoto(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save() 
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('/dashboard', id_foto=id_foto)
    else:
        form = FormFoto(instance=foto)
        konteks = {
            'form' : form,
            'foto' : foto,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_foto(request, id_foto):
    foto = Foto.objects.filter(id=id_foto)
    foto.delete()

    return redirect('dash')

