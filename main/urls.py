from django.urls import path
from . import views
urlpatterns = [
    path("<int:id>",views.idirect),
    path("",views.home),
    path("create/",views.create),
    path("del/",views.delete),
    path('upload',views.upload)
]