<template>
  <div class="Question mx-auto">
    <span>{{ question.title }}</span>
    <h1>{{ question.text }}</h1>
    <img class="img-fluid imgQuiz border border-2 border-light" v-if="question.image" :src="question.image" />
    <div class="answers row mt-3">
      <a class="btn border border-1 col-lg-6 p-3" v-for="(answer, index) in question.possibleAnswers" :key="answer.text"
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