from django.conf.urls import url
from .views import *
urlpatterns = [
url(r'registration/$', SnippetList.as_view()),
url(r'deleterecords/$', Deleterecords.as_view()),
url(r'getuser/$', Getuser.as_view()),
url(r'updateuser/([0-9])$', Updateuser.as_view()),
url(r'loginuser/$', Login.as_view()),
url(r'taskfileslist/$', TaskFiles.as_view()),
url(r'getTaskFilesList/$', GetTaskFilesList.as_view()),
url(r'userroles/$', UserRoles.as_view()),
url(r'objectlevel/$', ObjectLevel.as_view()),
url(r'getObjectlevel/$', GetObjectLevel.as_view()),
url(r'scenelevel/$', SceneLevelQuery.as_view()),
url(r'getScenelevel/$', GetSceneLevel.as_view()),
]