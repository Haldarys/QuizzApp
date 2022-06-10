 <template>
  <div class="container">
    <div v-if="participated" class="row mt-2">
      <h1>Félicitation ! {{ this.playerName }}, vous avez eu {{ this.currentScore }} points !</h1>
    </div>

  </div>
  <div class="container mt-2">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Nom du joueur</th>
          <th scope="col">Score<i :class="sortScoreIcon" @click="sortByScore"></i></th>
          <th scope="col">Date<i :class="sortDateIcon" @click="sortByDate"></i></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.id">
          <td>{{ scoreEntry.playerName }}</td>
          <td>{{ scoreEntry.score }}</td>
          <td>{{ scoreEntry.date }}</td>
        </tr>
      </tbody>
    </table>

  </div>
  <div class="row d-inline">
    <router-link to="/" class="btn btn-secondary btn-lg">Return to Home</router-link>
  </div>

</template>


<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "../services/ParticipationStorageService";

export default {
  name: "ScorePage",
  data() {
    return { registeredScores: [], currentScore: 0, playerName: "", sortScore: 0, sortDate: 0, participated: false }
  },
  async created() {
    var quizInfo = quizApiService.getQuizInfo();
    var quizInfoResult = await quizInfo;
    this.registeredScores = quizInfoResult.data.scores;
    this.currentScore = participationStorageService.getParticipationScore();
    this.playerName = participationStorageService.getPlayerName();
    if (this.currentScore && this.playerName) {
      this.participated = true;
    }
    participationStorageService.clear();
  },
  computed: {
    sortDateIcon() {
      return {
        'fa fa-fw fa-sort': !this.sortDate,
        'fa fa-fw fa-sort-desc': this.sortDate == 1,
        'fa fa-fw fa-sort-asc': this.sortDate == -1
      }
    },
    sortScoreIcon() {
      return {
        'fa fa-fw fa-sort': !this.sortScore,
        'fa fa-fw fa-sort-desc': this.sortScore == 1,
        'fa fa-fw fa-sort-asc': this.sortScore == -1
      }
    },

  },
  methods: {
    sortByDate() {
      this.sortScore = 0;
      if (!this.sortDate) { this.sortDate = 1 }
      this.sortDate *= -1;
      this.registeredScores.sort((a, b) => {
        if (a.date > b.date) {
          return -1 * this.sortDate;
        }
        if (a.date < b.date) {
          return 1 * this.sortDate;
        }
        return 0;
      });

    },
    sortByScore() {
      this.sortDate = 0;
      if (!this.sortScore) { this.sortScore = 1 }
      this.sortScore *= -1;
      this.registeredScores.sort((a, b) => (b.score - a.score) * this.sortScore);
    },
  }

}

</script>