from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name=models.CharField(max_length=100)
    preview_text=models.TextField(max_length=200)
    details_text=models.TextField(max_length=2000)
    price=models.FloatField()
    old_price=models.FloatField(default=0.00)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Category')
    image=models.ImageField(upload_to='product')
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        class Meta:
            ordering=['-created',]
