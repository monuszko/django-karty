from django.db import models


class MenuCard(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField("Description", max_length=200)
    pub_date = models.DateTimeField("Publication date", auto_now_add=True)
    mod_date = models.DateTimeField("Modification date", auto_now=True)

    def __str__(self):
        return self.name


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

