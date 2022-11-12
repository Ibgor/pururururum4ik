from django.db.models import (Model,
                              CharField,
                              ForeignKey,
                              CASCADE,
                              )

# Create your models here.


class Curator(Model):
    first_name = CharField(max_length=10)

    def __str__(self):
        return "kurat kurva "+self.first_name

class Direction(Model):
    name = CharField(max_length=10)
    curator = ForeignKey(Curator,
                         on_delete=CASCADE,
                         related_name='direction',
                         )
    def __str__(self):
        return "napravlenie "+self.name


class discipline(Model):
    dis_name = CharField(max_length=10)
    direction = ForeignKey(Direction,
                         on_delete=CASCADE,
                         related_name='discipline',
                         )


    def __str__(self):
        return "discipline "+self.dis_name
