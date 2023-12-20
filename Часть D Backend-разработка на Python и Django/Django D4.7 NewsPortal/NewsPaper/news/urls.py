from django.urls import path
from .views import (PostList, PostDetail, PostSearch, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, ArticleUpdate, ArticleDelete)
                    # create_post)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),

    # path('create/', create_post, name='product_create'),
    path('news/create/', NewsCreate.as_view(), name='post_create'),
    path('news/<int:pk>/update', NewsUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete', NewsDelete.as_view(), name='post_delete'),

    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),

]