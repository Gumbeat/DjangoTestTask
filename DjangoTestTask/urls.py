"""DjangoTestTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from TestTask.views import OrganizationListView, OrganizationDetail, ProductDetail, ProductListView, \
    OrganizationsByDistrictView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organizations/', OrganizationListView.as_view(), name='organizations'),
    path('organizations/<int:pk>/', OrganizationsByDistrictView.as_view(), name='organizations_by_district'),
    path('organization/<int:pk>/', OrganizationDetail.as_view(), name='organization_detail'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
