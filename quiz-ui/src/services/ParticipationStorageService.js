export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("participationScore", participationScore)// todo : implement
  },
  getParticipationScore() {
    return window.localStorage.getItem("participationScore");
  },
  saveToken(token) {
    window.localStorage.setItem("token", token)// todo : implement
  },
  getToken() {
    return window.localStorage.getItem("token");
  }
};