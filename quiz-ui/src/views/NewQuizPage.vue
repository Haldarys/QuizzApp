<template>
  <form>
    <div class="form-group">
      <label for="username" class="mt-1"> Saisissez votre nom</label>
      <input type="text" v-model="username" id="username" class="form-control mt-1" placeholder="..." />
      <button @click="launchNewQuiz()" class="btn btn-primary btn-lg mt-1"> Go </button>
    </div>
  </form>
</template>

<script>

import participationStorageService from "@/services/ParticipationStorageService";

export default {
  name: "HomePage",
  data() {
    return { username: '' }

  },
  async created() {
    if (participationStorageService.getPlayerName() == null) return;
    this.username = participationStorageService.getPlayerName();
  },
  methods: {
    launchNewQuiz() {
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
  }
}
</script>