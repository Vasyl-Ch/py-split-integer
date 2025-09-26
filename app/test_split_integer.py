import pytest


from app.split_integer import split_integer


def test_direct_examples_from_description() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (6, 2),
        (16, 4),
        (8, 1),
        (17, 4),
        (32, 6),
        (3, 5)
    ]
)
class TestSplitInteger:
    @pytest.fixture
    def parts(self, value: int, number_of_parts: int) -> list[int]:
        return split_integer(value=value, number_of_parts=number_of_parts)

    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
            value: int,
            number_of_parts: int,
            parts: list[int]
    ) -> None:
        assert sum(parts) == value
        assert len(parts) == number_of_parts

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self,
            value: int,
            number_of_parts: int,
            parts: list[int]
    ) -> None:
        if value % number_of_parts == 0:
            for elem in parts:
                assert elem == value // number_of_parts

    def test_should_return_part_equals_to_value_when_split_into_one_part(
            self,
            value: int,
            number_of_parts: int,
            parts: list[int]
    ) -> None:
        if number_of_parts == 1:
            assert parts[0] == value
            assert len(parts) == 1

    def test_parts_should_be_sorted_when_they_are_not_equal(
            self,
            parts: list[int]
    ) -> None:
        assert max(parts) - min(parts) <= 1
        assert all(isinstance(x, int) for x in parts)
        assert parts == sorted(parts)

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
            self,
            value: int,
            number_of_parts: int,
            parts: list[int]
    ) -> None:
        if value < number_of_parts:
            assert sum(parts) == value
            assert len(parts) == number_of_parts
            assert parts.count(0) == number_of_parts - value
