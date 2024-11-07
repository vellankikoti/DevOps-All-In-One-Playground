import React from 'react';
import DataList from './components/DataList';
import CreateForm from './components/CreateForm';

function App() {
  return (
    <div className="App">
      <h1>DevOps All-In-One Playground</h1>
      <CreateForm />
      <DataList />
    </div>
  );
}

export default App;
