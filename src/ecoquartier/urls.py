"""ecoquartier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from djgeojson.views import GeoJSONLayerView

from projects import views
from projects.models import Project


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^detail/(?P<pk>\d+)', views.ProjectDetailView.as_view(), name='detail'),
    url(r'^create/$', login_required(views.ProjectCreateView.as_view()), name='create'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Project, geometry_field='coordonnees_geographiques'), name='data')
]
