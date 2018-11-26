from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from static.py import slugify
from static.py import choices


# The Request class ####################################################################################################
class Request(models.Model):
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=4000)
    category = models.IntegerField(choices=choices.CATEGORY, default=1)
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    request_slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    is_reported = models.BooleanField(default=False)
    anonymous = models.BooleanField(default=True)
    start_price = models.IntegerField(validators=[RegexValidator(r'^\d{1,10}$')])
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request_slug

    def save(self, **kwargs):
        slug_str = "%s %s" % (self.subject, hash(self.subject) % (5000000 * 2))
        slugify.unique_slugify(self, slug_str, 'request_slug')
        super(Request, self).save(**kwargs)


# The Offer class ######################################################################################################
class Offer(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='offers')
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    is_active = models.BooleanField(default=True)
    is_reported = models.BooleanField(default=False)
    offer_slug = models.SlugField(unique=True)
    offer_price = models.IntegerField(null=True, validators=[RegexValidator(r'^\d{1,10}$')])

    def save(self, **kwargs):
        slug_str = "%s" % (hash(self.message) % (5000000 * 2))
        slugify.unique_slugify(self, slug_str, 'offerSlug')
        super(Offer, self).save(**kwargs)

    def __str__(self):
        return self.offer_slug


# The Media Offer class ################################################################################################
class OfferMedia(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='offermedias')
    media = models.FileField(upload_to='documents/')


# The Message Class between a Request and an Offer #####################################################################
class Message(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='messages')
    pm_message = models.TextField(max_length=5000)
    pm_created_at = models.DateTimeField(auto_now_add=True)
    pm_updated_at = models.DateTimeField(null=True)
    pm_created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    pm_updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')


# User-hidden Request Class ############################################################################################
class HiddenRequest(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='hiddenRequests')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
