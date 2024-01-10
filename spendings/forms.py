from django.forms import ModelForm
from .models import Categories, PersonalSpending

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['categoryName'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Categories
        fields = ['categoryName']

class PersonalSpendingForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Categories.objects.filter(user=user)
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['note'].widget.attrs.update({'class': 'form-control'})
        self.fields['spendingAmount'].widget.attrs.update({'class': 'form-control'})
        self.fields['spendingDate'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = PersonalSpending
        fields = ['category', 'note', 'spendingAmount', 'spendingDate']