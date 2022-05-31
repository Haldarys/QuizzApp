<template>
  <input type="text" v-model="username" />
  <p>{{ username }}</p>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return { username: '' }
  },
  async created() {
  }
}
</script>