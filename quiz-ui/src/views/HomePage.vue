<template>
  <h1 class="mt-5">Bienvenue dans le Quizz !</h1>
  <router-link to="/start-new-quiz-page" class="mt-5 btn btn-secondary btn-lg">Démarrer le quiz !
  </router-link>

</template>


<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return { registeredScores: [] }
  },
  async created() {
    var quizInfo = quizApiService.getQuizInfo();
    var quizInfoResult = await quizInfo;
    this.registeredScores = quizInfoResult.data.scores;
  }
};
</script>