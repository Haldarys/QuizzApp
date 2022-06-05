<template>
  <div v-if="!adminMode">
    <div class="form-group">
      <label for="passwrd">Password</label>
      <input type="password" class="form-control" v-model="password" id="passwrd" placeholder="Password">
    </div>
    <button @click="login()" class="btn btn-primary">Submit</button>
  </div>
  <div v-else>
    <QuestionListVue></QuestionListVue>
  </div>
</template>

<script>
import quizApiService from "../services/QuizApiService";
import QuestionListVue from "../components/QuestionList.vue";
import QuestionEditionVue from "../components/QuestionEdition.vue";
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
      if (requestObject != undefined) {
        participationStorageService.saveToken(requestObject.data.token);
        this.adminMode = true;
      }
    },

  },
  components: {
    QuestionListVue,
    QuestionEditionVue,
  }
}

</script>