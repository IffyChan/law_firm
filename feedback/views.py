from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Здесь можно обработать данные, например, отправить письмо
            return render(request, 'feedback/success.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': form})
