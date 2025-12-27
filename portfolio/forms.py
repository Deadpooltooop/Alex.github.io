from django import forms
from .models import Order
from .models import ContactMessage

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_name', 'user_email', 'description']
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'user_email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'description': forms.Textarea(attrs={'placeholder': 'Описание заказа, размер, стиль'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']  # Укажите нужные поля
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }        
