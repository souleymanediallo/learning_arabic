import random
from django.shortcuts import render, get_object_or_404
from .models import Word, QuizHistory, QuizScore

def quiz(request):
    # Vérifie s'il y a au moins 4 mots pour générer un quiz
    mots = list(Word.objects.all())

    # Lors de l'affichage initial (GET)
    if request.method == "GET":
        # Sélectionne un mot aléatoire comme question
        mot_question = random.choice(mots)

        # Propose 3 mauvaises réponses
        mauvaises_reponses = random.sample(
            [mot.french_word for mot in mots if mot != mot_question], 3
        )
        options = mauvaises_reponses + [mot_question.french_word]
        random.shuffle(options)

        # Stocke l'ID du mot question dans la session pour le récupérer après soumission
        request.session['mot_question_id'] = str(mot_question.id)

        return render(request, "learning/quiz.html", {"mot": mot_question, "options": options})

    # Lors de la soumission du formulaire (POST)
    elif request.method == "POST":
        # Récupère l'ID du mot question depuis la session
        mot_question_id = request.session.get('mot_question_id')
        if not mot_question_id:
            return render(request, "learning/quiz_error.html", {
                "message": "Une erreur est survenue. Veuillez recommencer le quiz."
            })

        # Récupère le mot question correspondant à l'ID
        mot_question = get_object_or_404(Word, id=mot_question_id)
        reponse = request.POST.get("reponse")

        # Vérifie si la réponse est correcte
        is_correct = (reponse == mot_question.french_word)

        # Enregistre l'historique de la tentative
        QuizHistory.objects.create(
            user=request.user,
            word=mot_question,
            is_correct=is_correct
        )

        # Met à jour le score de l'utilisateur
        quiz_score, created = QuizScore.objects.get_or_create(user=request.user)
        quiz_score.update_score(is_correct)

        # Message pour l'utilisateur
        message = "Bonne réponse !" if is_correct else "Faux, essaye encore !"
        return render(request, "learning/quiz_result.html", {"message": message})
