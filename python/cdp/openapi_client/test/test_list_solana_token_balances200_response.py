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

from cdp.openapi_client.models.list_solana_token_balances200_response import ListSolanaTokenBalances200Response

class TestListSolanaTokenBalances200Response(unittest.TestCase):
    """ListSolanaTokenBalances200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListSolanaTokenBalances200Response:
        """Test ListSolanaTokenBalances200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListSolanaTokenBalances200Response`
        """
        model = ListSolanaTokenBalances200Response()
        if include_optional:
            return ListSolanaTokenBalances200Response(
                next_page_token = 'eyJsYXN0X2lkIjogImFiYzEyMyIsICJ0aW1lc3RhbXAiOiAxNzA3ODIzNzAxfQ==',
                balances = [{"amount":{"amount":"1250000000","decimals":9},"token":{"symbol":"SOL","name":"Solana","mintAddress":"So11111111111111111111111111111111111111111"}},{"amount":{"amount":"123456000","decimals":6},"token":{"symbol":"USDC","name":"USD Coin","mintAddress":"4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU"}}]
            )
        else:
            return ListSolanaTokenBalances200Response(
                balances = [{"amount":{"amount":"1250000000","decimals":9},"token":{"symbol":"SOL","name":"Solana","mintAddress":"So11111111111111111111111111111111111111111"}},{"amount":{"amount":"123456000","decimals":6},"token":{"symbol":"USDC","name":"USD Coin","mintAddress":"4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU"}}],
        )
        """

    def testListSolanaTokenBalances200Response(self):
        """Test ListSolanaTokenBalances200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
