# infra/websocket/router.py

from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from src.Infra.Messaging.webSockets.container  import connection_manager


router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await connection_manager.connect(websocket)

    try:

        while True:

            await websocket.receive_text()

    except WebSocketDisconnect:

        connection_manager.disconnect(websocket)