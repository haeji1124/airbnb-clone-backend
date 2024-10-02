from django.contrib import admin
from .models import House

@admin.register(House) # admin 패널에 House라는 model을 등록
class HouseAdmin(admin.ModelAdmin):
    list_display = ("name", "price_per_night", "address", "pets_allowed")
    list_filter = ("price_per_night", "pets_allowed")