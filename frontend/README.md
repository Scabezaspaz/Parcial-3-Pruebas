# TicketFast — Sistema de Reserva de Boletos

## Descripcion
Sistema de pruebas de integracion, sistema y E2E para la plataforma TicketFast.

## Requisitos
- Python 3.13
- Docker y Docker Compose
- Node.js y Angular CLI
- Playwright

## Comandos para ejecutar cada tipo de prueba

### 1. Levantar la infraestructura
```bash
docker-compose -f docker-compose.test.yml up -d --build
```

### 2. Pruebas de integracion
```bash
pytest tests/integration/test_api_integracion.py -v
```

### 3. Pruebas de sistema
```bash
pytest tests/system/test_sistema_e2e.py -v
```

### 4. Pruebas E2E con Playwright
```bash
cd frontend && ng serve
```
```bash
pytest tests/e2e/test_reservas_e2e.py -v
```

### 5. Todas las pruebas
```bash
pytest tests/ -v
```