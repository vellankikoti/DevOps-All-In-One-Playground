import React from "react";
import "./styles/progress.css";

function Progress({ current, total }) {
  const percentage = (current / total) * 100;

  return (
    <div className="progress-container">
      <div className="progress-bar" style={{ width: `${percentage}%` }}>
        {current}/{total}
      </div>
    </div>
  );
}

export default Progress;
