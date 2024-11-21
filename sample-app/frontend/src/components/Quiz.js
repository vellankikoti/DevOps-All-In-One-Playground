import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Progress from "../Progress";
import "./styles/quiz.css";

function Quiz() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const navigate = useNavigate();

  const questions = [
    { question: "What does CI stand for?", options: ["Continuous Integration", "Continuous Improvement", "Container Instance"], answer: 0 },
    { question: "What is a container?", options: ["Lightweight VM", "Namespace", "Both"], answer: 2 },
  ];

  const handleAnswer = (index) => {
    if (index === questions[currentQuestion].answer) {
      setScore(score + 1);
    }
    const nextQuestion = currentQuestion + 1;
    if (nextQuestion < questions.length) {
      setCurrentQuestion(nextQuestion);
    } else {
      navigate("/result", { state: { score, total: questions.length } });
    }
  };

  return (
    <div className="quiz">
      <h2>{questions[currentQuestion].question}</h2>
      {questions[currentQuestion].options.map((option, index) => (
        <button key={index} onClick={() => handleAnswer(index)} className="option-btn">
          {option}
        </button>
      ))}
      <Progress current={currentQuestion + 1} total={questions.length} />
    </div>
  );
}

export default Quiz;
