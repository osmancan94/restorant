
from django.db import models

class Siparis(models.Model):
    urun_adi = models.CharField(max_length=100)
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.urun_adi
# anasayfa/models.py

from django.db import models

class Urun(models.Model):
    isim = models.CharField(max_length=100)
    fiyat = models.DecimalField(max_digits=6, decimal_places=2)
    resim = models.ImageField(upload_to='urun_resimleri/')
    aciklama = models.TextField(blank=True)

    def __str__(self):
        return self.isim
