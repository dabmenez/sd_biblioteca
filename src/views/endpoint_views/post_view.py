from views.http_types.http_response import HttpResponse
from views.http_types.http_request import HttpRequest





class PostView:
    def __init__(self) -> None:
        self.endpoint_controllers = {

        }

    def call_controller(self, endpoint, http_request: HttpRequest) -> HttpResponse:
        if endpoint in self.endpoint_controllers:
            controller_handler = self.endpoint_controllers[endpoint]
            formatted_response = controller_handler(http_request.body['csv_content'])
            if isinstance(formatted_response, HttpResponse):
                return formatted_response
            else:
                return HttpResponse(status_code=200, body=formatted_response)
        else:
            return HttpResponse(status_code=404, body={"error": "Endpoint not found"})
