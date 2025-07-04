# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:00:14+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field, RootModel


class AccessDeniedException(RootModel[Any]):
    root: Any


class AccessToken(RootModel[str]):
    root: str


class AuthCode(RootModel[str]):
    root: str


class AuthorizationPendingException(RootModel[Any]):
    root: Any


class ClientId(RootModel[str]):
    root: str


class ClientName(RootModel[str]):
    root: str


class ClientSecret(RootModel[str]):
    root: str


class ClientType(RootModel[str]):
    root: str


class DeviceCode(RootModel[str]):
    root: str


class ExpirationInSeconds(RootModel[int]):
    root: int


class ExpiredTokenException(RootModel[Any]):
    root: Any


class GrantType(RootModel[str]):
    root: str


class IdToken(RootModel[str]):
    root: str


class InternalServerException(RootModel[Any]):
    root: Any


class IntervalInSeconds(RootModel[int]):
    root: int


class InvalidClientException(RootModel[Any]):
    root: Any


class InvalidClientMetadataException(RootModel[Any]):
    root: Any


class InvalidGrantException(RootModel[Any]):
    root: Any


class InvalidRequestException(RootModel[Any]):
    root: Any


class InvalidScopeException(RootModel[Any]):
    root: Any


class LongTimeStampType(RootModel[int]):
    root: int


class RefreshToken(RootModel[str]):
    root: str


class Scope(RootModel[str]):
    root: str


class Scopes(RootModel[List[Scope]]):
    root: List[Scope]


class SlowDownException(RootModel[Any]):
    root: Any


class TokenType(RootModel[str]):
    root: str


class URI(RootModel[str]):
    root: str


class UnauthorizedClientException(RootModel[Any]):
    root: Any


class UnsupportedGrantTypeException(RootModel[Any]):
    root: Any


class UserCode(RootModel[str]):
    root: str


class ClientRegisterPostRequest(BaseModel):
    clientName: str = Field(..., description='The friendly name of the client.')
    clientType: str = Field(
        ...,
        description='The type of client. The service supports only <code>public</code> as a client type. Anything other than public will be rejected by the service.',
    )
    scopes: Optional[List[Scope]] = Field(
        None,
        description='The list of scopes that are defined by the client. Upon authorization, this list is used to restrict permissions when granting an access token.',
    )


class DeviceAuthorizationPostRequest(BaseModel):
    clientId: str = Field(
        ...,
        description='The unique identifier string for the client that is registered with IAM Identity Center. This value should come from the persisted result of the <a>RegisterClient</a> API operation.',
    )
    clientSecret: str = Field(
        ...,
        description='A secret string that is generated for the client. This value should come from the persisted result of the <a>RegisterClient</a> API operation.',
    )
    startUrl: str = Field(
        ...,
        description='The URL for the AWS access portal. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html">Using the AWS access portal</a> in the <i>IAM Identity Center User Guide</i>.',
    )


class TokenPostRequest(BaseModel):
    clientId: str = Field(
        ...,
        description='The unique identifier string for each client. This value should come from the persisted result of the <a>RegisterClient</a> API.',
    )
    clientSecret: str = Field(
        ...,
        description='A secret string generated for the client. This value should come from the persisted result of the <a>RegisterClient</a> API.',
    )
    code: Optional[str] = Field(
        None,
        description='The authorization code received from the authorization service. This parameter is required to perform an authorization grant request to get access to a token.',
    )
    deviceCode: Optional[str] = Field(
        None,
        description='Used only when calling this API for the device code grant type. This short-term code is used to identify this authentication attempt. This should come from an in-memory reference to the result of the <a>StartDeviceAuthorization</a> API.',
    )
    grantType: str = Field(
        ...,
        description='<p>Supports grant types for the authorization code, refresh token, and device code request. For device code requests, specify the following value:</p> <p> <code>urn:ietf:params:oauth:grant-type:<i>device_code</i> </code> </p> <p>For information about how to obtain the device code, see the <a>StartDeviceAuthorization</a> topic.</p>',
    )
    redirectUri: Optional[str] = Field(
        None,
        description='The location of the application that will receive the authorization code. Users authorize the service to send the request to this location.',
    )
    refreshToken: Optional[str] = Field(
        None,
        description='<p>Currently, <code>refreshToken</code> is not yet implemented and is not supported. For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see <i>Considerations for Using this Guide</i> in the <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html">IAM Identity Center OIDC API Reference</a>.</p> <p>The token used to obtain an access token in the event that the access token is invalid or expired.</p>',
    )
    scope: Optional[List[Scope]] = Field(
        None,
        description='The list of scopes that is defined by the client. Upon authorization, this list is used to restrict permissions when granting an access token.',
    )


class CreateTokenRequest(BaseModel):
    clientId: ClientId
    clientSecret: ClientSecret
    code: Optional[AuthCode] = None
    deviceCode: Optional[DeviceCode] = None
    grantType: GrantType
    redirectUri: Optional[URI] = None
    refreshToken: Optional[RefreshToken] = None
    scope: Optional[Scopes] = None


class CreateTokenResponse(BaseModel):
    accessToken: Optional[AccessToken] = None
    expiresIn: Optional[ExpirationInSeconds] = None
    idToken: Optional[IdToken] = None
    refreshToken: Optional[RefreshToken] = None
    tokenType: Optional[TokenType] = None


class RegisterClientRequest(BaseModel):
    clientName: ClientName
    clientType: ClientType
    scopes: Optional[Scopes] = None


class RegisterClientResponse(BaseModel):
    authorizationEndpoint: Optional[URI] = None
    clientId: Optional[ClientId] = None
    clientIdIssuedAt: Optional[LongTimeStampType] = None
    clientSecret: Optional[ClientSecret] = None
    clientSecretExpiresAt: Optional[LongTimeStampType] = None
    tokenEndpoint: Optional[URI] = None


class StartDeviceAuthorizationRequest(BaseModel):
    clientId: ClientId
    clientSecret: ClientSecret
    startUrl: URI


class StartDeviceAuthorizationResponse(BaseModel):
    deviceCode: Optional[DeviceCode] = None
    expiresIn: Optional[ExpirationInSeconds] = None
    interval: Optional[IntervalInSeconds] = None
    userCode: Optional[UserCode] = None
    verificationUri: Optional[URI] = None
    verificationUriComplete: Optional[URI] = None
