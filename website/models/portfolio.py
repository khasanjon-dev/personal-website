from django.db.models import CharField, Model, TextField, ForeignKey, CASCADE, ImageField


class CategoryPortfolio(Model):
    name = CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'CategoryPortfolio'

class Portfolio(Model):
    title = CharField(max_length=400)
    description = TextField()

    # relationship
    category = ForeignKey(CategoryPortfolio, CASCADE)

    class Meta:
        verbose_name_plural = 'Portfolio'


class UseTechnologies(Model):
    name = CharField(max_length=250)

    # relationship
    portfolio = ForeignKey(Portfolio, CASCADE)
    class Meta:
        verbose_name_plural = 'UseTechnologies'


class Images(Model):
    image = ImageField(upload_to='images/portfolio')
    description = TextField()

    # relationship
    portfolio = ForeignKey(Portfolio, CASCADE)

    class Meta:
        verbose_name_plural = 'Images'