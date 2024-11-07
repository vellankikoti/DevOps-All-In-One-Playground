const express = require('express');
const bodyParser = require('body-parser');
const recordRoutes = require('./routes/recordRoutes');

const app = express();

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.use('/api/records', recordRoutes);

module.exports = app;

