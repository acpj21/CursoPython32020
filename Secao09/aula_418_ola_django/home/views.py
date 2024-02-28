from django.shortcuts import render


def home(request):
    print('HOME')

    context = {
            'text': 'Olá home'
    }

    return render(
        request,
        'home/index.html',
        context
    )
