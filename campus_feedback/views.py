from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count

from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from campus_feedback.serializers import UserSerializer,FeedbackSerializer
from campus_feedback.models import Feedback
from campus_feedback.permissions import IsUser

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data = form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_user(** cleaned_data)

            serial_inst =  UserSerializer(instance)

            return Response(data=serial_inst.data)

        else:return Response(data=serializer.errors)

class FeedbackListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = Feedback.objects.filter(student=request.user)

        serializer = FeedbackSerializer(qs,many=True)

        return Response(data=serializer.data)

    def post(self,request):

        form_data = request.data

        serializer = FeedbackSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(student=request.user)

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)

class FeedbackRetrieveUpdateDelete(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsUser]

    def get(self,request,pk=None):

        instance = get_object_or_404(Feedback,id=pk)

        self.check_object_permissions(request,instance)

        serializer = FeedbackSerializer(instance)

        return Response(data=serializer.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(Feedback,id=pk)
        
        self.check_object_permissions(request,instance)

        form_data = request.data
        
        serializer = FeedbackSerializer(data=form_data,instance=instance)

        if serializer.is_valid():

            qs = serializer.save()

            serial = FeedbackSerializer(qs)

            return Response(data=serial.data)

        else: return Response(data=serializer.errors)

    def delete(self, request, pk=None):

        instance = get_object_or_404(Feedback, id=pk)

        self.check_object_permissions(request, instance)
        
        instance.delete()

        return Response({"message": "Feedback deleted successfully"})

class FeedbackSummaryView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        response_data = {
            "total_feedback": 0,
            "sentiment_summary": [],
            "category_summary": []
        }

        feedback_queryset = Feedback.objects.filter(student=request.user)

        if feedback_queryset:

            total_feedback = feedback_queryset.count()

            sentiment_summary = feedback_queryset.values("sentiment").annotate(total=Count("id"))

            category_summary = feedback_queryset.values("category").annotate(total=Count("id"))

            response_data["total_feedback"] = total_feedback
            response_data["sentiment_summary"] = sentiment_summary
            response_data["category_summary"] = category_summary

        return Response(data=response_data)
        