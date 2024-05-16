from django import forms
from catalog.models import Product

valid_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.initial:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'category', 'price', 'image', 'description')
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