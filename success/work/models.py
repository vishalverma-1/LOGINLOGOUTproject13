from django.db import models
class emp(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

