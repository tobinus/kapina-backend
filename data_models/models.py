from datetime import datetime

from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from solo.models import SingletonModel
from sorl_cropping import ImageRatioField


class Category(models.Model):
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategorier"

    name = models.CharField('Navn', max_length=64, unique=True)
    text_color = ColorField('Tekstfarge', default='000000')
    background_color = ColorField('Bakgrunnsfarge', default='ECB61C')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.__unicode__())


class Settings(SingletonModel):
    class Meta:
        verbose_name = 'Innstillinger'

    chief_editor = models.CharField('Ansvarlig redaktør', default="", max_length=128)
    radio_editor = models.CharField('Radioredaktør', default="", max_length=128)

    about = models.TextField('Om Radio Revolt')

    privacy_policy = models.TextField('Personvernerklæring', default="")

    def __unicode__(self):
        return 'Innstillinger for Radio Revolt'

    def __str__(self):
        return str(self.__unicode__())


class Show(models.Model):
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programmer"

    name = models.CharField('Navn', max_length=64, unique=True)
    slug = models.CharField(max_length=64, unique=True, editable=False)
    image = models.ImageField('Programlogo', upload_to='uploads/images')
    lead = models.CharField('Kort beskrivelse', max_length=140)
    content = models.TextField('Lang beskrivelse')

    categories = models.ManyToManyField(Category, blank=True, verbose_name='Kategorier')

    archived = models.BooleanField('Arkivert', default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, verbose_name='Opprettet av')

    def save(self, *args, **kwargs):
        if not self.id:
            # New object is being created.
            self.slug = slugify(self.name, allow_unicode=True)
            if Show.objects.filter(slug=self.slug).exists():
                self.slug = '{slug}-{random_string}'.format(
                    slug=self.slug, random_string=get_random_string(length=3))
            super(Show, self).save(*args, **kwargs)
        else:
            # The object already exists in DB.
            super(Show, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.__unicode__())

    def get_absolute_url(self):
        return '/programmer/' + self.slug


class Episode(models.Model):
    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episoder"
        ordering = ['-created_at']

    title = models.CharField('Tittel', max_length=64)
    use_title = models.BooleanField(
        'Bruk tittel',
        default=False,
        help_text='Vis tittelen på episoden. ' +
        'Om ikke tittel benyttes vises "Navn på show" + "Publiseringsdato"')
    lead = models.CharField('Beskrivelse', max_length=140)

    show = models.ForeignKey(
        Show,
        related_name='episodes',
        verbose_name='Program',
        on_delete=models.CASCADE,
    )

    categories = models.ManyToManyField(Category, blank=True, verbose_name='Kategorier')

    publish_at = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, verbose_name='Opprettet av')
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    on_demand_url = models.URLField(help_text="https://ondemandinfo.radiorevolt.no/")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.__unicode__())

    def get_absolute_url(self):
        # TODO: Update with episode link when we add support for this
        return '/programmer/' + self.show.slug


class Post(models.Model):
    class Meta:
        verbose_name = "Artikkel"
        verbose_name_plural = "Artikler"
        ordering = ['-publish_at']

    title = models.CharField('Tittel', max_length=64)
    slug = models.CharField(max_length=64, unique=True, editable=False)
    image = models.ImageField('Bilde', upload_to='uploads/images')
    cropping = ImageRatioField(
        'image',
        '1024x512',
        size_warning=True,
        verbose_name='Bildeutsnitt',
        help_text='Velg bildeutsnitt')
    lead = models.CharField('Ingress', max_length=140)
    content = models.TextField('Brødtekst')
    deleted = models.BooleanField('Slettet', default=False)

    episodes = models.ManyToManyField(
        Episode,
        blank=True,
        verbose_name='Episoder',
        help_text='Legger til episoder i bunnen av artikkelen. ' +
        'Episodelisten blir filtrert på valgt program etter at artikkelen er opprettet.')

    show = models.ForeignKey(
        Show,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Program',
        on_delete=models.CASCADE)

    categories = models.ManyToManyField(Category, blank=True, verbose_name='Kategorier')

    publish_at = models.DateTimeField('Publisert', default=datetime.now)

    ready_to_be_published = models.BooleanField(
        'Klar til publisering',
        default=False,
        help_text='Artikkelen vil aldri bli publisert før denne er huket av. ' +
        'Dette er uavhengig av hvilket publiseringstidspunkt som er satt ovenfor. ')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='publications', verbose_name='Opprettet av')

    def save(self, *args, **kwargs):
        if not self.id:
            # New object is being created.
            self.slug = slugify(self.title, allow_unicode=True)
            if Post.objects.filter(slug=self.slug).exists():
                self.slug = '{slug}-{random_string}'.format(
                    slug=self.slug, random_string=get_random_string(length=3))
            super(Post, self).save(*args, **kwargs)
        else:
            # The object already exists in DB.
            super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.__unicode__())

    def get_absolute_url(self):
        return '/post/' + self.slug
