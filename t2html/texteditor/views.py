from django.shortcuts import render
from .models import Editor
from .forms import EditorForm
def index(request):
    form=EditorForm()
    return render(request,'texteditor/index.html',{'form':form})