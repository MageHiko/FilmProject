from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ActorModel(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=256)
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = "actor_images/", blank=True, null=True)

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name + " " + self.surname

class FilmModel(models.Model):
    name = models.CharField(max_length=256) # Charfielde mutleq max_lengh verilmelidir
    rating = models.FloatField(default=0)
    pub_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=256)
    poster = models.ImageField(upload_to = "postery/", blank=True, null=True)
    video = models.FileField(upload_to = "videos/", blank=True, null=True)
    fragman = models.FileField(upload_to = "fragmans/", blank=True, null=True)
    views_count = models.IntegerField(default=0)
    about = models.TextField(blank=True, null=True)

    actors = models.ManyToManyField(ActorModel, related_name="films")

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.name
    

class CommentModel (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="user_comments")
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name ="film_comments", blank=True, null=True)
    actor = models.ForeignKey(ActorModel, on_delete=models.CASCADE, related_name ="actor_comments", blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name ="replies", blank=True, null=True)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.user.username + " | " + self.film.name if self.film else self.user.username + " | " + self.actor.name + " " + self.actor.surname

class LikeModel (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="user_likes", blank=True, null=True)
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name ="film_likes", blank=True, null=True)
    actor = models.ForeignKey(ActorModel, on_delete=models.CASCADE, related_name ="actor_likes", blank=True, null=True)
    comment = models.ForeignKey(CommentModel, on_delete=models.CASCADE, related_name ="comment_likes", blank=True, null=True)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self) -> str:
        if self.film:
            return self.user.username + " | " + self.film.name
        elif self.actor:
            return self.user.username + " | " + self.actor.name + " " + self.actor.surname
        else:
            return self.user.username + " | " + self.comment.content 

class ViewsModel (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name ="user_views")
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name ="film_views", blank=True, null=True)
    actor = models.ForeignKey(ActorModel, on_delete=models.CASCADE, related_name ="actor_views", blank=True, null=True)

    class Meta:
        verbose_name = "View"
        verbose_name_plural = "Views"
    
    def __str__(self) -> str:
        if self.film:
            return self.user.username + " | " + self.film.name
        else:
            return self.user.username + " | " + self.actor.name + " " + self.actor.surname