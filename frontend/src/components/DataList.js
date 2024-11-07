import React, { useEffect, useState } from 'react';

function DataList() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/records')
      .then(response => response.json())
      .then(data => setRecords(data))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div>
      <h2>Records List</h2>
      {records.length > 0 ? (
        <ul>
          {records.map((record) => (
            <li key={record.id}>
              <h3>{record.name}</h3>
              <p>{record.description}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No records found.</p>
      )}
    </div>
  );
}

export default DataList;

