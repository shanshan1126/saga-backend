from .models import Applicant, ApplicationStatus
from .serializers import WritingTaskSerializer, CreateApplicantSerializer, WritingTaskStatusSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.utils import timezone

@api_view(["POST"])
def applicant_create(request, format=None):
    if request.method == "POST":
        serializer = CreateApplicantSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            new_application = ApplicationStatus(applicant=instance, handle_by=instance.first_choice)
            new_application.save()
            new_application.send_writing_task_email()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT"])
def applicant_writing_task(request, pk, format=None):
    try:
        applicant = Applicant.objects.get(pk=pk)
    except Applicant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = WritingTaskSerializer(applicant)
        return Response(serializer.data)

    elif request.method == "PUT":
        try:
            dept = request.data.get("handle_by")
            application = applicant.applications.get(handle_by=dept)
        except ApplicationStatus.DoesNotExist:
            return Response("Can not find corresponding application", status=status.HTTP_400_BAD_REQUEST)
        
        serializer = WritingTaskStatusSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["PUT", "DELETE"])
def file_detail(request, pk, format=None):
    try:
        applicant = Applicant.objects.get(pk=pk)
    except Applicant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    dept = request.data.get("handle_by")
    try:
        application = applicant.applications.get(handle_by=dept)
    except ApplicationStatus.DoesNotExist:
        return Response("Can not find corresponding application", status=status.HTTP_400_BAD_REQUEST)
        
    if (application.writing_task_ddl < timezone.now()):
        return Response("Writing task deadline has passed", status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PUT":
        serializer = WritingTaskStatusSerializer(application, data=request.data)
        if request.data.get("writing_task_file").size > 1024 * 1024 * 10:
            return Response("File size too large", status=status.HTTP_400_BAD_REQUEST)
        elif request.data.get("writing_task_file").content_type != "application/pdf":
            return Response("File type not supported", status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            application.status = "WRTIING_TASK_SUBMITTED"
            application.save()
            return Response(request.data.get("writing_task_file").name, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        application.writing_task_file.delete()
        application.status = "WRTIING_TASK_EMAIL_SENT"
        application.save()
        return Response(status=status.HTTP_204_NO_CONTENT)