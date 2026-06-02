from typing import Any
from urllib.parse import urlsplit, urlunsplit

from src.infra.config.settings import settings


def _mask_url(value: str) -> str:
    parsed = urlsplit(value)
    if not parsed.username and not parsed.password:
        return value

    host = parsed.hostname or ""
    if parsed.port:
        host = f"{host}:{parsed.port}"
    return urlunsplit((parsed.scheme, f"***:***@{host}", parsed.path, parsed.query, parsed.fragment))


class InfraHealthHandler:
    async def check(self) -> dict[str, Any]:
        return {
            "service": settings.app_name,
            "ok": True,
            "mode": "docker-healthcheck",
            "message": "External service liveness is delegated to Docker healthchecks.",
            "clients": [
                {
                    "name": "rabbitmq",
                    "configured": True,
                    "url": _mask_url(settings.rabbitmq_url),
                    "exchange": settings.rabbitmq_exchange,
                    "user_events_exchange": settings.user_events_exchange,
                    "user_events_queue": settings.user_events_queue,
                },
                {
                    "name": "postgres",
                    "configured": True,
                    "url": _mask_url(settings.database_url),
                },
                {
                    "name": "redis",
                    "configured": True,
                    "url": _mask_url(settings.redis_url),
                },
                {
                    "name": "prometheus",
                    "configured": True,
                    "url": settings.prometheus_url,
                },
                {
                    "name": "datadog",
                    "configured": True,
                    "enabled": settings.datadog_enabled,
                    "service": settings.datadog_service,
                    "env": settings.datadog_env,
                    "agent_host": settings.datadog_agent_host,
                },
            ],
        }
