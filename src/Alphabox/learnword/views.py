from django.shortcuts import render
from django.http import JsonResponse
from nltk.corpus import wordnet
from string import ascii_lowercase

# nltk.download('wordnet')
def index(request):
    var = ''
    w = ''
    if request.method == 'POST':
        w = request.POST.get('mot')
        try:
            a = wordnet.synsets(w)[0]
            var = 'correct'
        except IndexError:
            var = 'incorrect'
    return render(request, 'learnword/index.html', {'var': var, 'mot': w})

def modules(request):
    return render(request, 'learnword/alphabox_module.html')

def play(request):
    request.session['mot_trouve'] = 0
    return render(request, 'learnword/paly_test.html', {'alphabet': ascii_lowercase})


def index_setting(request):
    request.session['mot_trouve'] = 0
    return render(request, 'learnword/settings.html', {'alphabet': ascii_lowercase})


def validate_word(request):
    if request.method == "POST":
        w = request.POST.get('mot', None)
        correct = True
        try:
            a = str(wordnet.synsets(w)[0])
            if w[0] != request.session["lettre"]:
                correct = False
            else:
                request.session['mot_trouve'] += 1

        except IndexError:
            correct = False
        data = {
            'mot': w,
            'correct': correct,
        }
        print(request.session['mot_trouve'])
        return JsonResponse(data)


def create_session(request):
    if request.method == 'POST':
        request.session[request.POST.get('nom')] = request.POST.get('contenu', None)
        return get_session(request)


def get_session(request):
    if request.method == 'POST':
        data = {
            request.POST.get('nom') : request.session[request.POST.get('nom')]
        }
        return JsonResponse(data)