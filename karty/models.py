from datetime import timedelta

from django.db import models

from django.core.urlresolvers import reverse


AT_LEAST_OLDER = timedelta(minutes=30)


class PublicMenuCardManager(models.Manager):
    def get_queryset(self):
        return super(PublicMenuCardManager, self).get_queryset().annotate(num_dishes=models.Count('dish')).exclude(num_dishes=0)


class MenuCard(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField("Description", max_length=200)
    pub_date = models.DateTimeField("Publication date", auto_now_add=True)
    mod_date = models.DateTimeField("Modification date", auto_now=True)

    objects = models.Manager()
    public = PublicMenuCardManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('karty:detail', args=(self.pk,))

    def was_modified(self):
        """
        Template method to make it easier no to display trivial edits soon
        after publication.
        """
        if self.mod_date > self.pub_date + AT_LEAST_OLDER:
            return True
        return False


class Dish(models.Model):
    menucard = models.ForeignKey(MenuCard, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    desc = models.TextField("Description", max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateTimeField("Publication date", auto_now_add=True)
    mod_date = models.DateTimeField("Modification date", auto_now=True)
    time = models.DurationField("Preparation time")
    vege = models.BooleanField("Vegetarian", default=False, help_text="Is it vegetarian ?")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "dishes"

