# FastAPI Opinionated Socket Extension

FastAPI Opinionated Socket is an optional extension for the FastAPI Opinionated Core framework that provides Socket.IO functionality for real-time bidirectional communication between clients and servers.

## Overview

This package extends the FastAPI Opinionated Core framework by adding Socket.IO capabilities through a plugin system. It allows you to easily integrate real-time features into your FastAPI applications using the python-socketio library.

## Features

- **Socket.IO Integration**: Provides WebSocket-like bidirectional communication between clients and servers
- **Plugin Architecture**: Integrates seamlessly with the FastAPI Opinionated Core plugin system
- **ASGI Mounting**: Automatically mounts the Socket.IO application onto your FastAPI application
- **Convenience Accessor**: Provides easy access to the AsyncServer instance for emitting events and registering handlers
- **Decorator-Based Event Registration**: Use `@SocketEvent` decorator to register Socket.IO event handlers
- **Namespace Support**: Supports Socket.IO namespaces for organizing events
- **Lifecycle Management**: Properly handles shutdown of the Socket.IO server

## Installation

```bash
# Install via Poetry (recommended)
poetry add fastapi-opinionated-socket

# Or via pip
pip install fastapi-opinionated-socket
```

## Usage

### Configuration

Enable the Socket plugin in your application:

```python
from fastapi_opinionated import App
from fastapi_opinionated_socket import SocketPlugin

app = App.create() # FastAPI Factory

App.enable(
    SocketPlugin(),
    async_mode="asgi",
    cors_allowed_origins=["*"],
    ping_interval=25,
    ping_timeout=5,
    socketio_path="socket.io"
)
```

### Registering Socket Event Handlers

Use the `@SocketEvent` decorator to register Socket.IO event handlers:

```python
from fastapi_opinionated_socket import SocketEvent

@SocketEvent("connect")
async def handle_connect(sid, environ):
    print(f"Client {sid} connected")

@SocketEvent("disconnect")
async def handle_disconnect(sid):
    print(f"Client {sid} disconnected")

@SocketEvent("message")
async def handle_message(sid, data):
    print(f"Received message from {sid}: {data}")
    # Broadcast to all clients
    await socket_api().emit("response", f"Echo: {data}")

@SocketEvent("message", namespace="/chat")
async def handle_chat_message(sid, data):
    print(f"Received chat message from {sid}: {data}")
    # Broadcast to all clients in the /chat namespace
    await socket_api().emit("response", f"Chat Echo: {data}", namespace="/chat")
```

### Using the Socket API

Access the Socket.IO server instance for sending events:

```python
from fastapi_opinionated_socket import socket_api

# Emit an event to all connected clients
await socket_api().emit("notification", {"message": "Hello, everyone!"})

# Emit an event to a specific room
await socket_api().emit("notification", {"message": "Hello, room!"}, room="room_id")

# Emit an event to a specific client
await socket_api().emit("private", {"message": "Hello, client!"}, to="client_sid")
```

### Complete Example

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_opinionated import App
from fastapi_opinionated_socket import SocketPlugin, SocketEvent, socket_api

# Register socket event handlers
@SocketEvent("connect")
async def handle_connect(sid, environ):
    print(f"Client {sid} connected")

@SocketEvent("disconnect")
async def handle_disconnect(sid):
    print(f"Client {sid} disconnected")

@SocketEvent("message")
async def handle_message(sid, data):
    print(f"Received message from {sid}: {data}")
    # Echo the message back to all clients
    await socket_api().emit("response", {"message": data, "from": sid})

# Create your application
app = App.create(title="My API with Socket.IO")

# Enable the Socket plugin
App.enable(
    SocketPlugin(),
    cors_allowed_origins=["*"],
    async_mode="asgi"
)

# Regular FastAPI endpoints
@app.get("/")
async def root():
    return {"message": "FastAPI with Socket.IO"}
```

## Architecture

The package consists of:

- **SocketPlugin**: A plugin class that extends BasePlugin and handles the initialization and mounting of Socket.IO
- **socket_api()**: A helper function that provides access to the AsyncServer instance from the application's plugin registry
- **SocketEvent**: A decorator for registering Socket.IO event handlers with lazy loading
- **Event Registry**: Internal registry mechanism that stores and processes Socket.IO event handlers
- **Integration**: Seamlessly integrates with the FastAPI Opinionated Core plugin system and lifecycle management

## Plugin Lifecycle

The Socket plugin properly handles lifecycle management:

- On startup: Initializes the Socket.IO server and registers event handlers
- On shutdown: Properly shuts down the Socket.IO server

## Configuration Options

The SocketPlugin accepts all python-socketio AsyncServer options:

- `async_mode`: Asynchronous mode ("asgi", "sanic", "tornado", etc.)
- `cors_allowed_origins`: List of allowed origins for CORS
- `ping_interval`: Interval between ping packets (seconds)
- `ping_timeout`: Timeout for ping responses (seconds)
- `socketio_path`: Path where Socket.IO will be mounted (default: "socket.io")

## Note

FastAPI Opinionated Socket is an **optional extension** of the FastAPI Opinionated Core framework. It provides additional functionality for applications that require real-time communication features, but is not required for basic FastAPI Opinionated Core functionality.