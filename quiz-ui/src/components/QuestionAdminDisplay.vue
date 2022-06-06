<template>
  <div class="Question mx-auto">
    <span>{{ question.title }}</span>
    <h1>{{ question.text }}</h1>
    <img class="img-fluid imgQuiz border border-2 border-light" v-if="question.image" :src="question.image" />
    <div class="answers row mt-3">
      <div class="btn border border-1 col-lg-6 p-3" v-for="(answer, index) in question.possibleAnswers"
        :key="answer.text">
        {{ answer.text }}
        <div v-if="answer.isCorrect == 1"><i class="fa fa-check" aria-hidden="true"></i>
        </div>
      </div>
    </div>
    <div class="row">
      <button data-toggle="modal" data-target="#displayEditModal" aria-hidden="true">Edit</button>
      <button @click="$emit('clickOnDelete', question.position)">Delete</button>
    </div>
    <QuestionEdition :question="question" @clickOnSave="emitSave">
    </QuestionEdition>
  </div>
</template>

<script>
import questionEdition from './QuestionEdition.vue';

export default {
  name: "QuestionAdminDisplay",
  props: {
    question: Object,
  },
  data() {
    return {};
  },
  components: {
    QuestionEdition: questionEdition
  },
  methods: {
    emitSave(position, question) {
      this.$emit('clickOnSave', position, question);
    }
  }
};
</script>