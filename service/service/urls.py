from django.urls import include, path

urlpatterns = [
    path('hashtag/', include('hashtag.urls'))
]
