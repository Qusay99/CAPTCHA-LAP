from django.db import models
from django.contrib.auth.models import User

vwl = "Volkswirtschaftslehre"
math = "Mathe"
programming = "Programmieren"
ds = "Data Science"
informatics = "Informatik"
databases = "Datenbanken"
recht = "Recht"
management = "Management"

blog = "Blog"
video = "Video"
internet = "Internet"
book = "Buch"
other = "Sonstiges"

topic_choices = ((math, "Mathe"),
                 (programming, "Programmieren"),
                 (vwl, "Volkswirtschaftslehre"),
                 (ds, "Data Science"),
                 (informatics, "Informatik"),
                 (databases, "Datenbanken"),
                 (recht, "Recht"),
                 (management, "Management"))

type_choices = ((blog, "Blogbeitrag"),
                (video, "Videobeitrag"),
                (internet, "Internetseite"),
                (book, "Buch"),
                (other, "Sonstiges"))
# Create your models here.
class Content(models.Model):
    content_type = models.CharField(max_length=50, choices=type_choices, default=video)
    header = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="added_content", null=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    topic = models.CharField(max_length=50, choices=topic_choices, default=math)
    link_to_source = models.URLField()
    created_on = models.DateField(auto_now_add=True)
    num_of_likes = models.IntegerField(default=0)
    content_creator = models.CharField(max_length=30)
    content_thumbnail = models.ImageField(blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return "Content {} of type {}. Thema: {}, Content-Creator: {}, Created: {}".format(self.header, self.content_type, self.topic, self.content_creator, self.created_on)

class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="comments")
    header = models.CharField(max_length=80, verbose_name="Überschrift")
    created_on = models.DateField(auto_now_add=True)
    num_of_likes = models.IntegerField(default=0)
    body = models.TextField(max_length=400, verbose_name="Inhalt")
    active = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return "Comment {} by {}".format(self.body, self.header)

class Document(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    uploaded_on = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)
    uploader = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name="documents")
    topic = models.CharField(max_length=50, choices=topic_choices, default=math)
    downloads = models.IntegerField(default=0)
    docfile = models.FileField(upload_to='documents', help_text="Maximal 42 Megabyte")

    class Meta:
        ordering = ["uploaded_on"]
    
    def __str__(self):
        return f"Document '{self.name}', uploaded on {self.uploaded_on}."
