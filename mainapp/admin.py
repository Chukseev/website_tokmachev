from django.contrib import admin
from .models import WarehouseProcessing, MarketplaceRegistration, DeliveryFBO, DeliveryFBS, Storage, ContentCreation, Promotion

admin.site.register(WarehouseProcessing)
admin.site.register(MarketplaceRegistration)
admin.site.register(DeliveryFBS)
admin.site.register(DeliveryFBO)
admin.site.register(Storage)
admin.site.register(ContentCreation)
admin.site.register(Promotion)

