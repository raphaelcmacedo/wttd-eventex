from django.shortcuts import render


def home(request):
    speakers = [
        {'name':'Grace Hoper', 'photo':'http://hbn.link/hopper-pic'},
        {'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'},
    ]
    return render(request, 'index.html', context={'speakers':speakers})
