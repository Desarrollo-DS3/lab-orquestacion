const http = require("node:http");

const desiredPort = 80;

const server = http.createServer((req, res) => {
  console.log("request received!");

  res.setHeader("Content-Type", "application/json");

  const jsonResponse = {
    mensaje: "Respuesta desde el Servicio de Sebastian en Node.js",
  };

  res.end(JSON.stringify(jsonResponse));
});

server.listen(desiredPort, () => {
  console.log(`Servidor corriendo en http://localhost:${desiredPort}`);
});