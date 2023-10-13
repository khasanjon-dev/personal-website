from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, Model, TextField, ImageField


class Project(Model):
    title = CharField(max_length=400)
    description = TextField()
    picture = ImageField(upload_to='images/projects')
    github_link = CharField(max_length=300)
    usage_technology = ArrayField(CharField(max_length=100), size=15)

    # data
    created_at = CharField(max_length=100)
    updated_at = CharField(max_length=100)

    def __str__(self):
        return self.title
