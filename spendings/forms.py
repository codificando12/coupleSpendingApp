from django.forms import ModelForm
from .models import Categories

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['categoryName'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Categories
        fields = ['categoryName']