from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def landing(request):
    form = ProfileForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data
        newform = form.save()
        print(data)
    return render(request, 'landing/index.html', locals())