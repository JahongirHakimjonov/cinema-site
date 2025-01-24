from rest_framework import serializers

from apps.hidaya.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "id",
            "answer",
        )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "book",
            "question",
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["answers"] = AnswerSerializer(instance.answers.all(), many=True).data
        return response
