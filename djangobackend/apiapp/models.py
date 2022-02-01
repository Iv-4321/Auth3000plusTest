from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=120, null=True)
    author = models.CharField(max_length=400, null=True)
    picture = models.FileField(null=True)
    description = models.TextField(null=True)
    pdf = models.FileField(blank=True)

    def __str_(self):
        return "Book for {}".format(self.name)