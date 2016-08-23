from django.db import models
from django.conf import settings
from django.utils.encoding import smart_text


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return smart_text(self.name)


class PlaceManager(models.Manager):
    def get_queryset(self):
        qs = super(PlaceManager, self).get_queryset()
        return qs.filter(user__is_active=True)

    def active_places(self):
        return self.get_queryset().filter(
            is_active=True,
        )


class Place(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='added_places')
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    coordinates = models.CharField(max_length=255, null=True, blank=False)
    category = models.ForeignKey(Category, blank=True, null=True)
    has_wifi = models.BooleanField(default=False)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,
                                   related_name='liked_places')

    objects = PlaceManager()
    all_objects = models.Manager()

    def __str__(self):
        return smart_text(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('place_detail', (self.id,))

    def review_count(self):
        return self.review_set.count()


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    place = models.ForeignKey(Place)
    comment = models.TextField(null=True, blank=True)
    vote = models.IntegerField(
        default=3,
        choices=(
            (1, 'Berbat'),
            (2, 'Kötü'),
            (3, 'Meh'),
            (4, 'Uh'),
            (5, 'Yıkılıyor'),
        )
    )

    def __str__(self):
        return smart_text(self.comment)


class Media(models.Model):
    place = models.ForeignKey(Place)
    image = models.ImageField(upload_to="places")

    class Meta:
        verbose_name_plural = "Media"

    def __str__(self):
        return smart_text(self.image.url)
