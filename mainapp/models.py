from django.db import models

# 1. Модель для складской обработки
class WarehouseProcessing(models.Model):
    service_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Складская обработка"
        verbose_name_plural = "Складская обработка"


# 2. Модель для регистрации на маркетплейсах
class MarketplaceRegistration(models.Model):
    marketplace_name = models.CharField(max_length=255)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
    sku_fee = models.DecimalField(max_digits=10, decimal_places=2)
    additional_option_fee = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_fee_per_position = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.marketplace_name

    class Meta:
        verbose_name = "Регистрация на маркетплейсах"
        verbose_name_plural = "Регистрация на маркетплейсах"


# 3. Модель для доставки по схеме FBO
class DeliveryFBO(models.Model):
    marketplace_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price_per_cubic_meter = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_pallet = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_6_pallets = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_15_pallets = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.marketplace_name} - {self.location}"

    class Meta:
        verbose_name = "Доставка по схеме FBO"
        verbose_name_plural = "Доставка по схеме FBO"


# 4. Модель для доставки по схеме FBS
class DeliveryFBS(models.Model):
    marketplace_name = models.CharField(max_length=255)
    small_package_price = models.DecimalField(max_digits=10, decimal_places=2)
    medium_package_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_package_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.marketplace_name

    class Meta:
        verbose_name = "Доставка по схеме FBS"
        verbose_name_plural = "Доставка по схеме FBS"


# 5. Модель для хранения
class Storage(models.Model):
    item_type = models.CharField(max_length=255)
    free_storage_days = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_type

    class Meta:
        verbose_name = "Хранение"
        verbose_name_plural = "Хранение"


# 6. Модель для создания контента
class ContentCreation(models.Model):
    service_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Создание контента"
        verbose_name_plural = "Создание контента"


# 7. Модель для продвижения
class Promotion(models.Model):
    service_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Продвижение"
        verbose_name_plural = "Продвижение"
