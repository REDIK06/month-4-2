from django.shortcuts import render, get_object_or_404
from . import models


def car_shop_view(request):
    if request.method == 'GET':
        car = models.CarShop.objects.all()
        return render(request, template_name='cars/car_shop.html',
                      context={'car': car})


def car_shop_detail_view(request, id):
    if request.method == 'GET':
        car_id = get_object_or_404(models.CarShop, id=id)
        return render(request, template_name='cars/car_detail.html',
                      context={'car_id': car_id})


