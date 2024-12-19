from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VisitorFeedbackForm

def feedback_form(request):
    if request.method == 'POST':
        form = VisitorFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('feedback_form')  # Assuming you have a 'thank_you' page configured.

    else:
        form = VisitorFeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def form(request):
    return render(request, 'home.html')
