from rest_framework import serializers


from .models import Todo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    slug=serializers.SerializerMethodField()
    class Meta:
        model=Todo
        #exclude=['created_at']
        #fields=["todo_title","slug"]
        fields="__all__"

    def get_slug(self,obj):
        return slugify(obj.todo_title)


    def validate_todo_title(self,data):
        if(len(data)<3):
            raise serializers.ValidationError("length of title is small")
        return data

    def validate(self,validated_data):
        if(validated_data.get('todo_title')):
            todoTitle=validated_data['todo_title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not(regex.search(todoTitle) == None):
                raise serializers.ValidationError('todo title contains special character')
        return validated_data
