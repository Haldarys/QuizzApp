import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
        return { status: error.response.status, data: error.message };
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", "questions/" + position);
  },
  getAllQuestions() {
    return this.call("get", "questions");
  },
  sendParticipation(playerName, scores) {
    return this.call("post", "participations", { "playerName": playerName, "answers": scores });
  },
  loginAdmin(password) {
    return this.call("post", "login", { "password": password });
  },
  saveQuestion(position, question, token = null) {
    return this.call("put", "questions/" + position, question, token);
  },
  addQuestion(question, token = null) {
    return this.call("post", "questions", question, token);
  },
  deleteQuestion(position, token = null) {
    return this.call("delete", "questions/" + position, "", token);
  },
};

