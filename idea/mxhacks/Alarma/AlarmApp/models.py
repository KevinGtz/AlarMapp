from django.db import models

class User (models.Model):
	name = models.TextField(max_length = 20)
	email = models.TextField(max_length = 20)
	password = models.TextField(max_length = 20)

# Create your models here.
