import asyncio
from playwright.async_api import async_playwright, expect
from automation_ui.pages.login_page import LoginPage



async def test_petstore_login():
    async with async_playwright() as p:
        # Lanzamos el navegador en modo visible (headless=False)
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Instanciamos el Page Object
        login_page = LoginPage(page)

        # 1. Navegar a la URL objetivo
        url = "https://petstore.octoperf.com/actions/Catalog.action"
        print(f"Navegando a {url}...")
        await login_page.navigate_to_catalog(url)

        # 2. Abrir el formulario de inicio de sesión (usando Page Object)
        print("Abriendo el formulario de inicio de sesión...")
        await login_page.open_sign_in_form()

        # 3. Ingresar credenciales y hacer clic en login (usando Page Object)
        print("Ingresando credenciales...")
        await login_page.enter_credentials(username="j2ee", password="j2ee")

        # Hacer clic en el botón de inicio de sesión
        await login_page.click_login_button()
        # 4. Validar que el login fue exitoso de forma robusta
        print("Verificando inicio de sesión...")
        try:
            # En JPetStore, cuando te logueas con éxito, aparece un mensaje de bienvenida arriba
            welcome_message = page.locator("#WelcomeContent")
            await expect(welcome_message).to_contain_text("Welcome", timeout=5000)
            
            # Validación secundaria: El botón "Sign In" cambia a "Sign Out"
            sign_out_link = page.get_by_role("link", name="Sign Out")
            await expect(sign_out_link).to_be_visible(timeout=5000)
            
            print("✅ ¡Login exitoso y verificado correctamente!")

        except Exception as e:
            print(f"❌ La validación falló o los elementos no aparecieron: {e}")
            # Guardamos captura si algo sale mal
            await page.screenshot(path="debug_login_fail.png")

        # Espera un momento para observar el resultado antes de cerrar
        await asyncio.sleep(3)
        await browser.close()

# Ejecutar la función asíncrona
if __name__ == "__main__":
    asyncio.run(test_petstore_login())

