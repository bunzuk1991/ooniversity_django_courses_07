from django.conf.urls import include, url
from django.contrib import admin
from pybursa.views import contact

urlpatterns = [
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^courses/',include('courses.urls')),
    url(r'^students/',include('students.urls')),
    url(r'^contact/',contact,name='contact'),
    url(r'^coaches/',include('coaches.urls')),
]