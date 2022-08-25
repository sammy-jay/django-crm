from django import forms
from .models import Lead

# class LeadForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField(min_value=0)


styles = 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': styles}),
            'last_name': forms.TextInput(attrs={'class': styles}),
            'age': forms.NumberInput(attrs={'class': styles}),
            'description': forms.Textarea(attrs={'class': f"{styles} h-20"}),
            'agent': forms.Select(attrs={'class': f"{styles} py-2.5"}),
        }

    