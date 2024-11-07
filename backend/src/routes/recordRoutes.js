const express = require('express');
const router = express.Router();
const recordController = require('../controllers/recordController');

// Create a new record
router.post('/', recordController.createRecord);

// Get all records
router.get('/', recordController.getAllRecords);

// Get a specific record by ID
router.get('/:id', recordController.getRecordById);

// Update a record by ID
router.put('/:id', recordController.updateRecord);

// Delete a record by ID
router.delete('/:id', recordController.deleteRecord);

module.exports = router;

