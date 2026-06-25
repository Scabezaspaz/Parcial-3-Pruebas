import httpx

BASE_URL = "http://localhost:8001"

def test_flujo_completo_sistema():
    # 1. POST reserva zona General cantidad 3
    response_post = httpx.post(f"{BASE_URL}/reservas/sistema-evento-xyz", json={
        "cliente_email": "sistema@correo.com",
        "zona": "General",
        "cantidad": 3
    })
    assert response_post.status_code == 201

    # 2. GET resumen del evento
    response_get = httpx.get(f"{BASE_URL}/reservas/sistema-evento-xyz/resumen")
    assert response_get.status_code == 200

    # 3. Validar total_recaudado = 3 x 50.000 = 150.000
    data = response_get.json()
    assert data["total_recaudado"] == 150000