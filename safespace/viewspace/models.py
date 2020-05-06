from django.db import models

# Create your models here.

class Photos(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'Ebook'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)


    def get_absolute_url(self):
        return f"/viewspace/{self.pk}"

    def delete_url(self):
        return f"{self.get_absolute_url()}/delete"
