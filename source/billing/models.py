from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
User =settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # customer_id in Stripe or Braintree

    def __str__(self):
        return self.email

def user_created_reciver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

# def billing_profile_reciver(sender, instance, created, *args, **kwargs)  :
#     if created:
#         print("ACTUAL API REQUEST Send to stripe/braintree")
#         instance.customer_id = newID
#         instance.save()

post_save.connect(user_created_reciver, sender=User)
