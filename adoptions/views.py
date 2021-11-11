from django.shortcuts import render,redirect
from django.http import Http404
from .models import Pet,Hash
from .forms import HashForm
import hashlib
from django.http import JsonResponse

def home(request):
    pets = Pet.objects.all()
    return render(request,'home.html',{'pets':pets,})

def pet_detail(request,pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request,'pet_detail.html',{'pet':pet,})


def hash_form(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=text_hash)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            return redirect('hash_display',hash=text_hash)
    form = HashForm()
    return render(request,'form.html',{'form':form,})


def hash_display(request,hash):
    try:
        hash_obj = Hash.objects.get(hash=hash)
        return render(request,'hash_display.html',{'hash':hash_obj,})
    except Hash.DoesNotExist:
        raise Http404('Hash not found')


def quickHash(request):
    text = request.GET['text']
    text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return JsonResponse({'hash':text_hash})