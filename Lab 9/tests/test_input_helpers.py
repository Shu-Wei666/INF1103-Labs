import io
import unittest

from contextlib import redirect_stdout
from unittest.mock import patch

from input_helpers import get_positive_float


class TestInputHelpers(unittest.TestCase):
    def test_retries_until_positive_number(self) -> None:
        output = io.StringIO()

        with patch(
            "builtins.input",
            side_effect=["abc", "-5", "12.50"]
        ) as mocked_input:
            with redirect_stdout(output):
                result = get_positive_float("Price: ")

        self.assertAlmostEqual(result, 12.50)
        self.assertEqual(mocked_input.call_count, 3)

        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "Please enter a valid number, e.g. 12.50",
                "Please enter a number greater than zero."
            ]
        )

    def test_zero_is_rejected(self) -> None:
        output = io.StringIO()

        with patch(
            "builtins.input",
            side_effect=["0", "5"]
        ) as mocked_input:
            with redirect_stdout(output):
                result = get_positive_float("Price: ")

        self.assertAlmostEqual(result, 5.0)
        self.assertEqual(mocked_input.call_count, 2)
        self.assertIn(
            "Please enter a number greater than zero.",
            output.getvalue()
        )

    def test_valid_input_returns_immediately(self) -> None:
        with patch(
            "builtins.input",
            return_value="25.50"
        ) as mocked_input:
            result = get_positive_float("Price: ")

        self.assertAlmostEqual(result, 25.50)
        mocked_input.assert_called_once_with("Price: ")


if __name__ == "__main__":
    unittest.main()