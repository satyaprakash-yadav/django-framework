from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    Title = models.CharField(max_length=100)

    def __str__(self):
        return self.Title 
    
class ImageModel(models.Model):
    Title = models.CharField(max_length=100)
    Category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Images/', blank=True)
    Description = models.TextField()

