from django.shortcuts import render


def ime_bot(request):
    return render(request, 'Ibot.html')


def get(request):
    return render(request, 'select.html')

def whatsapp(request):
    return render(request, 'whatsappbulk.html')
