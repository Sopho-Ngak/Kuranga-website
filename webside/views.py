from django.shortcuts import render
from webside.forms import CallbackForm
from base import send_email, TEAM_RECIPIENTS_EMAIL as our_team

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.cleaned_data['call_back_confirmation'] = False
            print(form.cleaned_data)
            send_email(
                subject="New Callback Request",
                context=form.cleaned_data,
                to=our_team
            )
            form.cleaned_data['call_back_confirmation'] = True
            send_email(
                subject="Thank you for your request",
                context=form.cleaned_data,
                to=[form.cleaned_data['email']]
            )
            form = CallbackForm()
            return render(request, 'index.html', {'form': form, 'success': True})
    form = CallbackForm()

    return render(request, 'index.html', context={'form': form})

def about(request):
    return render(request, 'about.html')

def services(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.cleaned_data['call_back_confirmation'] = False
            print(form.cleaned_data)
            send_email(
                subject="New Callback Request",
                context=form.cleaned_data,
                to=our_team
            )
            form.cleaned_data['call_back_confirmation'] = True
            send_email(
                subject="Thank you for your request",
                context=form.cleaned_data,
                to=[form.cleaned_data['email']]
            )
            form = CallbackForm()
            return render(request, 'services.html', {'form': form, 'success': True})
    form = CallbackForm()
    return render(request, 'services.html', context={'form': form})

def contact(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.cleaned_data['call_back_confirmation'] = False
            print(form.cleaned_data)
            send_email(
                subject="New Callback Request",
                context=form.cleaned_data,
                to=our_team
            )
            form.cleaned_data['call_back_confirmation'] = True
            send_email(
                subject="Thank you for your request",
                context=form.cleaned_data,
                to=[form.cleaned_data['email']]
            )
            form = CallbackForm()
            return render(request, 'contact.html', {'form': form, 'success': True})
    form = CallbackForm()
    return render(request, 'contact.html', context={'form': form})

def one_page(request):
    return render(request, 'one-page.html')

def our_programs(request):
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.cleaned_data['call_back_confirmation'] = False
            print(form.cleaned_data)
            send_email(
                subject="New Callback Request",
                context=form.cleaned_data,
                to=our_team
            )
            form.cleaned_data['call_back_confirmation'] = True
            send_email(
                subject="Thank you for your request",
                context=form.cleaned_data,
                to=[form.cleaned_data['email']]
            )
            form = CallbackForm()
            return render(request, 'our-programs.html', {'form': form, 'success': True})
    form = CallbackForm()
    return render(request, 'our-programs.html', context={'form': form})


