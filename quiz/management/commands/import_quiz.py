import json
from django.core.management.base import BaseCommand
from quiz.models import Question, Choice
from datetime import datetime

class Command(BaseCommand):
    help = 'Import quiz data from JSON file'

    def handle(self, *args, **kwargs):
        with open('quizzes-fixed.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            question_text = item['question']
            pub_date = datetime.strptime(item['published_date'], '%Y-%m-%d').date()
            q = Question.objects.create(text=question_text, published_date=pub_date)

            for choice in item['choices']:
                Choice.objects.create(
                    question=q,
                    text=choice['text'],
                    correct=choice['correct']
                )

        self.stdout.write(self.style.SUCCESS('Imported quiz data successfully.'))
