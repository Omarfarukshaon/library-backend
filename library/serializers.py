from rest_framework import serializers
from .models import Book, BookIssue, IssueLog

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = '__all__'

class IssueLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueLog
        fields = '__all__'
