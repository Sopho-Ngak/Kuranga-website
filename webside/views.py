from django.shortcuts import render
from webside.forms import CallbackForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            return render(request, 'index.html', {'form': form, 'success': True})
    else:
        form = CallbackForm()

    print(form['name'].value())
    
    return render(request, 'index.html', context={'form': form})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def one_page(request):
    return render(request, 'one-page.html')


