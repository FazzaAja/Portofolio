from django.shortcuts import render, redirect
from portofolio.models import *
from portofolio.forms import FormFoto
from django.contrib import messages

def ubah_foto(request, id_foto):
    foto = Foto.objects.get(id=id_foto)
    template = 'ubah-foto.html'
    if request.POST:
        form = FormFoto(request.POST, instance=foto)
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


# Create your views here.
def hapus_foto(request, id_foto):
    foto = Foto.objects.filter(id=id_foto)
    foto.delete()

    return redirect('dash')

def dash(req):
    fotos = Foto.objects.all()

    konteks = {
        'fotos' : fotos
    }

    return render(req, 'dash.html', konteks)


def tambah_foto(request):
    if request.POST:
        form = FormFoto(request.POST)
        if form.is_valid():
            form.save()
            form = FormFoto()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-foto.html', konteks)
    else:
        form = FormFoto()

        konteks = {
            'form' : form,
        }

    return render(request, 'tambah-foto.html', konteks)

def index(req):
    return render(req, 'index.html')