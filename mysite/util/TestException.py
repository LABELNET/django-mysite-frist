from rest_framework.views import exception_handler


def custom_exception_handler(exc, request):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, request)

    # Now add the HTTP status code to the response and rename detail to error
    if response is not None:
        response.data['code'] = response.status_code
        response.data['data'] = []
        response.data['msg'] = response.data.get('detail')
        del response.data['detail']

    return response
