# coding: utf-8

"""
    Coinbase Developer Platform APIs

    The Coinbase Developer Platform APIs - leading the world's transition onchain.

    The version of the OpenAPI document: 2.0.0
    Contact: cdp@coinbase.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cdp.openapi_client.models.common_swap_response_fees import CommonSwapResponseFees
from cdp.openapi_client.models.common_swap_response_issues import CommonSwapResponseIssues
from cdp.openapi_client.models.create_swap_quote_response_all_of_permit2 import CreateSwapQuoteResponseAllOfPermit2
from cdp.openapi_client.models.create_swap_quote_response_all_of_transaction import CreateSwapQuoteResponseAllOfTransaction
from typing import Optional, Set
from typing_extensions import Self

class CreateSwapQuoteResponse(BaseModel):
    """
    CreateSwapQuoteResponse
    """ # noqa: E501
    block_number: Annotated[str, Field(strict=True)] = Field(description="The block number at which the liquidity conditions were examined.", alias="blockNumber")
    to_amount: Annotated[str, Field(strict=True)] = Field(description="The amount of the `toToken` that will be received in atomic units of the `toToken`. For example, `1000000000000000000` when receiving ETH equates to 1 ETH, `1000000` when receiving USDC equates to 1 USDC, etc.", alias="toAmount")
    to_token: Annotated[str, Field(strict=True)] = Field(description="The 0x-prefixed contract address of the token that will be received.", alias="toToken")
    fees: CommonSwapResponseFees
    issues: CommonSwapResponseIssues
    liquidity_available: StrictBool = Field(description="Whether sufficient liquidity is available to settle the swap. All other fields in the response will be empty if this is false.", alias="liquidityAvailable")
    min_to_amount: Annotated[str, Field(strict=True)] = Field(description="The minimum amount of the `toToken` that must be received for the swap to succeed, in atomic units of the `toToken`.  For example, `1000000000000000000` when receiving ETH equates to 1 ETH, `1000000` when receiving USDC equates to 1 USDC, etc. This value is influenced by the `slippageBps` parameter.", alias="minToAmount")
    from_amount: Annotated[str, Field(strict=True)] = Field(description="The amount of the `fromToken` that will be sent in this swap, in atomic units of the `fromToken`. For example, `1000000000000000000` when sending ETH equates to 1 ETH, `1000000` when sending USDC equates to 1 USDC, etc.", alias="fromAmount")
    from_token: Annotated[str, Field(strict=True)] = Field(description="The 0x-prefixed contract address of the token that will be sent.", alias="fromToken")
    permit2: Optional[CreateSwapQuoteResponseAllOfPermit2]
    transaction: CreateSwapQuoteResponseAllOfTransaction
    __properties: ClassVar[List[str]] = ["blockNumber", "toAmount", "toToken", "fees", "issues", "liquidityAvailable", "minToAmount", "fromAmount", "fromToken", "permit2", "transaction"]

    @field_validator('block_number')
    def block_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[1-9]\d*$", value):
            raise ValueError(r"must validate the regular expression /^[1-9]\d*$/")
        return value

    @field_validator('to_amount')
    def to_amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9]\d*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9]\d*)$/")
        return value

    @field_validator('to_token')
    def to_token_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^0x[a-fA-F0-9]{40}$", value):
            raise ValueError(r"must validate the regular expression /^0x[a-fA-F0-9]{40}$/")
        return value

    @field_validator('min_to_amount')
    def min_to_amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9]\d*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9]\d*)$/")
        return value

    @field_validator('from_amount')
    def from_amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(0|[1-9]\d*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9]\d*)$/")
        return value

    @field_validator('from_token')
    def from_token_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^0x[a-fA-F0-9]{40}$", value):
            raise ValueError(r"must validate the regular expression /^0x[a-fA-F0-9]{40}$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateSwapQuoteResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of fees
        if self.fees:
            _dict['fees'] = self.fees.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issues
        if self.issues:
            _dict['issues'] = self.issues.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permit2
        if self.permit2:
            _dict['permit2'] = self.permit2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # set to None if permit2 (nullable) is None
        # and model_fields_set contains the field
        if self.permit2 is None and "permit2" in self.model_fields_set:
            _dict['permit2'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSwapQuoteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "blockNumber": obj.get("blockNumber"),
            "toAmount": obj.get("toAmount"),
            "toToken": obj.get("toToken"),
            "fees": CommonSwapResponseFees.from_dict(obj["fees"]) if obj.get("fees") is not None else None,
            "issues": CommonSwapResponseIssues.from_dict(obj["issues"]) if obj.get("issues") is not None else None,
            "liquidityAvailable": obj.get("liquidityAvailable"),
            "minToAmount": obj.get("minToAmount"),
            "fromAmount": obj.get("fromAmount"),
            "fromToken": obj.get("fromToken"),
            "permit2": CreateSwapQuoteResponseAllOfPermit2.from_dict(obj["permit2"]) if obj.get("permit2") is not None else None,
            "transaction": CreateSwapQuoteResponseAllOfTransaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None
        })
        return _obj


