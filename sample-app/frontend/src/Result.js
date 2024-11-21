import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./styles/result.css";

function Result() {
  const location = useLocation();
  const navigate = useNavigate();
  const { score, total } = location.state || { score: 0, total: 0 };

  const restartQuiz = () => {
    navigate("/welcome");
  };

  return (
    <div className="result">
      <h1>Quiz Completed!</h1>
      <p>Your Score: {score} / {total}</p>
      <button onClick={restartQuiz} className="restart-btn">
        Restart Quiz
      </button>
    </div>
  );
}

export default Result;
