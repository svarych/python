import pytest


class TestOne:
    def test0(self):
        assert True

    def test1(self):
        assert True

    @pytest.mark.jenkins
    def test2(self):
        assert True
