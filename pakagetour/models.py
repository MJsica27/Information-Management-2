from django.db import models

# Create your models here.

class TourPackage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Review(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    review_text = models.TextField()

    def __str__(self):
        return f"Review for {self.tour_package.title} by {self.customer_name}"