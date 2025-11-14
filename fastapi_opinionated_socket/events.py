# Registry for socket event handlers
_socket_event_registry = []


def register_socket_event(event_name: str, handler, namespace: str | None):
    """
    event_name: str
    handler: callable
    namespace: optional namespace for this event
    """
    _socket_event_registry.append({
        "event": event_name,
        "handler": handler,
        "namespace": namespace,
    })


def consume_socket_events():
    events = list(_socket_event_registry)
    _socket_event_registry.clear()
    return events
