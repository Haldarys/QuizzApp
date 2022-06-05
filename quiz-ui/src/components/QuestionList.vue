<template>
  <div class="table-responsive">
    <table class="table  table-hover">
      <thead>
        <tr>
          <th scope="col">Position</th>
          <th scope="col">Titre</th>
          <th scope="col">Question</th>
        </tr>
      </thead>
      <tr class="" v-for="(question, index) in this.allQuestions" :key="question.position">
        <td>{{ question.position }}</td>
        <td>{{ question.title }}</td>
        <td>{{ question.text }}</td>
      </tr>
    </table>
  </div>

</template>

<script>
import quizApiService from "../services/QuizApiService";
export default {
  name: "QuestionList",
  data() {
    return { allQuestions: [] }
  },
  async created() {
    var questionResult = await quizApiService.getAllQuestions();
    this.allQuestions = questionResult.data;


    this.allQuestions = this.allQuestions.map(element => {
      return JSON.parse(element);
    });
    console.log(this.allQuestions);

  },
  methods: {

  }

}
</script>