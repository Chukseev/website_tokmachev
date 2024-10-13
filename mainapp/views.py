from django.shortcuts import render
from .models import (WarehouseProcessing, MarketplaceRegistration, DeliveryFBO, DeliveryFBS, Storage, ContentCreation,
                     Promotion)
from .forms import ContactForm
from .telegram_bot import send_telegram_message


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы, например, отправка email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Логика обработки формы
            status = send_telegram_message(name, email, message)

            if status == 200:
                # Сообщение успешно отправлено
                return render(request, 'mainapp/thanks.html', {'name': name})
            else:
                # Произошла ошибка при отправке сообщения
                return render(request, 'contact.html', {'form': form, 'error': 'Failed to send message to Telegram'})
    else:
        form = ContactForm()
    warehouse_processing_items = WarehouseProcessing.objects.all()
    marketplace_registration_items = MarketplaceRegistration.objects.all()
    delivery_fbo_items = DeliveryFBO.objects.all()
    delivery_fbs_items = DeliveryFBS.objects.all()
    storage_items = Storage.objects.all()
    content_creation_items = ContentCreation.objects.all()
    promotion_items = Promotion.objects.all()
    context = {'warehouse_processing_items': warehouse_processing_items,
               'marketplace_registration_items': marketplace_registration_items,
               'delivery_fbo_items': delivery_fbo_items,
               'delivery_fbs_items': delivery_fbs_items,
               'storage_items': storage_items,
               'content_creation_items': content_creation_items,
               'promotion_items': promotion_items,
               'form': form}
    return render(request, 'mainapp/index.html', context)
