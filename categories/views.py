# from django.http import JsonResponse
# from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category


@api_view()
def categories(request):
    # all_categories = Category.objects.all()
    # return JsonResponse(
    return Response(
        {
            "ok": True,
            # "categories": serializers.serialize("json", all_categories),
            "categories": Category.objects.all(),
        }
    )
