# users/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

class Pegadri(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True,
        related_name='owned_user_pegadri',
        verbose_name=_('owner'),
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_('name'),
    )
    email = models.EmailField(
        blank=False, null=False,
        verbose_name=_('email'),
    )

    class Meta:
        verbose_name = _('Pegadri')
        verbose_name_plural = _('Pegadris')

    def __str__(self):
        return self.name+', '+str(self.email)

    def get_absolute_url(self):
        return reverse('pegadri_detail', kwargs={'pk': self.pk})

    def can_user_delete(self, user):
        if not self.owner or self.owner == user:
            return True
        if user.has_perm('users.delete_pegadri'):
            return True
        return False

    def can_user_see(self, user):
        if user.has_perm('users.delete_pegadri'):
            return True
        return False


class Cocodri(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True,
        related_name='owned_user_cocodri',
        verbose_name=_('owner'),
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_('name'),
    )
    email = models.EmailField(
        blank=False, null=False,
        verbose_name=_('email'),
    )

    class Meta:
        verbose_name = _('Cocodri')
        verbose_name_plural = _('Cocodris')

    def __str__(self):
        return self.name+', '+str(self.email)

    def get_absolute_url(self):
        return reverse('cocodri_detail', kwargs={'pk': self.pk})

    def can_user_delete(self, user):
        if not self.owner or self.owner == user:
            return True
        if user.has_perm('users.delete_cocodri'):
            return True
        return False

    def can_user_see(self, user):
        if user.has_perm('users.delete_cocodri'):
            return True
        return False


class Functionteam(models.Model):

    name = models.CharField(
        max_length=30,
        verbose_name=_('name'),
    )

    class Meta:
        verbose_name = _('Functionteam')
        verbose_name_plural = _('Functionteams')

    def __str__(self):
        return self.name

