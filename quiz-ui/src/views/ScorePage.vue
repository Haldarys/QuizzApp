<template>
  <div class="container">
    <div class="row">
      <div class="col-4">
        <h1>Congratulation ! {{ this.playerName }} You got {{ this.currentScore }}</h1>
      </div>
    </div>
    <div class="row">
      <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
      </div>
    </div>
    <div class="row d-inline">
      <button @click="sortByDate">Sort by date</button>
      <button @click="sortByScore">Sort by score</button>
      <router-link to="/">Return to Home</router-link>
    </div>

  </div>
</template>


<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService";

export default {
  name: "ScorePage",
  data() {
    return { registeredScores: [], currentScore: 0, playerName: "" }
  },
  async created() {
    var quizInfo = quizApiService.getQuizInfo();
    var quizInfoResult = await quizInfo;
    this.registeredScores = quizInfoResult.data.scores;
    this.currentScore = participationStorageService.getParticipationScore();
    this.playerName = participationStorageService.getPlayerName();
  },
  methods: {
    sortByDate() {
      this.registeredScores.sort((a, b) => {

        if (a.date > b.date) {
          return -1;
        }
        if (a.date < b.date) {
          return 1;
        }
        return 0;
      });
      console.log(this.registeredScores);
    },
    sortByScore() {
      this.registeredScores.sort((a, b) => b.score - a.score);
      console.log(this.registeredScores);
    },
  }

};
</script>