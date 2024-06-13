from flask import Blueprint, jsonify, request
from views.http_types.http_response import HttpResponse
from views.main_view import MainView
from errors.error_handler import handle_errors
from views.http_types.http_request import HttpRequest

tags_routes_bp = Blueprint('ia_routes', __name__)
main_view = MainView()

@tags_routes_bp.route("/<endpoint>", methods=['GET', 'POST'])
def handle_endpoint(endpoint):
    try:
        if request.method == 'GET':
            response_handler = main_view.endpoints['get_view']
            response = response_handler(endpoint)
        elif request.method == 'POST':
            if 'file' in request.files:
                file = request.files['file']
                csv_content = file.read().decode('iso-8859-1')
                http_request = HttpRequest(body={'csv_content': csv_content})
            else:
                http_request = HttpRequest(body=request.json)
            
            response_handler = main_view.endpoints['post_view']
            response = response_handler(endpoint, http_request)
        else:
            raise ValueError(f"Método HTTP '{request.method}' não suportado para o endpoint '{endpoint}'.")
    except Exception as exception:
        response = handle_errors(exception)

    if isinstance(response.body, HttpResponse):
        return response.body.body, response.status_code
    
    return response.body, response.status_code
