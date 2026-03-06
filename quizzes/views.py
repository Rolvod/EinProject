from django.shortcuts import render, get_object_or_404
from .models import Quiz, Answer, Question
from django.contrib.auth.decorators import login_required

@login_required
def quizzes_page(request):
    quizzes = Quiz.objects.filter(public=True)
    return render(request, 'quizzes/quizzes_page.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, id):
    quiz = get_object_or_404(Quiz, id=id)
    
    if request.method == 'POST':
        score = 0
        for question in quiz.questions.all():
            selected_answer_id = request.POST.get(f'q_{question.id}')
            if selected_answer_id:
                ans = Answer.objects.get(id=selected_answer_id)
                if ans.is_correct:
                    score += 1
        
        if str(quiz.id) not in request.user.completed_quizzes:
            request.user.points += (score * 10)
            request.user.completed_quizzes[str(quiz.id)] = score
            request.user.save()
            message = f"Поздравляем! Вы получили {score * 10} баллов."
        else:
            message = "Вы уже проходили этот тест. Баллы не начислены."

        return render(request, 'quizzes/result.html', {
            'quiz': quiz, 
            'score': score, 
            'message': message
        })

    return render(request, 'quizzes/current_quiz.html', {'quiz': quiz})