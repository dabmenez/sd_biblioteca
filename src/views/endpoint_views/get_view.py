from views.http_types.http_response import HttpResponse


class GetView:
    def __init__(self) -> None:
        pass
    def call_controller(self, endpoint) -> HttpResponse:
        controller_handler = self.endpoint_controllers[endpoint]
        formatted_response = controller_handler()
        return HttpResponse(status_code=200, body=formatted_response)