from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import createMallView, detailsMallView
from .views import createShopView, detailsShopView
from .views import fetchDataview, viewUserTable, createProductView,\
    detailsProductView, MallsList, Shoplist,\
    Productlist, SearchProductlist, OrderCreateView, OrderDeatilsView,\
    OrderHistory, UpdatePassword
from .views import ResetPasswordRequestView
from api.views import create_user, UserRegistration, UserList, CreateOrder, login_user,\
 SearchMall, SearchShop, User_detail,\
    Product_view, Shop_details_view, WishListCreate
app_name = 'api'
urlpatterns = {
    url(r'^mall_create/$', createMallView.as_view(), name="create"),
    url(r'^mall_details/(?P<pk>[0-9]+)/$', detailsMallView.as_view(), name="details"),
    url(r'^shop_create/$', createShopView.as_view(), name="create"),
    url(r'^shop_details/(?P<pk>[0-9]+)/$', detailsShopView.as_view(), name="details"),
    url(r'^fetch_join/(?P<pk>[0-9]+)/$', fetchDataview.as_view(), name="details"),
    url(r'^view_user/$', viewUserTable.as_view(), name="details"),
    url(r'^product_create/$', createProductView.as_view(), name="details"),
    #url(r'^product_details/(?P<pk>[0-9]+)/$', detailsProductView.as_view(), name="details"),# product details based on product id
    url(r'^mall_list/$', MallsList.as_view(), name="list"),#mall list api
    url(r'^shop_list/$', Shoplist.as_view(), name="list"),#shop list api
    url(r'^product_list/$', Productlist.as_view(), name="list"),#product list api
    url(r'^product_search/$', SearchProductlist.as_view(), name="searchlist"),#search product api
    url(r'^mall_search/$', SearchMall.as_view(), name="searchlist"),#search mall api
    url(r'^shop_search/$', SearchShop.as_view(), name="searchlist"),#search shop api
    url(r'^order_create/$', OrderCreateView.as_view(), name="create"),#create order api
    url(r'^order_details/(?P<pk>[0-9]+)/$', OrderDeatilsView.as_view(), name="details"),
    url(r'^order_history/$', OrderHistory.as_view(), name="create"),
    url(r'^user_registration/$', UserRegistration.as_view(), name="create"),
    #url(r'^user_login/$', UserLogin.as_view(), name="create"),
    url(r'^change_password/$', UpdatePassword.as_view(), name="create"),#change password api
    url(r'^reset_password/$', ResetPasswordRequestView.as_view(), name="create"),
    url(r'^create_wishlist/$', WishListCreate.as_view(), name="create"),
    #url(r'^create_cart/$', CartCreate.as_view(), name="create"),
    #url(r'^delete_from_wishlist/(?P<pk>[0-9]+)/$', RemoveFromWishList.as_view(), name="delete"),
    url(r'^create_user/$', create_user, name="create"),#this link for usercreation
    url(r'^login/$', login_user),#user login
    url(r'^cerate_user_list/$', UserList.as_view(), name="create"),
    #url(r'^mall_search/$', MallViewSet, name="create"),
    url(r'^create_order/$', CreateOrder),
    #url(r'^product_details/(?P<pk>[0-9]+)/$', detailsProductView.as_view(), name="details"),
    #url(r'^profile_user_list/$', userprofileCreate.as_view(), name="create"),
    #url(r'^productdetails1/(?P<pk>[0-9]+)/$', ProductDetails)
    #url(r'^productdetails1/(?P<pk>[0-9]+)/$', details),
    #url(r'^prodetails/(?P<pk>[0-9]+)/$', productdetails.as_view(), name="details"),
    #url(r'^productdetails1/$', ProductDetails),
    #url(r'^add_cart/$', AddCart)

    #for test create_user
    #url(r'^viewarticle/(\d+)/$', viewArticle, name="viewArticle"),
    #url(r'^hellotest/$', hello, name="hello"),
    #url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
    #url(r'^product_details/(?P<pk>[0-9]+)/$',productdetails12345),#this api for viewing product details
    #url(r'^product1_details/(?P<pk>[0-9]+)/$', get),
    #url(r'^user_details/(?P<pk>[0-9]+)/$',detailsUserView),
    url(r'^user/(?P<pk>[0-9]+)/$', User_detail),#the given url is using for dispalying user information and updating user information 
    url(r'^product/(?P<pk>[0-9]+)/$', Product_view),# display product details api
    url(r'^shop/(?P<pk>[0-9]+)/$', Shop_details_view),#display shop details api
}
urlpatterns = format_suffix_patterns(urlpatterns)
