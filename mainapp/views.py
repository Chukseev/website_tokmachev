from django.shortcuts import render
from .models import (WarehouseProcessing, MarketplaceRegistration, DeliveryFBO, DeliveryFBS, Storage, ContentCreation,
                     Promotion)


def index(request):
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
               'promotion_items': promotion_items}
    return render(request, 'mainapp/index.html', context)
