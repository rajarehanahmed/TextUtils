from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('<h1>Rehan</h1> <p><a href="https://www.youtube.com/">YouTube</a></p> <p><a href="https://www.google.com/">Google</a></p> <p><a href="https://www.wikipedia.com/">Wikipedia</a></p> <p><a href="https://www.facebook.com/">Facebook</a></p>')


def analyze(request):
    # Get the Text
    djText = request.POST.get('text', 'default')
    # Check the Checkboxes
    remPunc = request.POST.get('removePunc', 'off')
    fullCaps = request.POST.get('fullCaps', 'off')
    remNewLine = request.POST.get('removeNewLine', 'off')
    remSpace = request.POST.get('removeExtraSpace', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = djText
    # Check if isPunc is on or off
    if remPunc == "on":
        temp = analyzed
        analyzed = ""
        for char in temp:
            if char not in punctuations:
                analyzed = analyzed + char
    # Check if fullCaps is on or off
    if fullCaps == 'on':
        temp = analyzed
        analyzed = ""
        for char in temp:
            analyzed = analyzed + char.upper()
    # Check if remNewLine is on or off
    if remNewLine == 'on':
        temp = analyzed
        analyzed = ""
        for char in temp:
            if char != '\n':
                analyzed = analyzed + char
    # Check if removeSpace is on of off
    if remSpace == 'on':
        temp = analyzed
        analyzed = ""
        for index, char in enumerate(temp):
            if not (temp[index] == ' ' and temp[index + 1] == ' '):
                analyzed = analyzed + char

    length = len(analyzed)
    param = {
        'purpose': 'Removed Punctuations',
        'analyzed_text': analyzed,
        'text_length': length
    }
    return render(request, 'analyze.html', param)