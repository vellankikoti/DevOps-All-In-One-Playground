import React from "react";
import { useNavigate } from "react-router-dom";
import "./styles/quiz.css";

function Welcome() {
  const navigate = useNavigate();

  const startQuiz = () => {
    navigate("/quiz");
  };

  return (
    <div className="welcome">
      <h1>Ready for the Challenge?</h1>
      <button onClick={startQuiz} className="start-btn">
        Start Quiz
      </button>
    </div>
  );
}

export default Welcome;
