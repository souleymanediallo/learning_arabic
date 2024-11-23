from django.shortcuts import render
from learning.models import Tome


# Create your views here.
def home(request):
    tomes = Tome.objects.all()
    context = {'tomes': tomes}
    return render(request, 'pages/index.html', context)