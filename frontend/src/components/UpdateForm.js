import React, { useState } from 'react';

function UpdateForm({ record, onUpdate }) {
  const [name, setName] = useState(record.name);
  const [description, setDescription] = useState(record.description);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(`http://localhost:5000/api/records/${record.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, description }),
    })
      .then(response => response.json())
      .then(data => {
        onUpdate(data);
        alert('Record updated successfully');
      })
      .catch(error => console.error('Error:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Update Record</h2>
      <label>Name:</label>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      <label>Description:</label>
      <textarea value={description} onChange={(e) => setDescription(e.target.value)} required />
      <button type="submit">Update</button>
    </form>
  );
}

export default UpdateForm;

