class EventManager(object):
    def __init__(self):
        #key = event(string) / value = list clients (callable)
        self._registrations = {}


    def register(self, event_type, callback):
        """
        For adding a callback to an event_type
        callback will be called if an event of type event_type is received
        If event type does not exist, raise KeyError
        """
        self._registrations[event_type].append(callback)

    def send_event(self, event_type, event=None):
        """
        All events will be send to clients
        """
        list_clients = self._registrations[event_type]
        for client in list_clients:
            if event is None:
                client()
            else:
                client(event)


    def create_event_type(self, event_type):
        if not event_type in self._registrations:
            self._registrations[event_type] = []


_event_manager = EventManager()

create_event_type = _event_manager.create_event_type
send_event = _event_manager.send_event
register = _event_manager.register
