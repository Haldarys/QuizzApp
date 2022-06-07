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
          <button class="editQuestion" @click="onEdit(index)" data-toggle="modal" data-target="#displayEditModal"><i
              class="fa fa-edit"></i></button>
          <button class="editQuestion" @click="printQuestion(question.position)"><i class="fa fa-eye"></i></button>
        </tr>
        <tr><i class="fa fa-plus" data-toggle="modal" data-target="#displayEditModal" aria-hidden="true"
            @click="onAdd()"></i>
        </tr>
      </tbody>
    </table>

  </div>
  <QuestionEdition :question="questionOnEdit" mode="edit" @clickOnSave="saveClickedHandler">
  </QuestionEdition>


</template>

<script>
import quizApiService from "../services/QuizApiService";
import questionEdition from "../components/QuestionEdition.vue";
import participationStorageService from "../services/ParticipationStorageService";
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
    onEdit(index) {
      this.mode = "edit";
      this.questionOnEdit = this.allQuestions[index];
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
        var saveResult = await quizApiService.saveQuestion(position, question, participationStorageService.getToken());
      }
      else {
        var saveResult = await quizApiService.addQuestion(question, participationStorageService.getToken());
      }

      if (saveResult.status == 200) {
        this.$router.go();
      }
    },

  },
  components: {
    QuestionEdition: questionEdition
  },


}
</script>