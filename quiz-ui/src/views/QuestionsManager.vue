<template>
  <div class="questionsManager">
    <QuestionDisplay :question="currentQuestion" @clickOnAnswer="answerClickedHandler" />
  </div>
</template>

<script>
//
// Question dans QuestionDisplay à remplacer par la question en cours
//
import QuestionDisplay from "@/components/QuestionDisplay.vue";
import QuizApiService from '../services/QuizApiService';
import ParticipationStorageService from "../services/ParticipationStorageService";

export default {
  name: "QuestionsManager",
  data() {
    return {
      currentQuestion: {
        'title': 'La géo tu connais ?',
        'text': 'Quelle est la capitale du Togo ?',
        'image': 'nope je vais pas écrire du binaire',
        'position': 1,
        'possibleAnswers': [{ 'text': 'Madrid' }, { 'text': 'Lomé' }, { 'text': 'Bonta' }, { 'text': 'Tirana' }]
      },
      currentScore: []
    }
  },
  components: {
    QuestionDisplay
  },
  methods: {

    async loadQuestionByPosition(position) {
      var question;
      try {
        question = await QuizApiService.getQuestion(position);
      }
      catch (e) {
        this.endQuiz();
        return;
      }
      this.currentQuestion = question.data;


    },
    async answerClickedHandler(position) {
      this.currentScore.push(position);
      let questionPosition = this.currentScore.length;
      this.loadQuestionByPosition(questionPosition);

    },
    async endQuiz(position) {

    }
  }
};
</script>

<style>
@media (min-width: 1024px) {
  .questionsManager {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
