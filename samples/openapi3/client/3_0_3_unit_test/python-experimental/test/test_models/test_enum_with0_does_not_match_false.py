# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.model.enum_with0_does_not_match_false import EnumWith0DoesNotMatchFalse
from unit_test_api import configuration


class TestEnumWith0DoesNotMatchFalse(unittest.TestCase):
    """EnumWith0DoesNotMatchFalse unit test stubs"""
    _configuration = configuration.Configuration()

    def test_integer_zero_is_valid_passes(self):
        # integer zero is valid
        EnumWith0DoesNotMatchFalse._from_openapi_data(
            0,
            _configuration=self._configuration
        )

    def test_float_zero_is_valid_passes(self):
        # float zero is valid
        EnumWith0DoesNotMatchFalse._from_openapi_data(
            0.0,
            _configuration=self._configuration
        )

    def test_false_is_invalid_fails(self):
        # false is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            EnumWith0DoesNotMatchFalse._from_openapi_data(
                False,
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()
