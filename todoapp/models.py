from django.db import models

# Create your models here.

PRIORITY = (('danger', 'high'),('info','normal'),('success','low'))  # (保存されるデータ, 表示データ)
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    def __str__(self):  # objectに名前をつける(object1とかではない)
        return self.title  # title名をobject名にする