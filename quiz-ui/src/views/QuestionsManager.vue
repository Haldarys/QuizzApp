<template>
  <div class="questionsManager">
    <QuestionDisplay
      :question="{
        'title': 'La géo tu connais ?',
        'text': 'Quelle est la capitale du Togo ?',
        'image': 'nope je vais pas écrire du binaire',
        'position': 1,
        'possibleAnswers': [{'text': 'Madrid'}, {'text': 'Lomé'}, {'text': 'Bonta'}, {'text': 'Tirana'}]
      }"
      @answerSelected="answerSelected"
    />
  </div>
</template>

<script>
//
// Question dans QuestionDisplay à remplacer par la question en cours
//
import QuestionDisplay from "@/components/QuestionDisplay.vue";

export default {
  name: "QuestionsManager",
  components: {
    QuestionDisplay
  },
  methods: {
        // Fonction appelée lors du clic sur une réponse
        answerSelected(index) {
            console.log("Answer selected: " + index)
        }
    }
};
</script>

<style>
@media (min-width: 1024px) {
  .questionsManager {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
