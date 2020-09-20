from django.shortcuts import render
from django.utils import timezone
from polls.models import Todo


def home(request):
    return render(request, 'main/index.html')
 
def todo(request):
    # print(request.POST.get('todo'))
    current_date = timezone.now()
    content = request.POST["todo"]
    # print(added_date)
    # print(content)
    created_obj =  Todo.objects.create(added_date= current_date, text= content)
    return render(request, 'main/index.html')