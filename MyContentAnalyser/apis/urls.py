from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'content', ContentViewSet)
# router.register(r'link', LinksViewSet)

urlpatterns = [
   #  path("", getRoutes, name="get-routes"),
    path("fetch/",LinksViewSet),
    path('viewKeywordSummary/<str:channel_id>',View_Keyword_Summary),
    path('viewUnmappedKeywords/<str:channel_id>',Content_Fetch_Unmapped),
    path('viewMappedKeywords/<str:channel_id>',Content_Fetch_Mapped),
    path('viewContentSummary/<str:channel_id>',View_Content_Summary),
    path('viewOriginalContent/<str:channel_id>',View_Original_Content),
    path('viewDateTime/<str:channel_id>',Content_Fetch_DateTime),
    path('parameters/<str:channel_id>',Fetch_Parameters),
] 

    
# urlpatterns = [
#         path('', views.index)
# ]  