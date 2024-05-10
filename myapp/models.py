from django.db import models

# Create your models here.

cat = (
        ("Starter", "Starter"),
        ("Mains", "Mains"),
        ("Desserts", "Desserts"),
        ("Drinks", "Drinks")
    )
class menu_items(models.Model):
    category = models.CharField(
        max_length=20,
        choices=cat,
        default="Starter"
    )
    title = models.TextField(max_length=120)
    desc = models.TextField(max_length=500)
    price = models.IntegerField()



class reservation(models.Model):
    name = models.TextField(max_length=120)
    contact_number = models.TextField(max_length=120)
    date = models.DateField()
    party_size = models.IntegerField()
    additional_information = models.TextField(max_length=500)

class FeedBack(models.Model):
    name = models.CharField(max_length=120)
    contact_number = models.CharField(max_length=120)
    date = models.DateField()
    feedback_model = models.TextField(max_length=500)