import random

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hidaya.models import Question
from apps.hidaya.serializers import QuestionSerializer


class QuestionList(APIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk=None, qty=None):
        questions = list(Question.objects.filter(is_active=True, book_id=pk))
        if qty is not None:
            qty = int(qty)
            questions = random.sample(questions, min(qty, len(questions)))
        serializer = self.serializer_class(questions, many=True)
        return Response(
            {
                "success": True,
                "message": "Questions list",
                "data": serializer.data
            }
        )


class TestResult(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        book = request.data.get('book')
        results_data = request.data.get('results')

        correct_count = 0
        incorrect_count = 0
        not_attempted_count = 0
        total_score = 0

        for result in results_data:
            question_id = result.get('question_id')
            answer_id = result.get('answer_id')
            try:
                question = Question.objects.get(id=question_id)
            except Question.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "message": "Question not found"
                    }
                )
            try:
                correct_answer = question.answers.get(is_correct=True)
            except question.answers.model.DoesNotExist:
                return Response(
                    {
                        "success": False,
                        "message": "Correct answer not found"
                    }
                )
            if answer_id is None:
                not_attempted_count += 1
            elif answer_id == correct_answer.id:
                correct_count += 1
                total_score += correct_answer.ball
            else:
                incorrect_count += 1

        return Response(
            {
                "success": True,
                "message": "Test result",
                "data": {
                    "book": book,
                    "correct_count": correct_count,
                    "incorrect_count": incorrect_count,
                    "not_attempted_count": not_attempted_count,
                    "total_score": total_score
                }
            }
        )
