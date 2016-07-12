# faships/models.py
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.validators import (
    MaxValueValidator, MinValueValidator, RegexValidator
)

from users.models import Pegadri, Cocodri, Functionteam


class Station(models.Model):

    name = models.CharField(
        max_length=30,
        verbose_name=_('name'),
    )

    class Meta:
        verbose_name = _('Station')
        verbose_name_plural = _('Stations')

    def __str__(self):
        return self.name


class Faship(models.Model):
        
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='owned_faships',
    )

    purpose = models.TextField(
        max_length=300, null=True,
        validators=[
            RegexValidator(
               regex=r"^[a-z A-Z 0-9 \[^\u4e00-\u9fa5\] /,.?~!@#$%^&*()_+]*$",
               message='Chinese characters are restricted. Must be alphanumeric'
                       '(只接受英文、數字、半形符號).',
               code='invalid',
            ),
        ],
        verbose_name=_('Loan Purpose'),
        help_text=_(
            "只接受英文、數字、半形符號， "
            "內容作為信件標題請仔細填寫，"
            "(限制字數三百字)。" 
        ),
    )

    function_team = models.ForeignKey(
        Functionteam,
        verbose_name=_('Function Team')
    )

    cocodri = models.ForeignKey(
        Cocodri, blank=False, null=True,
        related_name='cocodri_item_fa', 
        verbose_name=_('CoCo DRI'),
    )

    recipient = models.ForeignKey(
        Cocodri, blank=False, null=True,
        related_name='recipient_item_fa', 
        verbose_name=_('Recipient Name'),
    )

    pegadri = models.ForeignKey(
        Pegadri, blank=False, null=True,
        related_name='pegadri_item_fa', 
        verbose_name=_('Pega DRI'),
    )

    pega_dri_mail_group = models.CharField(
        max_length=600,
        null=True,
        verbose_name=_('Pega DRI Mail Group'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Faship')
        verbose_name_plural = _('Faships')

    def __str__(self):
        return self.purpose

    @models.permalink
    def get_absolute_url(self):
        #return reverse('loan_detail', kwargs={'pk': self.pk})
        return ('faship_detail', [self.pk])


class Device(models.Model):

    FFNED_CHOICES = (
        ('FF', _('FF')),
        ('NED', _('NED')),
    )
    ffned = models.CharField(
        max_length=3, 
        choices=FFNED_CHOICES,
        verbose_name=_('FF/NED')
    )

    UIFDR_CHOICES = (
        ('NO', _('NO')),
        ('YES', _('YES')),
    )
    uifdr = models.CharField(
        max_length=3, 
        choices=UIFDR_CHOICES,
        verbose_name=_('Non UI/FDR-seal')
    )

    faship = models.ForeignKey(
        'Faship',
        related_name='menu_items', 
        verbose_name=_('faship'),
    )

    config = models.CharField(
        max_length=10,
        blank=True, null=True,
    )

    unit_no = models.CharField(
        max_length=20,
        blank=True, null=True,
    )

    isn = models.CharField(
        max_length=20,
        blank=False, null=True,
        verbose_name=_('ISN'),
    )

    station = models.ForeignKey(
        'Station',
        related_name='station_items', 
        verbose_name=_('Station'),
    )

    failure_symptoms = models.CharField(
        max_length=300,
        blank=False, null=True,
    )

    radar = models.CharField(
        max_length=20,
        blank=True, null=True,
        verbose_name=_('Radar'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')

    def __str__(self):
        return self.isn

    @models.permalink
    def get_absolute_url(self):
        return ('device_detail', [self.pk])


