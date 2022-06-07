<template>
  <!-- Modal -->
  <div class="modal fade" id="displayEditModal" tabindex="-1" role="dialog" aria-labelledby="editQuestion"
    aria-hidden="true">
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Edition de question</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="container-fluid">
            <div class="form-group">
              <label> Position</label>
              <input class="form-control" type="number" min="0" v-model="editQuestion.position" />
            </div>
            <label> Titre</label>
            <input class="form-control" type="text" v-model="editQuestion.title" />
          </div>
          <div class="form-group">
            <label> Texte </label>
            <input class="form-control" type="text" v-model="editQuestion.text" />
          </div>
          <div class="form-group">
            <label> Image </label>
            <ImageUpload class="form-control" @file-change="imageFileChangedHandler" />
            <img :src="this.editQuestion.image" class="img-fluid">
          </div>
          <div class="form-group">
            <label> Réponses possibles </label>
            <div v-for="(answer, index) in editQuestion.possibleAnswers" :key="answer.id">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" name="answerRadio" v-model="answer.isCorrect">
                <input type="text" class="form-control" v-model="answer.text" />
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" @click="$emit('clickOnSave', question.position, editQuestion)"
            data-dismiss="modal">Save
            changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import ImageUpload from './ImageUpload.vue';
export default {
  name: "QuestionEdition",
  created() {
    { }
  },
  props: {
    question: Object,
  },
  data() {
    return { editQuestion: {} }
  },
  methods: {
    imageFileChangedHandler(b64String) {
      this.editQuestion.image = b64String;
    }
  }
  ,
  emits: ['clickOnSave'],
  components: {
    ImageUpload
  },
  watch: {
    question: {
      immediate: true,
      handler(val, oldVal) {
        this.editQuestion = Object.assign({}, this.question);
      },
    }
  }
};
</script>