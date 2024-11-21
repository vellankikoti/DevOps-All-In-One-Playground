import React, { useState, useEffect } from "react";
import axios from "axios";

const Challenge = ({ user }) => {
  const [question, setQuestion] = useState(null);
  const [answer, setAnswer] = useState("");
  const [feedback, setFeedback] = useState("");

  useEffect(() => {
    fetchQuestion();
  }, []);

  const fetchQuestion = async () => {
    try {
      const response = await axios.post("http://localhost:5000/get-challenge", {
        topic: "Linux", // Default topic for now
      });
      setQuestion(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  const submitAnswer = async () => {
    try {
      const response = await axios.post("http://localhost:5000/submit-answer", {
        id: question.id,
        email: user.email,
        answer,
      });
      setFeedback(response.data.message);
      if (response.data.score) fetchQuestion();
    } catch (err) {
      setFeedback(err.response?.data?.error || "Something went wrong.");
    }
  };

  return (
    <div>
      <h2>Welcome, {user.name}!</h2>
      {question ? (
        <div>
          <h3>{question.question}</h3>
          {question.options.map((opt, idx) => (
            <div key={idx}>
              <input
                type="radio"
                id={opt}
                name="answer"
                value={opt}
                onChange={(e) => setAnswer(e.target.value)}
              />
              <label htmlFor={opt}>{opt}</label>
            </div>
          ))}
          <button onClick={submitAnswer}>Submit Answer</button>
          {feedback && <p>{feedback}</p>}
        </div>
      ) : (
        <p>Loading question...</p>
      )}
    </div>
  );
};

export default Challenge;
