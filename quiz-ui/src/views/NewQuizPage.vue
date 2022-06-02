<template>
  <label for="username"> Saisissez votre nom</label>
  <input type="text" v-model="username" id="username" />
  <p>{{ username }}</p>
  <button @click="launchNewQuiz()"> Go </button>
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