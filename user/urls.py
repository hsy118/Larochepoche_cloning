from django.urls import path
<<<<<<< HEAD
from .views import SignUpView, SignInView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view())

]
=======
from .views import SignUpView, AccountCheckView, SignInView, UserInfoView, LikeProductView, CartProductView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/accountcheck', AccountCheckView.as_view()),
    path('/userinfo', UserInfoView.as_view()),
    path('/likeproduct', LikeProductView.as_view()),
    path('/cartproduct', CartProductView.as_view())
]

>>>>>>> 0438d5d890ff30646664be8b5b74678c6a4c8a6b
