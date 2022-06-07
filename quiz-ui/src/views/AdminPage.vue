<template>
  <div>
    <div v-if="!adminMode">
      <div class="form-group">
        <label for="passwrd">Password</label>
        <input type="password" class="form-control" v-model="password" id="passwrd" placeholder="Password">
        <p class="text-danger">{{ msg }}</p>
      </div>
      <button @click="login()" class="btn btn-primary">Submit</button>
    </div>
    <div v-else>
      <QuestionList></QuestionList>
    </div>
  </div>
</template>

<script>
import quizApiService from "../services/QuizApiService";
import questionList from "../components/QuestionList.vue";
import participationStorageService from "../services/ParticipationStorageService";
export default {
  name: "AdminPage",
  data() {
    return { password: "", adminMode: false, msg: '' };
  },
  created() {
    if (participationStorageService.getToken()) {
      this.adminMode = true;
    }
  },
  methods: {
    async login() {
      var requestObject = await quizApiService.loginAdmin(this.password);
      if (requestObject.status == 200) {
        participationStorageService.saveToken(requestObject.data.token);
        this.adminMode = true;
      }
      else if (requestObject.status == 401) {
        this.msg = "Mauvais mot de passe";
      }
    },

  },
  components: {
    QuestionList: questionList,
  }
}

</script>