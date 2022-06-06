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
      <tbody>
        <tr class="" v-for="(question, index) in this.allQuestions" :key="question.position">
          <td>{{ question.position }}</td>
          <td>{{ question.title }}</td>
          <td>{{ question.text }}</td>
          <button class="editQuestion" @click="onEdit(question.position)" data-toggle="modal"
            data-target="#displayEditModal"><i class="fa fa-edit"></i></button>
          <button class="editQuestion" @click="printQuestion(question.position)"><i class="fa fa-eye"></i></button>
        </tr>
        <tr><i class="fa fa-plus" data-toggle="modal" data-target="#displayEditModal" aria-hidden="true"
            @click="onAdd()"></i>
        </tr>
      </tbody>
    </table>

  </div>
  <QuestionEditionVue :question="questionOnEdit" mode="edit" @clickOnSave="saveClickedHandler">
  </QuestionEditionVue>


</template>

<script>
import quizApiService from "../services/QuizApiService";
import QuestionEditionVue from "../components/QuestionEdition.vue";
import ParticipationStorageService from "../services/ParticipationStorageService";
export default {
  name: "QuestionList",
  data() {
    return { allQuestions: [], questionOnEdit: {}, mode: "" }
  },
  async created() {
    var questionResult = await quizApiService.getAllQuestions();
    if (questionResult.status != 200) {
      return;
    }
    this.allQuestions = questionResult.data;
    this.allQuestions = this.allQuestions.map(element => {
      return JSON.parse(element);
    });
    this.allQuestions.sort((a, b) => a.position - b.position);

  },
  methods: {
    printQuestion(position) {
      this.$router.push({ name: 'QuestionsAdmin', params: { position: position } })
    },
    onEdit(position) {
      this.mode = "edit";
      this.questionOnEdit = this.allQuestions[position - 1];
      this.questionOnEdit.possibleAnswers = this.questionOnEdit.possibleAnswers.map(element => {
        element.isCorrect = element.isCorrect == 1;
        return element;
      });
    },
    onAdd() {
      this.mode = "add";
      this.questionOnEdit = {
        title: "",
        text: "",
        position: 0,
        image: "",
        possibleAnswers: [
          { text: "", isCorrect: false },
          { text: "", isCorrect: false },
          { text: "", isCorrect: false },
          { text: "", isCorrect: false },
        ]

      }
    },
    async saveClickedHandler(position, question) {
      if (this.mode == "edit") {
        var saveResult = await quizApiService.saveQuestion(position, question, ParticipationStorageService.getToken());
      }
      else {
        var saveResult = await quizApiService.addQuestion(question, ParticipationStorageService.getToken());
      }

      if (saveResult.status == 200) {
        this.$router.go();
      }
    },

  },
  components: {
    QuestionEditionVue
  },


}
</script>