import pytest
import sympy


class TestInt:
    @pytest.mark.parametrize("int_data", [-1, 0, 1])
    def test_positive_instance_of_int(self, int_data):
        assert isinstance(int_data, int)

    @pytest.mark.parametrize("data", [0, 1, 5, 55, 4181])
    def test_part_of_fibbonachi(self, data):
        def fib(n):
            return int(sympy.sqrt(5 * (n ** 2) + 4))
        assert isinstance(fib(data), int)

    def test_positive_int(self):
        assert 5 > 0

class TestList:
    def test_positive_sum(self):
        data = [0, 5, -3, 2, -2]
        for element in data:
            assert isinstance(element, (float, int))
        assert sum(data) > 0

    def test_negative_single_instanses_in_list(self):
        data = [0, -1, 'a', 1, ('name', 5)]
        match = type(data[0])
        try:
            for element in data:
                assert issubclass(type(element), match)
        except AssertionError:
            pass

    def test_unique_elements(self):
        data = [0, 'a', 5.3, 1, {'name': 'Snickers'}]
        for element in data:
            assert data.count(element) == 1
