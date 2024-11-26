from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html', {
        'firm_name': 'Юридическая Фирма "Право и Закон"',
        'services': ['Консультации', 'Судебное представительство', 'Документооборот'],
        'contact': {'email': 'info@lawfirm.com', 'phone': '+7 (123) 456-78-90'},
    })