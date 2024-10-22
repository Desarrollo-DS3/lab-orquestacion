const express = require('express');
const app = express();
const port = 80;

app.get('/duque', (req, res) => {
  res.json({ mensaje: "Hola! Este es el servicio de Santiago Duque. Estoy hecho en JS con Express" });
});

app.listen(port, () => {
  console.log(`El servicio está escuchando en http://localhost:${port}`);
});