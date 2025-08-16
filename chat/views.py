from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')  # рядок з ім’ям шаблону у лапках
