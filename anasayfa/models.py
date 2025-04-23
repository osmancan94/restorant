
from django.db import models

class Siparis(models.Model):
    urun_adi = models.CharField(max_length=100)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.urun_adi
