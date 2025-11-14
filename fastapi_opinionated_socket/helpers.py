from fastapi_opinionated.app import App
from socketio import AsyncServer
from fastapi_opinionated.exceptions.plugin_exception import PluginException

def socket_api()->AsyncServer:
    """
    Return the application's AsyncServer socket instance.

    This is a convenience accessor that retrieves the socket server instance from the application's
    plugin registry (App.plugin.socket). Use this to access the AsyncServer for emitting events,
    registering handlers, or performing other server-level operations.

    Returns:
        AsyncServer: The AsyncServer instance provided by the application's plugin.

    Notes:
        - The returned object is typically a shared/global instance; modifying it may affect other
          parts of the application.
        - Ensure the application and its plugins have been initialized before calling this function,
          otherwise App.plugin.socket may be unset or raise an AttributeError.
    """
    if not hasattr(App.plugin, "socket"):
        raise PluginException("SocketPlugin", cause=AttributeError("Socket plugin not enabled or not initialized"))
    return App.plugin.socket