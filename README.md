# FastAPI Opinionated Socket Extension

FastAPI Opinionated Socket is an optional extension for the FastAPI Opinionated Core framework that provides Socket.IO functionality for real-time bidirectional communication between clients and servers.

## Overview

This package extends the FastAPI Opinionated Core framework by adding Socket.IO capabilities through a plugin system. It allows you to easily integrate real-time features into your FastAPI applications using the socketio library.

## Features

- **Socket.IO Integration**: Provides WebSocket-like bidirectional communication between clients and servers
- **Plugin Architecture**: Integrates seamlessly with the FastAPI Opinionated Core plugin system
- **ASGI Mounting**: Automatically mounts the Socket.IO application onto your FastAPI application
- **Convenience Accessor**: Provides easy access to the AsyncServer instance for emitting events and registering handlers

## Installation

```bash
# Install via Poetry (recommended)
poetry add fastapi-opinionated-socket

# Or via pip
pip install fastapi-opinionated-socket
```

## Usage
### Configuration

You can pass additional arguments to the Socket.IO server during initialization:

```python
from fastapi_opinionated import App
from fastapi_opinionated_socket.plugin import SocketPlugin

# Enable socket with custom configuration
app = App.create() # Fastapi Factory

App.enable(
    SocketPlugin(),
    async_mode="asgi",
    cors_allowed_origins=[],
    ping_interval=3,
    ping_timeout=60,
    socketio_path="socket",
)
```

## Architecture

The package consists of:

- **SocketPlugin**: A plugin class that extends BasePlugin and handles the initialization and mounting of Socket.IO
- **socket_api()**: A helper function that provides access to the AsyncServer instance from the application's plugin registry
- **Integration**: Seamlessly integrates with the FastAPI Opinionated Core plugin system

## Note

FastAPI Opinionated Socket is an **optional extension** of the FastAPI Opinionated Core framework. It provides additional functionality for applications that require real-time communication features, but is not required for basic FastAPI Opinionated Core functionality.