from django.shortcuts import render, redirect
from film.models import FilmModel, ActorModel, CommentModel, LikeModel, ViewsModel
from django.views.generic import View

class IndexView(View):
    def get(self, request, *args,**kwargs):
        films = FilmModel.objects.all()
        context = {
            "films": films
    }
        return render(request, "index.html", context)


    # def post(self, request, *args,**kwargs):
    #     pass

# def index(request):
#     films = FilmModel.objects.all()
#     context = {
#         "films": films
#     }
#     return render(request, "index.html", context)

class DetailView(View):
    def get(self, request, id, *args,**kwargs):
        film = FilmModel.objects.get(id=id)
        user_comments = CommentModel.objects.filter(
            user = request.user,
            film = film
        ) if request.user.is_authenticated else None

        if request.user.is_authenticated:
            ViewsModel.objects.create(
                user = request.user,
                film = film,
        ) 

        context = {
            "film": film,
            "user_comments": user_comments,

        }

        return render(request, "detail.html", context)

    def post(self, request, id, *args,**kwargs):
        choice = request.POST.get("choice")
        if choice == "comment":
            film_id = request.POST.get("film_id")
            film = FilmModel.objects.get(id=film_id)
            content = request.POST.get("content")

            CommentModel.objects.create(
                user = request.user,
                film = film,
                content = content
            )
        elif choice == "like":
            film_id = request.POST.get("film_id")
            film = FilmModel.objects.get(id=film_id)

            if not LikeModel.objects.filter(user=request.user, film=film).exists():
                LikeModel.objects.create(
                    user = request.user,
                    film = film
                )
            else:
                like = LikeModel.objects.get(user=request.user, film=film)
                like.delete()

        elif choice == "like_comment":
            comment_id = request.POST.get("comment_id")
            comment = CommentModel.objects.get(id=comment_id)

            if not LikeModel.objects.filter(user=request.user, comment=comment).exists():
                LikeModel.objects.create(
                    user = request.user,
                    comment = comment
                )
            else:
                like = LikeModel.objects.get(user=request.user, comment=comment)
                like.delete()
           
        return redirect("detail", id=id)

# def detail(request, id):
#     film = FilmModel.objects.get(id=id)
#     user_comments = CommentModel.objects.filter(
#         user = request.user,
#         film = film
#     ) if request.user.is_authenticated else None

#     if request.user.is_authenticated:
#         ViewsModel.objects.create(
#             user = request.user,
#             film = film,
#         ) 

#     context = {
#         "film": film,
#         "user_comments": user_comments,

#     }
    # if request.method =="POST":
    #     choice = request.POST.get("choice")
    #     if choice == "comment":
    #         film_id = request.POST.get("film_id")
    #         film = FilmModel.objects.get(id=film_id)
    #         content = request.POST.get("content")

    #         CommentModel.objects.create(
    #             user = request.user,
    #             film = film,
    #             content = content
    #         )
    #     elif choice == "like":
    #         film_id = request.POST.get("film_id")
    #         film = FilmModel.objects.get(id=film_id)

    #         if not LikeModel.objects.filter(user=request.user, film=film).exists():
    #             LikeModel.objects.create(
    #                 user = request.user,
    #                 film = film
    #             )
    #         else:
    #             like = LikeModel.objects.get(user=request.user, film=film)
    #             like.delete()

    #     elif choice == "like_comment":
    #         comment_id = request.POST.get("comment_id")
    #         comment = CommentModel.objects.get(id=comment_id)

    #         if not LikeModel.objects.filter(user=request.user, comment=comment).exists():
    #             LikeModel.objects.create(
    #                 user = request.user,
    #                 comment = comment
    #             )
    #         else:
    #             like = LikeModel.objects.get(user=request.user, comment=comment)
    #             like.delete()
           
    #     return redirect("detail", id=id)

    # return render(request, "detail.html", context)

class ActorView(View):
    def get(self, request, *args,**kwargs):
        actors = ActorModel.objects.all()


        context = {
            "actors": actors
        }
        return render(request, "actor.html", context)

class ActorDetailView(View):
    def get(self, request, id, *args, **kwargs):
        actor = ActorModel.objects.get(id=id)
        user_comments = CommentModel.objects.filter(
            user = request.user,
            actor = actor,
            ) if request.user.is_authenticated else None
            
        context = {
            "actor": actor,
            "user_comments": user_comments,
        }

        if request.user.is_authenticated:
            ViewsModel.get.objects(
                user = request.user,
                actor = actor,
            )
        return render(request, "actor_detail.html", context)

    def post(self, request, id, *args, **kwargs):
        choice = request.POST.get("choice")
        if choice == "comment":
            actor_id = request.POST.get("actor_id")
            actor = ActorModel.objects.get(id=actor_id)
            content = request.POST.get("content")

            CommentModel.objects.create(
                user = request.user,
                actor = actor,
                content = content
            )
        elif choice == "like":
            actor_id = request.POST.get("actor_id")
            actor = ActorModel.objects.get(id=actor_id)

            if not LikeModel.objects.filter(user=request.user, actor=actor).exists():
                LikeModel.objects.create(
                    user = request.user,
                    actor= actor
                )
            else:
                like = LikeModel.objects.get(user=request.user, actor=actor)
                like.delete()

        elif choice == "like_comment":
            comment_id = request.POST.get("comment_id")
            comment = CommentModel.objects.get(id = comment_id)

            if not LikeModel.objects.filter(user=request.user, comment=comment).exists():
                LikeModel.objects.create(
                    user = request.user,
                    comment=comment
                )
            else:
                like = LikeModel.objects.get(user=request.user, comment=comment)
                like.delete()

                   
        return redirect("actor_detail", id=id)



class DeleteCommentView(View):
    def get(self,request, id, *args, **kwargs):
        comment = CommentModel.objects.get(id=id)
        comment.delete()
        return redirect("detail", id = comment.film.id)
    
class UserViewsView(View):
    def get(self,request, id, *args, **kwargs):
        likes = LikeModel.objects.filter(
            user = request.user,
        )
        film_likes, actor_likes = [], []
        for like in likes:
            if like.film:
                film_likes.append(like)
            elif like.actor:
                actor_likes.append(like)
        views = ViewsModel.objects.filter(
            user = request.user,
        )
        film_views, actor_views = [], []
        for view in views:
            if view.film:
                film_views.append(view)
            elif view.actor:
                actor_views.append(view)
        comments = CommentModel.objects.filter(
            user = request.user,
        )
        film_comments, actor_comments = [], []
        for comment in comments:
            if comment.film:
                film_comments.append(comment)
            elif comment.actor:
                actor_comments.append(comment)

        context = {
            "film_likes":film_likes,
            "actor_likes":actor_likes,
            "film_views":film_views,
            "actor_views":actor_views,
            "film_comments":film_comments,
            "actor_comments":actor_comments,
        }

        return render(request, "user_views.html", context)

# Create your views here.

