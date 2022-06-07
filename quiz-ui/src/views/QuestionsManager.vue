<template>
  <div class="questionManager">
    <div v-if="adminPos == undefined">
      <QuestionDisplay :question="currentQuestion" @clickOnAnswer="answerClickedHandler" />
    </div>
    <div v-else>
      <QuestionAdminDisplay :question="currentQuestion" @clickOnSave="saveClickHandler"
        @clickOnDelete="deleteClickHandler" />

    </div>
  </div>
  <ErrorDisplay :error="error">
  </ErrorDisplay>
</template>

<script>
//
// Question dans QuestionDisplay à remplacer par la question en cours
//
import questionDisplay from "@/components/QuestionDisplay.vue";
import questionAdminDisplay from "@/components/QuestionAdminDisplay.vue";
import quizApiService from '../services/QuizApiService';
import participationStorageService from "../services/ParticipationStorageService";
import errorDisplay from "@/components/ErrorDisplay.vue";

export default {
  name: "QuestionsManager",
  data() {
    return {
      currentQuestion: {
      },
      currentScore: [],
      size: 0,
      adminPos: -1,
      error: {}
    }
  },
  components: {
    QuestionDisplay: questionDisplay,
    QuestionAdminDisplay: questionAdminDisplay,
    ErrorDisplay: errorDisplay
  },
  async created() {
    var quizInfo = await quizApiService.getQuizInfo();
    this.size = quizInfo.data.size;
    this.adminPos = this.$route.params.position;
    let router = this.$router;
    $('#errorPopUp').on('hidden.bs.modal', function () {
      router.push('/');
    });
    if (this.adminPos != undefined) {
      await this.loadQuestionByPosition(this.adminPos);
      return;
    }
    await this.loadQuestionByPosition(1);
  },
  methods: {

    async loadQuestionByPosition(position) {
      let question = await quizApiService.getQuestion(position);
      if (question.status == 200)
        this.currentQuestion = question.data;
      else {
        $("#errorPopUp").modal('toggle');
        this.error = question;
      }

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
    },
    async saveClickHandler(position, question) {
      var saveResult = await quizApiService.saveQuestion(position, question, participationStorageService.getToken());
      if (saveResult.status == 200) {
        this.$router.push('/adminPage');
      }
      else {
        $("#errorPopUp").modal('toggle');
        this.error = question;
      }
    },
    async deleteClickHandler(position) {
      if (!confirm("Êtes vous sûr de supprimer la question ?")) {
        return;
      }
      var deleteResult = await quizApiService.deleteQuestion(position, participationStorageService.getToken());
      if (deleteResult.status == 204) {
        this.$router.push('/adminPage');
      }
      else {
        $("#errorPopUp").modal('toggle');
        this.error = question;
      }
    }
  }
};
</script>

<style>
@media (min-width: 1024px) {
  .questionsManager {
    display: flex;
    align-items: center;
  }
}

.imgQuiz {
  max-height: 50vh;
}
</style>
