<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <Header></Header>
  <div class="container-fluid">

    <RouterView />
  </div>

</template>

<style>
@import '@/assets/base.css';


#app {
  top: 0;
  width: 70%;
  margin: 0 auto;
  background-color: transparent;
  font-weight: normal;
  text-align: center;
  overflow-y: auto;
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

a,
.green {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.4s;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  body {
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    display: flex;
    font-size: larger;
    overflow-y: auto;
    height: 100vh;
  }

  i #app {
    display: flex;
    flex-flow: column;
    padding: 0 2rem;
  }

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  h1 {
    text-shadow: 1px 1px grey;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>

<script>
import Header from './components/Header.vue';
export default {
  components: {
    Header
  }
}
</script>