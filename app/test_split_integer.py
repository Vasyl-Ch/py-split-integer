import pytest


from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (6, 2),
        (16, 4),
        (8, 1),
        (17, 4),
        (32, 6)
    ]
)
class TestSplitInteger:
    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        assert sum(
            split_integer(
                value=value,
                number_of_parts=number_of_parts
            )
        ) == value

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        parts = split_integer(value=value, number_of_parts=number_of_parts)
        if value % number_of_parts == 0:
            for elem in parts:
                assert elem == value // number_of_parts

    def test_should_return_part_equals_to_value_when_split_into_one_part(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        parts = split_integer(value=value, number_of_parts=number_of_parts)
        if number_of_parts == 1:
            assert parts[0] == value
            assert len(parts) == 1

    def test_parts_should_be_sorted_when_they_are_not_equal(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        parts = split_integer(value=value, number_of_parts=number_of_parts)
        assert parts == sorted(parts)

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
            self,
            value: int,
            number_of_parts: int
    ) -> None:
        parts = split_integer(value=value, number_of_parts=number_of_parts)
        if value < number_of_parts:
            assert sum(parts) == value
            assert len(parts) == number_of_parts
            assert parts.count(0) >= 2
