<template>
  <div class="questionsManager">
    <QuestionDisplay :question="currentQuestion" @clickOnAnswer="answerClickedHandler" />
  </div>
</template>

<script>
//
// Question dans QuestionDisplay à remplacer par la question en cours
//
import questionDisplay from "@/components/QuestionDisplay.vue";
import quizApiService from '../services/QuizApiService';
import participationStorageService from "../services/ParticipationStorageService";

export default {
  name: "QuestionsManager",
  data() {
    return {
      currentQuestion: {
      },
      currentScore: [],
      size: 0
    }
  },
  components: {
    QuestionDisplay: questionDisplay
  },
  async created() {
    var quizInfo = await quizApiService.getQuizInfo();
    this.size = quizInfo.data.size;
    await this.loadQuestionByPosition(1);
  },
  methods: {

    async loadQuestionByPosition(position) {
      let question = await quizApiService.getQuestion(position);
      this.currentQuestion = question.data;


    },
    async answerClickedHandler(position) {
      this.currentScore.push(position);
      let questionPosition = this.currentScore.length + 1;
      if (questionPosition > this.size) {
        this.endQuiz();
        return;
      }
      this.loadQuestionByPosition(questionPosition);
    },
    async endQuiz() {
      var participationResult = await quizApiService.sendParticipation(participationStorageService.getPlayerName(), this.currentScore);
      participationStorageService.saveParticipationScore(participationResult.data.score);
      this.$router.push('/scorePage');
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
