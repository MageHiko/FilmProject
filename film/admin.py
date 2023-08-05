from django.contrib import admin
from film.models import FilmModel, ActorModel, CommentModel, LikeModel

admin.site.register(FilmModel)
admin.site.register(ActorModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
# Register your models here.
