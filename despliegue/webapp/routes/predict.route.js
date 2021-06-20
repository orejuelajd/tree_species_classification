const express = require('express');
const controller = require('../controllers/predict.controller');

const router = express.Router();
router.post('/', controller.makePredictions);
module.exports = router;