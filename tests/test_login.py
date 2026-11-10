import pytest
from pages.login_page import LoginPage


class TestLogin:
    """Kumpulan kasus uji fungsional fitur autentikasi pengguna."""

    def test_login_positive_valid_user(self, driver):
        """
        TC-01: Verifikasi login berhasil menggunakan kredensial yang valid.
        Expected: Berpindah ke URL inventory dan elemen logo Swag Labs tampil.
        """
        login_page = LoginPage(driver)

        # Arrange & Act
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Assertions
        expected_inventory_url = "https://www.saucedemo.com/inventory.html"
        actual_url = login_page.get_current_url()

        # Assertion 1: validasi perubahan URL
        assert actual_url == expected_inventory_url, (
            f"Kegagalan URL: Diharapkan '{expected_inventory_url}', "
            f"tetapi berada di '{actual_url}'"
        )

        # Assertion 2: validasi elemen penanda dashboard
        assert login_page.is_dashboard_displayed() is True, (
            "Dashboard Swag Labs logo tidak tampil setelah submit login valid!"
        )

    def test_login_negative_locked_out_user(self, driver):
        """
        TC-02: Verifikasi penanganan login user yang diblokir (locked out).
        Expected: Muncul error 'Epic sadface: Sorry, this user has been locked out.'
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = login_page.get_error_message()

        assert expected_error in actual_error, (
            f"Pesan error tidak sesuai. Diharapkan: '{expected_error}', "
            f"Diterima: '{actual_error}'"
        )

    def test_login_negative_empty_password(self, driver):
        """
        TC-03: Verifikasi validasi form ketika password dikosongkan.
        Expected: Muncul pesan kesalahan password wajib diisi.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "")

        expected_error = "Epic sadface: Password is required"
        actual_error = login_page.get_error_message()