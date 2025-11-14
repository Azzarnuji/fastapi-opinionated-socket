# Registry for socket event handlers
_socket_event_registry = []


def register_socket_event(event_name: str, handler, namespace: str | None):
    """
    Register a socket event handler in the module-level event registry.

    Adds a mapping describing an event to the internal `_socket_event_registry` so the
    framework can dispatch incoming socket events to the provided handler.

    Args:
        event_name (str): Name of the socket event to register (for example "connect" or "message").
        handler (callable): Callable to be invoked when the event is emitted. The expected
            signature depends on the surrounding socket framework; it should accept the
            event payload and any context arguments the framework supplies.
        namespace (str | None): Optional namespace under which the event is registered.
            If None, the event applies to the default/global namespace.

    Returns:
        None

    Notes:
        - This function mutates the module-level `_socket_event_registry` by appending a
          dictionary with keys "event", "handler", and "namespace".
        - No argument validation is performed; callers should ensure `event_name` is a
          string and `handler` is callable.
        - Duplicate registrations for the same event/namespace are not prevented by this function.
    """
    _socket_event_registry.append({
        "event": event_name,
        "handler": handler,
        "namespace": namespace,
    })


def consume_socket_events():
    """
    Consume and return all queued socket events.

    Retrieve all entries currently stored in the module-level `_socket_event_registry`,
    clear the registry, and return those entries as a list. The returned list is a
    shallow copy of the registry contents at the time of invocation; subsequent
    modifications to the returned list will not affect the registry.

    Returns:
        list: A list containing the socket event objects/records that were registered.
              If the registry is empty, an empty list is returned.

    Side effects:
        - Clears the module-level `_socket_event_registry`.

    Notes:
        - This function does not guarantee atomicity or thread safety; if multiple
          threads or coroutines may access `_socket_event_registry` concurrently,
          access should be synchronized externally.
    """
    events = list(_socket_event_registry)
    _socket_event_registry.clear()
    return events
