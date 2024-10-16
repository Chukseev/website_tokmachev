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
     # 1. Складская обработка
    warehouse_processing = WarehouseProcessing.objects.all()
    warehouse_processing_data = {
        'table_title': 'СКЛАДСКАЯ ОБРАБОТКА',
        'table_headers': ['Услуга', 'Стоимость', 'Единица измерения'],
        'table_rows': [
            [service.service_name, f"{service.price} руб", service.unit]
            for service in warehouse_processing
        ]
    }

    # 2. Регистрация на маркетплейсах
    marketplace_registrations = MarketplaceRegistration.objects.all()
    marketplace_registration_data = {
        'table_title': 'РЕГИСТРАЦИЯ НА МАРКЕТПЛЕЙСАХ',
        'table_headers': ['Маркетплейс', 'Стоимость регистрации', 'Стоимость SKU', 'Доп. опции',
                            'Стоимость доставки'],
        'table_rows': [
            [
                registration.marketplace_name,
                f"{registration.registration_fee} руб",
                f"{registration.sku_fee} руб",
                f"{registration.additional_option_fee} руб",
                f"{registration.delivery_fee_per_position} руб"
            ]
            for registration in marketplace_registrations
        ]
    }

    # 3. Доставка по схеме FBO
    deliveries_fbo = DeliveryFBO.objects.all()
    delivery_fbo_data = {
        'table_title': 'ДОСТАВКА ПО СХЕМЕ FBO',
        'table_headers': ['Маркетплейс', 'Локация', 'Стоимость за куб.м', 'Стоимость за поддон',
                            'Стоимость за 6 поддонов', 'Стоимость за 15 поддонов'],
        'table_rows': [
            [
                delivery.marketplace_name,
                delivery.location,
                f"{delivery.price_per_cubic_meter} руб" if delivery.price_per_cubic_meter else '-',
                f"{delivery.price_per_pallet} руб" if delivery.price_per_pallet else '-',
                f"{delivery.price_per_6_pallets} руб" if delivery.price_per_6_pallets else '-',
                f"{delivery.price_per_15_pallets} руб" if delivery.price_per_15_pallets else '-'
            ]
            for delivery in deliveries_fbo
        ]
    }

    # 4. Доставка по схеме FBS
    deliveries_fbs = DeliveryFBS.objects.all()
    delivery_fbs_data = {
        'table_title': 'ДОСТАВКА ПО СХЕМЕ FBS',
        'table_headers': ['Маркетплейс', 'Стоимость маленькой посылки', 'Стоимость средней посылки',
                            'Стоимость большой посылки'],
        'table_rows': [
            [
                delivery.marketplace_name,
                f"{delivery.small_package_price} руб",
                f"{delivery.medium_package_price} руб",
                f"{delivery.large_package_price} руб"
            ]
            for delivery in deliveries_fbs
        ]
    }

    # 5. Хранение
    storages = Storage.objects.all()
    storage_data = {
        'table_title': 'ХРАНЕНИЕ',
        'table_headers': ['Тип товара', 'Бесплатные дни хранения', 'Стоимость за день'],
        'table_rows': [
            [
                storage.item_type,
                f"{storage.free_storage_days} дн.",
                f"{storage.price_per_day} руб/дн."
            ]
            for storage in storages
        ]
    }

    # 6. Создание контента
    content_creations = ContentCreation.objects.all()
    content_creation_data = {
        'table_title': 'СОЗДАНИЕ КОНТЕНТА',
        'table_headers': ['Услуга', 'Стоимость', 'Единица измерения'],
        'table_rows': [
            [content.service_name, f"{content.price} руб", content.unit]
            for content in content_creations
        ]
        }

    # 7. Продвижение
    promotions = Promotion.objects.all()
    promotion_data = {
        'table_title': 'ПРОДВИЖЕНИЕ',
        'table_headers': ['Услуга', 'Стоимость'],
        'table_rows': [
            [promotion.service_name, f"{promotion.price} руб"]
            for promotion in promotions
        ]
    }
    context = {
        'form': form,
        'tables' : [
            warehouse_processing_data,
            marketplace_registration_data,
            delivery_fbo_data,
            delivery_fbs_data,
            storage_data,
            content_creation_data,
            promotion_data
        ]
    }
    return render(request, 'mainapp/index.html', context)
