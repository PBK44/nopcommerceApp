import pytest


class Test_SearchCustomerByEmail_004:
    @pytest.mark.regression
    def test_searchCustomerByEmail(self):
        assert "python".upper() == "PYTHON"
        assert "pytest".capitalize() == "Pytest"
