from playwright.async_api import Page


class LoginPage:
    """Page Object para el formulario de login del Pet Store."""

    # Selectores (locators)
    SIGN_IN_LINK = "Sign In"
    USERNAME_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_BUTTON = 'input[name="signon"]'

    def __init__(self, page: Page):
        self.page = page

    async def navigate_to_catalog(self, url: str) -> None:
        """Navegar a la página del catálogo."""
        await self.page.goto(url)

    async def open_sign_in_form(self) -> None:
        """Hacer clic en el enlace de 'Sign In' para abrir el formulario de login."""
        await self.page.get_by_role("link", name=self.SIGN_IN_LINK).click()

    async def enter_credentials(self, username: str, password: str) -> None:
        """Ingresar las credenciales en los campos del formulario."""
        await self.page.locator(self.USERNAME_INPUT).fill(username)
        
        # Limpiamos la contraseña por defecto si el formulario ya trae algo escrito
        await self.page.locator(self.PASSWORD_INPUT).click()
        await self.page.locator(self.PASSWORD_INPUT).fill(password)

    async def click_login_button(self) -> None:
        """Hacer clic en el botón de inicio de sesión."""
        await self.page.locator(self.LOGIN_BUTTON).click()