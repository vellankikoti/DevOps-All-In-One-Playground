const app = require('./app');
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Backend server is running on http://localhost:${PORT}`);
});

