from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms


def update_car_view(request, id):
    car_id = get_object_or_404(models.CarShop, id=id)
    if request.method == 'POST':
        form = forms.CarShopForm(request.POST, instance=car_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Успешно изменен в БД</h1> <a href="/">Все машины</a>')
    else:
        form = forms.CarShopForm(instance=car_id)
    return render(request, template_name='cars/update_car.html',
                  context={'form': form, 'car_id': car_id})


def delete_car_view(request, id):
    car_id = get_object_or_404(models.CarShop, id=id)
    car_id.delete()
    return HttpResponse('<h1>Успешно удален в БД</h1> <a href="/">Все машины</a>')


def create_car_view(request):
    if request.method == 'POST':
        form = forms.CarShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Успешно добавлен в БД</h1> <a href="/">Все машины</a>')
    else:
        form = forms.CarShopForm()
    return render(request, template_name='cars/create_car.html',
                  context={'form': form})


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


def add_comment_view(request, id):
    car = get_object_or_404(models.CarShop, id=id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car_review = car
            comment.save()
            return HttpResponse('<h1>Комментарий успешно добавлен</h1> <a href="/">Вернуться на главную</a>')
    else:
        form = forms.CommentForm()
    return render(request, template_name='cars/add_comment.html', context={'form': form, 'car': car})
