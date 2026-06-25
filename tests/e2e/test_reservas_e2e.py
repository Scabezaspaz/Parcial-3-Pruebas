import re
from playwright.sync_api import Page, expect

def test_reserva_vip_muestra_total(page: Page):
    # 1. Navegar a la interfaz de reservas
    page.goto("http://localhost:4200/reservas")

    # 2. Llenar el formulario
    page.get_by_test_id("input-email-cliente").fill("cliente@correo.com")
    page.get_by_test_id("select-zona-evento").select_option("VIP")
    page.get_by_test_id("input-cantidad-asientos").fill("1")

    # 3. Clic en confirmar
    page.get_by_test_id("btn-confirmar-reserva").click()

    # 4. Verificar que el resumen muestre 150.000
    expect(page.get_by_test_id("seccion-resumen-total")).to_contain_text("150.000")