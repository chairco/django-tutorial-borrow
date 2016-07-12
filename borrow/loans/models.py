# loans/models.py
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.validators import (
    MaxValueValidator, MinValueValidator, RegexValidator
)

from users.models import Pegadri, Cocodri, Functionteam

class Loan(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='owned_loans',
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
            "只接受英文、數字、半形符號."
            "內容作為信件標題請仔細填寫 "
            "(限制字數三百字). " 
        ),
    )

    function_team = models.ForeignKey(
        Functionteam,
        verbose_name=_('Function Team')
    )

    cocodri = models.ForeignKey(
        Cocodri, blank=False, null=True,
        related_name='cocodri_item', 
        verbose_name=_('CoCo DRI'),
    )

    pegadri = models.ForeignKey(
        Pegadri, blank=False, null=True,
        related_name='pegadri_item', 
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
        verbose_name = _('Loan')
        verbose_name_plural = _('Loans')

    def __str__(self):
        return self.purpose

    @models.permalink
    def get_absolute_url(self):
        #return reverse('loan_detail', kwargs={'pk': self.pk})
        return ('loan_detail', [self.pk])


class Device(models.Model):

    loan = models.ForeignKey(
        'Loan',
        related_name='menu_items', 
        verbose_name=_('loan'),
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
