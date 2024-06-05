"""
URL configuration for dalasgar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.n3),
    path('ulanyjy_gos', views.n1),
    path('submit/',views.n2),
    path('giris/', views.n4),
    path('admin2', views.n5),
    path('talyp_gos', views.n6),
    path('girenler', views.n7),
    path('uytget/<int:i>', views.n8),
    path('save/<int:i>', views.n9),
    path('save_talyp/', views.n11),
    path('deneme',views.deneme),
    path('home/<str:i>/<str:p>',views.n12),
    path('gozle_home/<str:q>/<str:p>', views.n13),
    path('maglumat/<int:i>/<int:s>', views.n14),
    path('bar/', views.n15),
    path('ekzamen/<int:i>',views.n16),
    path('gozl/',views.n17),
    path('gozlemek/',views.n18),
    path('sahranit/<int:i>', views.n19),
    path('tablisa', views.n20),
    path('ad_filter' ,views.n21),
    path('ssss/<str:q>/<str:w>', views.n22),
    path('familya_filter' ,views.n23),
    path('ata_ady_filter' ,views.n24),
    path('netije_filter' ,views.n25),
    path('ugur_filter' ,views.n26),
    path('id_filter' ,views.n27),
    path('t/<int:i>', views.n28),
    path('r/<int:i>', views.n29),
    path('e/<int:i>', views.n30),
    path('deneme2',views.n31),
    path('sony/<int:i>', views.n32),
    path("filter/<int:i>", views.filter, name="filter"),
    path('poz/<int:i>', views.poz),
    path('poz2/<int:i>', views.poz2),
    path('jik',views.pim)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
