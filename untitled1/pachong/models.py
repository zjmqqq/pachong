from django.db import models

class movie(models.Model):
    name=models.TextField()
    content=models.TextField()

class uesrs(models.Model):
    username=models.TextField()
    userpassword=models.TextField()
    usersex=models.TextField()

class phoneinfo(models.Model):
    title=models.TextField()
    imgsrc=models.TextField()
    prices=models.TextField()

class computerinfo(models.Model):
    title=models.TextField()
    imgsrc=models.TextField()
    prices=models.TextField()
    merchant=models.TextField()


