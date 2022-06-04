<template>
  <div class="container">
    <div v-if="data" class="row">
      <div class="col-4">
        <h1>Congratulation ! {{ this.playerName }} You got {{ this.currentScore }}</h1>
      </div>
    </div>

  </div>
  <div class="container">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#<i class="fa fa-fw fa-sort"></i></th>
          <th scope="col">Player name<i class="fa fa-fw fa-sort"></i></th>
          <th scope="col">Score<i class="fa fa-fw fa-sort" @click="sortByScore"></i></th>
          <th scope="col">Date<i class="fa fa-fw fa-sort" @click="sortByDate"></i></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
          <th scope="row">1</th>
          <td>{{ scoreEntry.playerName }}</td>
          <td>{{ scoreEntry.score }}</td>
          <td>{{ scoreEntry.date }}</td>
        </tr>
      </tbody>
    </table>

  </div>
  <div class="row d-inline">
    <button @click="sortByDate">Sort by date</button>
    <button @click="sortByScore">Sort by score</button>
    <router-link to="/">Return to Home</router-link>
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
    },
    sortByScore() {
      this.registeredScores.sort((a, b) => b.score - a.score);
    },
  }

};
</script>