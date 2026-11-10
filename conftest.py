import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Inisialisasi browser Google Chrome untuk setiap fungsi pengujian."""
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")
    # Opsional: matikan popup password manager Chrome yang bisa mengganggu klik
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    })

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
    