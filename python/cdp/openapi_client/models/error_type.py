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
import json
from enum import Enum
from typing_extensions import Self


class ErrorType(str, Enum):
    """
    The code that indicates the type of error that occurred. These error codes can be used to determine how to handle the error.
    """

    """
    allowed enum values
    """
    ALREADY_EXISTS = 'already_exists'
    BAD_GATEWAY = 'bad_gateway'
    FAUCET_LIMIT_EXCEEDED = 'faucet_limit_exceeded'
    FORBIDDEN = 'forbidden'
    IDEMPOTENCY_ERROR = 'idempotency_error'
    INTERNAL_SERVER_ERROR = 'internal_server_error'
    INVALID_REQUEST = 'invalid_request'
    INVALID_SIGNATURE = 'invalid_signature'
    MALFORMED_TRANSACTION = 'malformed_transaction'
    NOT_FOUND = 'not_found'
    PAYMENT_METHOD_REQUIRED = 'payment_method_required'
    RATE_LIMIT_EXCEEDED = 'rate_limit_exceeded'
    REQUEST_CANCELED = 'request_canceled'
    SERVICE_UNAVAILABLE = 'service_unavailable'
    TIMED_OUT = 'timed_out'
    UNAUTHORIZED = 'unauthorized'
    POLICY_VIOLATION = 'policy_violation'
    POLICY_IN_USE = 'policy_in_use'
    ACCOUNT_LIMIT_EXCEEDED = 'account_limit_exceeded'
    NETWORK_NOT_TRADABLE = 'network_not_tradable'
    GUEST_PERMISSION_DENIED = 'guest_permission_denied'
    GUEST_REGION_FORBIDDEN = 'guest_region_forbidden'
    GUEST_TRANSACTION_LIMIT = 'guest_transaction_limit'
    GUEST_TRANSACTION_COUNT = 'guest_transaction_count'
    PHONE_NUMBER_VERIFICATION_EXPIRED = 'phone_number_verification_expired'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ErrorType from a JSON string"""
        return cls(json.loads(json_str))


