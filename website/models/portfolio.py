from django.db.models import CharField, Model, TextField, ForeignKey, CASCADE, ImageField


class CategoryPortfolio(Model):
    name = CharField(max_length=250)


class Portfolio(Model):
    title = CharField(max_length=400)
    description = TextField()

    # relationship
    category = ForeignKey(CategoryPortfolio, CASCADE)


class UseTechnologies(Model):
    name = CharField(max_length=250)

    # relationship
    portfolio = ForeignKey(Portfolio, CASCADE)


class Images(Model):
    image = ImageField(upload_to='images/portfolio')
    description = TextField()

    # relationship
    portfolio = ForeignKey(Portfolio, CASCADE)
