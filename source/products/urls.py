
from django.urls import path

from products.views import (
# product_list_view,
ProductListView,
# ProductDetailView,
# product_detail_view,
# ProductFeaturedListView,
# ProductFeaturedDetailView,
ProductDetailSlugView
)

urlpatterns = [

    path('', ProductListView.as_view()),
    path('<slug:slug>/', ProductDetailSlugView.as_view()),
    # path('productsfbv/<int:pk>/', product_detail_view),
    # path('productsfbv/', product_list_view),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
]
