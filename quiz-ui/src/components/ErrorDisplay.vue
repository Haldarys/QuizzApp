<template>
  <div id="errorPopUp" class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog"
    aria-labelledby="myLargeModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Edition de question</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          Error {{ this.error.status }} {{ this.error.data }}
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Return to home</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "QuestionDisplay",
  props: {
    error: Object,
  },
  data() {
    return {};
  }
};
</script>