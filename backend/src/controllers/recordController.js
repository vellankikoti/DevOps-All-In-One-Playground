const db = require('../models/recordModel');

// Create a new record
exports.createRecord = async (req, res) => {
  const { name, description } = req.body;
  try {
    const newRecord = await db.create({ name, description });
    res.status(201).json(newRecord);
  } catch (error) {
    res.status(500).json({ error: 'Error creating record' });
  }
};

// Get all records
exports.getAllRecords = async (req, res) => {
  try {
    const records = await db.findAll();
    res.status(200).json(records);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching records' });
  }
};

// Get a specific record by ID
exports.getRecordById = async (req, res) => {
  try {
    const record = await db.findByPk(req.params.id);
    if (record) {
      res.status(200).json(record);
    } else {
      res.status(404).json({ error: 'Record not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error fetching record' });
  }
};

// Update a record by ID
exports.updateRecord = async (req, res) => {
  try {
    const record = await db.findByPk(req.params.id);
    if (record) {
      record.name = req.body.name;
      record.description = req.body.description;
      await record.save();
      res.status(200).json(record);
    } else {
      res.status(404).json({ error: 'Record not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error updating record' });
  }
};

// Delete a record by ID
exports.deleteRecord = async (req, res) => {
  try {
    const record = await db.findByPk(req.params.id);
    if (record) {
      await record.destroy();
      res.status(200).json({ message: 'Record deleted successfully' });
    } else {
      res.status(404).json({ error: 'Record not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Error deleting record' });
  }
};

