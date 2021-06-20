const express = require('express');
const cors = require('cors');
const app = express();

const corsOptions = {
  origin: '*',
};

app.use(express.json());
app.use(cors(corsOptions));
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {
  res.send('Servicio web para clasificación de arboles')
});

const predictRouter = require('./routes/predict.route')
app.use('/predict', predictRouter);

PORT = process.env.PORT || 3000;
app.listen(PORT);
console.log(`Servidor corriendo en http://localhost:${PORT}`);