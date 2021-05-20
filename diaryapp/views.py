# from likelion_week6.diary import diaryapp
from django.shortcuts import get_object_or_404, render, redirect
from .models import Diaryapp

# Create your views here.
def home(request):
    number = Diaryapp.objects.count
    return render(request, 'home.html')

def content(request):
    diaries = Diaryapp.objects.all()
    return render(request, 'content.html', {'diaries':diaries})
    

def detail(request, id):
    diaryapp = get_object_or_404(Diaryapp, pk = id)
    return render(request, 'detail.html', {'diaryapp':diaryapp})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_diary = Diaryapp()
    new_diary.title = request.POST['title']
    new_diary.body = request.POST['body']
    new_diary.save()
    return redirect('detail', new_diary.id)

def edit(request, id):
    edit_diary = Diaryapp.objects.get(id=id)
    return render(request, 'edit.html', {'diaryapp': edit_diary})

def update(request, id):
    update_diary =  Diaryapp.objects.get(id=id)
    update_diary.title = request.POST['title']
    update_diary.body = request.POST['body']
    update_diary.save()
    return redirect('detail', update_diary.id)

def delete(request, id):
    delete_diary =  Diaryapp.objects.get(id=id)
    delete_diary.delete()
    return redirect('content')



