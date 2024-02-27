from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic
from django.views import View
from .models import Comment


class UpdateCarView(generic.UpdateView):
    template_name = 'cars/update_car.html'
    form_class = forms.CarShopForm
    success_url = '/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarShop, id=car_id)

    def form_valid(self, form):
        return super(UpdateCarView, self).form_valid(form=form)


class DeleteCarView(generic.DeleteView):
    template_name = 'cars/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarShop, id=car_id)


class CreateCarView(generic.CreateView):
    template_name = 'cars/create_car.html'
    form_class = forms.CarShopForm
    success_url = '/'


class CarShopView(generic.ListView):
    template_name = 'cars/car_shop.html'
    context_object_name = 'car'
    model = models.CarShop

    def get_queryset(self):
        return self.model.objects.all()


class CarShopDetailView(generic.DetailView):
    template_name = 'cars/car_detail.html'
    context_object_name = 'car_id'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarShop, id=car_id)


class DeleteCommentView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        return render(request, 'confirm_delete_comment.html', {'comment': comment})

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('/')


class EditCommentView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        form = forms.CommentForm(instance=comment)
        return render(request, 'cars/edit_comment.html', {'form': form})

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        form = forms.CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'cars/edit_comment.html', {'form': form})


class AddCommentView(View):
    def get(self, request, id):
        car = get_object_or_404(models.CarShop, id=id)
        form = forms.CommentForm()
        return render(request, 'cars/add_comment.html', {'form': form, 'car': car})

    def post(self, request, id):
        car = get_object_or_404(models.CarShop, id=id)
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car_review = car
            comment.save()
            return redirect('/')
        return render(request, 'cars/add_comment.html', {'form': form, 'car': car})


class SearchView(generic.ListView):
    template_name = 'cars/car_shop.html'
    context_object_name = 'car'
    paginate_by = 5

    def get_queryset(self):
        return models.CarShop.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q")
        return context
