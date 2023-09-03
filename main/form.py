
from django import forms

from .models import Filter

class FilterForm(forms.ModelForm):

    class Meta:
        model = Filter
        fields = "__all__"
        widgets = {
            'slug': forms.HiddenInput(),
            'key_word': forms.TextInput(attrs={'required':'required'}),
            'content': forms.Textarea(attrs={'required':'required'}),
            'search_type': forms.RadioSelect(attrs={'required':'required'}),
            'search_behavior': forms.RadioSelect(attrs={'required':'required'}),
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for field in self.fields:
            ctx = {
                'placeholder': self.fields[field].label or field.title(),
            }
            self.fields[field].label = ''
            if not field in ['slug']:
                self.fields[field].widget.attrs.update(ctx)


        self.fields['key_word'].widget.attrs.update({
            'class': 'key-input-f',
            'placeholder': 'Looking For...',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'content-area'
        })

        self.fields['num_keys'].widget.attrs.update({
            'placeholder': 'Custom search',
            'min':'0',
            'max':'10000'
        })


        search_choices = self.fields['search_type'].choices
        custom_ids = [f"id_{value}" for value, _ in search_choices]

        self.fields['search_type'].widget = CustomRadioSelect(custom_ids=custom_ids, choices=search_choices)

class CustomRadioSelect(forms.RadioSelect):
    def __init__(self, custom_ids=None,  *args, **kwargs):
        self.custom_ids = custom_ids
        super().__init__(*args, **kwargs)

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        if self.custom_ids is not None:
            option['attrs']['id'] = self.custom_ids[index]
        return option
