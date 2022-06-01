<template>
  <div class="Question">
    <span>{{ question.title }}</span>
    <h1>{{ question.text }}</h1>
    <img v-if="question.image" :src="question.image" />
    <div class="answers">
      <a class="btn" v-for="(answer, index) in question.possibleAnswers" :key="answer.text" @click="$emit('answerSelected', index)">
        {{answer.text}}
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
  emits: ['answerSelected'],
};
</script>