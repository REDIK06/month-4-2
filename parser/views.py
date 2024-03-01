from django.shortcuts import redirect
from django.views import generic
from . import models, parser, forms

class CinematicaListView(generic.ListView):
    model = models.ParserModel
    template_name = 'parser/cinematica_list.html'
    context_object_name = 'cinematica'

    def get_queryset(self):
        return models.ParserModel.objects.all()

class GetParsingForm(generic.FormView):
    template_name = "parser/cinematica_form.html"
    form_class = forms.ParserForm
    success_url = '/film_list/'

    def form_valid(self, form):
        form.parser_data()
        return super().form_valid(form)
