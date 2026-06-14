from dataclasses import dataclass


@dataclass
class WebSocketConfig:

    heartbeat_interval: int = 30

    max_connections: int = 10000

    redis_channel_prefix: str = "ws"

    enable_redis_pubsub: bool = True

    enable_kafka_consumers: bool = False


websocket_config = WebSocketConfig()