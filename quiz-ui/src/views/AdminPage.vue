<template>
  <div v-if="!adminMode">
    <div class="form-group">
      <label for="passwrd">Password</label>
      <input type="password" class="form-control" v-model="password" id="passwrd" placeholder="Password">
    </div>
    <button @click="login()" class="btn btn-primary">Submit</button>
  </div>
  <div v-else>
    <QuestionList></QuestionList>
  </div>
</template>

<script>
import quizApiService from "../services/QuizApiService";
import questionList from "../components/QuestionList.vue";
import participationStorageService from "../services/ParticipationStorageService";
export default {
  name: "AdminPage",
  data() {
    return { password: "", adminMode: false };
  },
  created() {
    if (participationStorageService.getToken()) {
      this.adminMode = true;
    }
  },
  methods: {
    async login() {
      var requestObject = await quizApiService.loginAdmin(this.password);
      console.log(requestObject);
      if (requestObject.status == 200) {
        participationStorageService.saveToken(requestObject.data.token);
        this.adminMode = true;
      }
    },

  },
  components: {
    QuestionList: questionList,
  }
}

</script>