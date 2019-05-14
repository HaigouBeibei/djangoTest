from django.http import HttpResponse
from django.shortcuts import render
from  .forms  import AddFrom
def index(request):
    if request.method == 'POST':
        form = AddFrom(request.POST)
        if  form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form  = AddFrom()
    return render(request, 'index.html',{'form':form})
    
# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     a = int(a)
#     b = int(b)
#     return HttpResponse(str(a+b))