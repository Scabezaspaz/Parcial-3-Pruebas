from src.database.models import ReservaDB

def test_crear_reserva_valida(client_con_bd, db_session):
    response = client_con_bd.post("/reservas/concierto-2026", json={
        "cliente_email": "test@correo.com",
        "zona": "VIP",
        "cantidad": 2
    })

    assert response.status_code == 201

    reserva = db_session.query(ReservaDB).filter(
        ReservaDB.cliente_email == "test@correo.com"
    ).first()
    assert reserva is not None
    assert reserva.cliente_email == "test@correo.com"