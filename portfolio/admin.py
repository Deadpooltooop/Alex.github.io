from django.contrib import admin
from .models import PortfolioWork, Order, SocialLink, Page

# Регистрация моделей в админ-панели
admin.site.register(PortfolioWork)
admin.site.register(Order)
admin.site.register(SocialLink)
admin.site.register(Page)
