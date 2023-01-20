from django.db import models

#choice
STUDYSTATE = [
    ("will","学習したい"),
    ("ing","学習してる"),
    ("can","使える")
]


class Studystate(models.Model):
    state = models.CharField(verbose_name="学習状況",choices=STUDYSTATE,max_length=16)
    language = models.CharField(max_length=32)
    imgurl = models.URLField(max_length=2048)
    def __str__(self) -> str:
        return self.language + ":" + self.state

class Strong(models.Model):
    strong = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.strong

class StrongExp(models.Model):
    strong = models.ForeignKey(Strong,related_name="exps",on_delete=models.CASCADE)
    exp = models.CharField(max_length=50)

    def __str__(self):
        return self.exp

class History(models.Model):
    when = models.CharField(max_length=20)
    event = models.CharField(max_length=128)
    order = models.PositiveIntegerField(verbose_name="順序")

    class Meta:
        ordering = ['order']

    def __str__(self) -> str:
        return self.when + ":" + self.event