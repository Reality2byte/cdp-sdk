# coding: utf-8

"""
    Coinbase Developer Platform APIs

    The Coinbase Developer Platform APIs - leading the world's transition onchain.

    The version of the OpenAPI document: 2.0.0
    Contact: cdp@coinbase.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cdp.openapi_client.models.sign_sol_transaction_criteria_inner import SignSolTransactionCriteriaInner

class TestSignSolTransactionCriteriaInner(unittest.TestCase):
    """SignSolTransactionCriteriaInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignSolTransactionCriteriaInner:
        """Test SignSolTransactionCriteriaInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignSolTransactionCriteriaInner`
        """
        model = SignSolTransactionCriteriaInner()
        if include_optional:
            return SignSolTransactionCriteriaInner(
                type = 'solAddress',
                addresses = [HpabPRRCFbBKSuJr5PdkVvQc85FyxyTWkFM2obBRSvHT],
                operator = 'in',
                sol_value = '1000000000000000000',
                spl_value = '1000000000000000000'
            )
        else:
            return SignSolTransactionCriteriaInner(
                type = 'solAddress',
                addresses = [HpabPRRCFbBKSuJr5PdkVvQc85FyxyTWkFM2obBRSvHT],
                operator = 'in',
                sol_value = '1000000000000000000',
                spl_value = '1000000000000000000',
        )
        """

    def testSignSolTransactionCriteriaInner(self):
        """Test SignSolTransactionCriteriaInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
