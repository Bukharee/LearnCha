from ast import Sub
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import Subject, Books, Quiz, Answer


class SubjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ["title", "description"]


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ["title", "book", "cover", "grade", "subject"]


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["question", "correct", "first_option",
                  "second_option", "third_option"]
