from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from campus_feedback.views import SignUpView
from campus_feedback.views import FeedbackListCreateView,FeedbackRetrieveUpdateDelete
from campus_feedback.views import FeedbackSummaryView

urlpatterns = [

    path('signup/',SignUpView.as_view()),
    path('signin/',ObtainAuthToken.as_view()),

    path('feedbacks/',FeedbackListCreateView.as_view()),
    path('feedbacks/<int:pk>/',FeedbackRetrieveUpdateDelete.as_view()),

    path('summary/',FeedbackSummaryView.as_view()),
]