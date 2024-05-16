from django import forms
from blog.models import Publication
from catalog.forms import valid_list, StyleFormMixin


class PublicationForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Publication
        # fields = '__all__'
        fields = ('name', 'description', 'image', 'publication_activ', 'counter')
        # exclude = ('name')

    def clean_name(self):
        cleaned_data: str = self.cleaned_data['name']

        for word in valid_list:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Название не прошло валидацию')

        return cleaned_data

    def clean_description(self):
        cleaned_data: str = self.cleaned_data['description']

        for word in valid_list:
            if word.lower() in cleaned_data.lower():
                raise forms.ValidationError('Описание не прошло валидацию')

        return cleaned_data
