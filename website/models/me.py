from django.db.models import Model, CharField, EmailField, ImageField, TextField, FileField


class Me(Model):
    first_name = CharField(max_length=150)
    last_name = CharField(max_length=150)
    position = CharField(max_length=150)
    email = EmailField(max_length=100)
    phone = CharField(max_length=20)
    location = CharField(max_length=250)
    picture = ImageField(upload_to='images/home/')

    class Meta:
        verbose_name_plural = 'Me'

    def __str__(self):
        return self.first_name


class About(Model):
    about_me = TextField()
    picture = ImageField(upload_to='images/about/')
    cv_file = FileField(upload_to='files/about/cv/')

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_me


class Skills(Model):
    name = CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class WorkExperience(Model):
    position = CharField(max_length=250)
    start_date = CharField(max_length=250)
    end_date = CharField(max_length=250)
    description = TextField()
    company_name = CharField(max_length=250)
    location = CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'WorkExperience'

    def __str__(self):
        return self.position


class SocialMedia(Model):
    name = CharField(max_length=250)
    url = CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'SocialMedia'

    def __str__(self):
        return self.name
