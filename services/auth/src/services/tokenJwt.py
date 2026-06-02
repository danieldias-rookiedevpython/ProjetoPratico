from datetime import datetime, timedelta, timezone
from typing import Optional

from authlib.jose import JoseError, jwt

from ..config import get_settings


class TokenService:
    @staticmethod
    def _encode(payload: dict) -> str:
        settings = get_settings()
        token = jwt.encode({"alg": settings.JWT_ALGORITHM}, payload, settings.JWT_SECRET)
        return token.decode("utf-8") if isinstance(token, bytes) else token

    @staticmethod
    def generate_token(user_id: str, role: str = "user") -> dict:
        settings = get_settings()
        now = datetime.now(timezone.utc)

        access_payload = {
            "sub": str(user_id),
            "role": role,
            "type": "access",
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)).timestamp()),
        }

        refresh_payload = {
            "sub": str(user_id),
            "role": role,
            "type": "refresh",
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)).timestamp()),
        }

        return {
            "access_token": TokenService._encode(access_payload),
            "refresh_token": TokenService._encode(refresh_payload),
            "token_type": "Bearer",
        }

    @staticmethod
    def validate_token(token: str, refresh_token: str = "") -> bool:
        payload = TokenService.decode_token(token)
        if not payload:
            return False
        return payload.get("type") == "access" or bool(refresh_token)

    @staticmethod
    def decode_token(token: str) -> Optional[dict]:
        try:
            settings = get_settings()
            claims = jwt.decode(token, settings.JWT_SECRET)
            claims.validate()
            return dict(claims)
        except JoseError:
            return None

    @staticmethod
    def encode_token(payload: dict) -> str:
        return TokenService._encode(payload)

    @staticmethod
    def refresh_token(token: str) -> Optional[str]:
        settings = get_settings()
        payload = TokenService.decode_token(token)

        if not payload or payload.get("type") != "refresh":
            return None

        now = datetime.now(timezone.utc)
        new_access_payload = {
            "sub": payload.get("sub"),
            "role": payload.get("role", "user"),
            "type": "access",
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)).timestamp()),
        }

        return TokenService._encode(new_access_payload)
