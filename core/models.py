from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    text = models.TextField()
    embedding = models.BinaryField()  # Store embeddings as bytes
