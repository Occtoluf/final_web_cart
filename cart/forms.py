from django import forms
from cart.models import ContactInformation


class ContactInformationForm(forms.ModelForm):
    """ Контактная информация """

    CHOICES = [('card', 'Оплата картой'), ('cash', 'Наличными при получении')]
    pay_method = forms.CharField(label='Способ оплаты', widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = ContactInformation
        fields = ['name', 'surname', 'patronymic', 'country', 'address', 'phone', 'email', 'additional']

        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'placeholder': 'Введите имя'
                },
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'placeholder': 'Введите фамилию'
                }
            ),
            'patronymic': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'placeholder': 'Введите отчество'
                }
            ),
            'country':  forms.Select(
                    attrs={'class': 'form-control my-3 p-4'}
                ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'placeholder': 'Введите адрес'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'placeholder': 'Введите номер телефона'
                }
            ),

            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'placeholder': 'Введите email'
                }
            ),

            'additional': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите дополнительную информацию'
                }
            ),
        }