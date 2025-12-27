from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import  render, redirect
from django.contrib import messages
from .models import Page
from .forms import ContactForm
from .forms import OrderForm
from .models import PortfolioWork, Order

@staff_member_required  # Доступ только для админов
def admin_dashboard(request):
    context = {
        'recent_works': PortfolioWork.objects.order_by('-created_at')[:5],
        'pending_orders': Order.objects.filter(status='pending').count(),
        'total_works': PortfolioWork.objects.count(),
    }
    return render(request, 'admin/dashboard.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    try:
        page = Page.objects.get(slug='about')
    except Page.DoesNotExist:
        page = None

    return render(request, 'about.html', {'page': page})


def portfolio(request):
    works = PortfolioWork.objects.all()  # Получаем все работы
    return render(request, 'portfolio.html', {'works': works})

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заказ успешно отправлен!')
            return redirect('order')  # Редирект на ту же страницу
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})