import os
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Orders Microservice",
    description="API de gestión de órdenes para prueba técnica DevOps",
    version="1.0.0"
)

# Configuración mediante variables de entorno (Inyectadas desde Docker/ConfigMap)
PORT = int(os.getenv("APP_PORT", "8080"))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.get("/health")
def health_check():
    """Endpoint de salud para Liveness/Readiness Probes de Kubernetes."""
    return {
        "status": "healthy",
        "environment": ENVIRONMENT
    }


@app.get("/api/v1/orders")
def get_orders():
    """Endpoint principal de consulta de órdenes."""
    return {
        "environment": ENVIRONMENT,
        "orders": [
            {"id": 101, "item": "Servidor Nube AWS", "status": "processed", "amount": 120.0},
            {"id": 102, "item": "Licencia API Gateway", "status": "pending", "amount": 450.0}
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)