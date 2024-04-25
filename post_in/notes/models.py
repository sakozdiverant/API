from django.db.models import (Model, CharField, TextField, DateTimeField)


class Note(Model):
    title = CharField(max_length=255)
    text = TextField(blank=True)
    created = DateTimeField(auto_now_add=True)
    update = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-update']