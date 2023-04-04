import pytest


class Test_003_AddCustomer:
    @pytest.mark.sanity
    def test_addCustomer(self):
        assert 1 in divmod(9, 5)
        assert "put" not in "this is pytest"
        assert [1, 2, 4] == [1, 2, 4]


