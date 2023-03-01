from django.db import models
from django.utils.translation import gettext_lazy as _

# optional field arguments
OPTIONAL = {
    'blank': True,
    'null': True,
}

# Create your models here.

class AgileValues(models.Model):
    heading = models.CharField(
        max_length=255,
        **OPTIONAL
        )
    definition = models.TextField(
        max_length=3000,
        **OPTIONAL
        )
    
    class Meta:
        verbose_name = _('Agile Value')
        verbose_name_plural = _('Agile Values')

    def __str__(self):
        return self.heading
    
class AgilePrinciples(models.Model):
    heading = models.CharField(
        max_length=255,
        **OPTIONAL
        )
    definition = models.TextField(
        max_length=3000,
        **OPTIONAL
        )
    
    class Meta:
        verbose_name = _('Agile Principle')
        verbose_name_plural = _('Agile Principles')

    def __str__(self):
        return self.heading
