import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
 
 
@pytest.fixture
def inventory_page(driver):
    """Precondition: login sebagai standard_user dan berada di halaman inventori."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
 
    page = InventoryPage(driver)
    # Hard assertion untuk precondition: gagal login = tes tidak dilanjutkan
    assert "inventory" in page.get_current_url(), (
        f"Precondition gagal: tidak berada di halaman inventori, URL: {page.get_current_url()}"
    )
    return page
 
 
class TestInventory:
    """Kasus uji alur inventori dan keranjang belanja."""
 
    def test_add_backpack_to_cart(self, inventory_page):
        """
        TC-04: Add to Cart Flow.
        Expected: badge keranjang menampilkan teks '1' setelah Backpack ditambahkan.
        """
        inventory_page.add_backpack_to_cart()
 
        actual_count = inventory_page.get_cart_badge_count()
        assert actual_count == "1", (
            f"Badge keranjang tidak sesuai. Diharapkan: '1', Diterima: '{actual_count}'"
        )
 
    def test_logout_flow(self, driver, inventory_page):
        """
        TC-05: Logout Flow.
        Expected: kembali ke URL utama login dan tombol login tampil.
        """
        inventory_page.logout()
 
        login_page = LoginPage(driver)
 
        # Assertion 1: tombol login tampil (explicit wait menunggu redirect selesai)
        assert login_page.is_login_button_displayed() is True, (
            "Tombol login tidak tampil setelah logout!"
        )
 
        # Assertion 2: URL kembali ke halaman utama login
        expected_url = "https://www.saucedemo.com/"
        actual_url = login_page.get_current_url()
        assert actual_url == expected_url, (
            f"URL setelah logout tidak sesuai. Diharapkan: '{expected_url}', "
            f"Diterima: '{actual_url}'"
        )