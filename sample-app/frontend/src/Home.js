import React from "react";
import { useNavigate } from "react-router-dom";
import "./styles/home.css";

function Home() {
  const navigate = useNavigate();

  const handleStart = () => {
    navigate("/welcome");
  };

  return (
    <div className="home">
      <h1>Welcome to the DevOps Quiz Platform</h1>
      <p>Test your knowledge on DevOps tools and practices!</p>
      <button onClick={handleStart} className="start-btn">
        Start Quiz
      </button>
    </div>
  );
}

export default Home;
