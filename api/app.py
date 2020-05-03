from chalice import Chalice, Response
from chalicelib.controllers import (
    my_first_controller
)

app = Chalice(app_name='app')
app.debug = True # ! remove in prod

@app.route('/', cors=True, methods=['GET','POST', 'PUT', 'DELETE'])
def route_my_first_controller():
    req = app.current_request.json_body
    return my_first_controller.main()

@app.route('/books', methods=['GET', 'POST'])
def books_route():
    request = app.current_request

    if request.method == 'GET':
        return [
            dict(book_id=1),
            dict(book_id=2)
        ]
    elif request.method == 'POST':
        return Response(body=None,
                        headers=dict(Location='/books/3'),
                        status_code=201)


@app.route('/books/{book_id}', methods=['GET', 'PUT', 'DELETE'])
def books_route(book_id):
    request = app.current_request

    if request.method == 'GET':
        return get_book(book_id)
    elif request.method == 'PUT':
        return Response(body=None,
                        status_code=204)
    elif request.method == 'DELETE':
        return Response(body=None,
                        status_code=204)


def get_book(book_id):
    return dict(book_id=int(book_id))