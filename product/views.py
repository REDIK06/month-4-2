from django.views import generic
from . import models


class WomenClothView(generic.ListView):
    template_name = 'product/women_cloth.html'
    context_object_name = 'women_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tag__name='Женская одежда').order_by('-id')


class MenClothView(generic.ListView):
    template_name = 'product/men_cloth.html'
    context_object_name = 'men_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tag__name='Мужская одежда').order_by('-id')


class KidsClothView(generic.ListView):
    template_name = 'product/kids_cloth.html'
    context_object_name = 'kids_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tag__name='Детская одежда').order_by('-id')



# from django.shortcuts import render
# from django.views import View
# from .models import Cloth
#
# class WomenClothView(View):
#     def get(self, request):
#         women_clothes = Cloth.objects.filter(gender='F')
#         return render(request, 'women_cloth.html', {'clothes': women_clothes})
#
# class MenClothView(View):
#     def get(self, request):
#         men_clothes = Cloth.objects.filter(gender='M')
#         return render(request, 'men_cloth.html', {'clothes': men_clothes})
#
# class KidsClothView(View):
#     def get(self, request):
#         kids_clothes = Cloth.objects.filter(gender='K')
#         return render(request, 'kids_cloth.html', {'clothes': kids_clothes})
