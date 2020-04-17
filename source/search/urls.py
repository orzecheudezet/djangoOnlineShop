
from django.urls import path

from search.views import (
    SearchProductView,
)

app_name = 'search'

urlpatterns = [

    path('', SearchProductView.as_view(), name='query'),

    # path('productsfbv/<int:pk>/', product_detail_view),
    # path('productsfbv/', product_list_view),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
]
