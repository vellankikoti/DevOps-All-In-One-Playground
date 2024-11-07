import React, { useState } from 'react';

function CreateForm() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Post to backend API
    fetch('http://localhost:5000/api/records', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, description }),
    })
      .then(response => response.json())
      .then(data => {
        setName('');
        setDescription('');
        alert('Record created successfully');
      })
      .catch(error => console.error('Error:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Create a New Record</h2>
      <label>Name:</label>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      <label>Description:</label>
      <textarea value={description} onChange={(e) => setDescription(e.target.value)} required />
      <button type="submit">Create</button>
    </form>
  );
}

export default CreateForm;

