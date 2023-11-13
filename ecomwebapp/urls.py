app_name = "ecomwebapp"
from django.urls import path,reverse_lazy
from ecomwebapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
from django.urls.base import reverse_lazy
urlpatterns = [
    # path('', views.home),
    path('',views.ProductView.as_view(),name = "home"),
    # path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.showcart, name='showcart'),
    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='plus_cart'),
    path('removecart/', views.remove_cart, name='remove_cart'),





    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='../templates/login.html',authentication_form=LoginForm), name='login'),
    # logout url below here loging out and redirecting it to the login page using next_page
    # path('logout/', auth_views.LogoutView.as_view( next_page='login' ), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='../templates/changepassword.html',form_class=MyPasswordChangeForm,success_url = '/passwordchangedone/'), name='changepassword'),
    #here success url is used cause after change of password is successfully done we need a success url where it will redirect user to the page.success url is basically after submitting password successfully redirect to a page(here page name is given).

    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name = '../templates/passwordchangedone.html'),name='passwordchangedone'),
    

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = '../templates/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name = '../templates/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = '../templates/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = '../templates/password_reset_complete.html'),name='password_reset_complete'),









    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='payment_done'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# in the 'accounts/login' url there auth view is used as view function and loginview class is used.After hitting the accounts/login url loginView class will run which is default provided by django but here to add bootstrap we have already created a loginform as authetication form thats why in the class based function we are assigning that loginform as authentication form and the location of the template which will be used.Like this LoginView.as_view(template_name='templates/login.html',authentication_form=LoginForm)
# success_url=reverse_lazy('ecomwebapp:password_reset_complete')