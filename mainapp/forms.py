from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Номер телефона', max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Сообщение')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError('Имя должно содержать минимум 3 символа.')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Удаляем все символы, кроме цифр
            phone = ''.join(filter(str.isdigit, phone))

            # Если номер не пустой и не начинается с 7, добавляем +7
            if len(phone) == 10 and not phone.startswith('7'):
                phone = '7' + phone  # Добавляем 7, если это номер без кода страны
            elif len(phone) < 10 or len(phone) > 11:
                raise forms.ValidationError('Номер телефона должен содержать 10 или 11 цифр.')

            # Добавляем код страны +7
            phone = '+7' + phone[-10:]  # Берем последние 10 цифр

        return phone


