from django.contrib import admin
from .models import House

@admin.register(House) # admin 패널에 House라는 model을 등록
class HouseAdmin(admin.ModelAdmin):
	list_display = ( # 보여주고 싶은 column list를 적어준다. model의 property중에
        "name",
        "price_per_night",
        "address",
        "pets_allowed"
    )

	list_filter = ( # 어떤 컬럼으로 필터링 할지 적어준다.
        "price_per_night",
        "pets_allowed"
    )

	search_fields = ("address", ) # 검색하고자 하는 컬럼을 적어준다.