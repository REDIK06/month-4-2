from django.db import models


class CarShop(models.Model):

    ENGINE = (
        ('Бензин', 'Бензин'),
        ('Дизель', 'Дизель'),
        ('Гибрид', 'Гибрид'),
        ('Газ', 'Газ'),
        ('Электро', 'Электро'),
    )

    STEERING_WHEEL = (
        ('Слева', 'Слева'),
        ('Справа', 'Справа'),
    )

    DRIVE_UNIT = (
        ('Полный', 'Полный'),
        ('Передний', 'Передний'),
        ('Задний', 'Задний'),
    )

    DISCOUNT_PERCENTAGE = (
        ('3%', '3%'),
        ('5%', '5%'),
        ('10%', '10%'),
    )

    title = models.CharField(max_length=100, verbose_name='Укажите марку автомобиля')
    description = models.TextField(verbose_name='Укажите  информацию о характеристиках автомобиля')
    image = models.URLField(verbose_name='Укажите ссылку на фото')
    year = models.IntegerField(max_length=100, verbose_name='Укажите год автомобиля', null=True)
    engine = models.CharField(max_length=100, choices=ENGINE)
    steering_wheel = models.CharField(max_length=100, choices=STEERING_WHEEL)
    drive_unit = models.CharField(max_length=100, choices=DRIVE_UNIT, null=True)
    acceleration = models.FloatField(verbose_name='Разгон до 100км/ч:', null=True)
    price = models.PositiveIntegerField(verbose_name='Укажите цену')
    discount = models.CharField(max_length=100, choices=DISCOUNT_PERCENTAGE)
    gift = models.CharField(max_length=100, verbose_name='Укажите подарок к покупке', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}-{self.price}'

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'


class ReviewCars(models.Model):
    car_review = models.ForeignKey(CarShop, on_delete=models.CASCADE, related_name='review_cars')
    text = models.TextField(verbose_name='Напишите коммент')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car_review}-{self.text}'


class Comment(models.Model):
    review = models.ForeignKey(ReviewCars, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.review.text} - {self.text}'

