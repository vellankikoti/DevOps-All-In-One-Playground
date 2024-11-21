import axios from "axios";

const API_BASE_URL = "http://localhost:5000";

export const startQuiz = async (username) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/start/${username}`);
    return response.data;
  } catch (error) {
    console.error("Error starting the quiz:", error);
  }
};

export const fetchQuestion = async (username) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/question/${username}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching question:", error);
  }
};

export const submitAnswer = async (username, data) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/answer/${username}`, data);
    return response.data;
  } catch (error) {
    console.error("Error submitting answer:", error);
  }
};
