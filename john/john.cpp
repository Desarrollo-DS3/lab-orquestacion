#include "crow.h"

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/john")([](){
        crow::json::wvalue x;
        x["mensaje"] = "Respuesta desde el Servicio de John en C++";
        return x;
    });

    app.port(80).multithreaded().run();
}