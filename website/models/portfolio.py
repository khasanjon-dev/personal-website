from django.db.models import CharField, Model, TextField, ForeignKey, CASCADE, ImageField


class Project(Model):
    title = CharField(max_length=400)
    description = TextField()
    picture = ImageField(upload_to='images/projects')

    # data
    created_at = CharField(max_length=100)
    updated_at = CharField(max_length=100)
    github_link = CharField(max_length=300)

    def __str__(self):
        return self.title


class UsageTechnology(Model):
    name = CharField(max_length=250)
    # relationship
    project = ForeignKey(Project, CASCADE)

    class Meta:
        verbose_name_plural = 'Usage Technologies'

    def __str__(self):
        return self.name
