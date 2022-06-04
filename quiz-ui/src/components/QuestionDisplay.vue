<template>
  <div class="Question m-auto">
    <div class="">
      <span>{{ question.title }}</span>
      <h1>{{ question.text }}</h1>
    </div>
    <img class="img-fluid border border-2 border-light" v-if="question.image" :src="question.image" />
    <div class="answers">
      <a class="btn" v-for="(answer, index) in question.possibleAnswers" :key="answer.text"
        @click="$emit('clickOnAnswer', index + 1)">
        {{ answer.text }}
      </a>
    </div>
  </div>
</template>

<script>


export default {
  name: "QuestionDisplay",
  props: {
    question: Object,
  },
  data() {
    return {};
  },
  emits: ['clickOnAnswer'],
};
</script>