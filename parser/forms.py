from django import forms
from . import parser, models


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ("cinematica.com", "cinematica.com"),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    def parser_data(self):
        if self.cleaned_data['media_type'] == 'cinematica.com':
            film_parser = parser.parsing()
            for i in film_parser:
                models.ParserModel.objects.create(**i)
