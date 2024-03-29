from django.db import models



class Newsletter(models.Model):

    """ A model for newsletter subscribers table """

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Newsletter subscribers'
        ordering = ['created']

    def __str__(self):
        return self.name



class Contact(models.Model):

    """ A model to create the inbox from contact form """

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Email inbox'
        ordering = ['created']

    def __str__(self):
        return self.name        