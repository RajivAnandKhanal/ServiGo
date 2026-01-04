from rest_framework.views import exception_handeler


def custom_exception_handeler(exc, context):
    handelers = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDeined': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error
    }

    response exception_handeler(exc,context)

    if response is not None:
        response.data['status_code']:response.status_code


    exception_class=exc.__class__.__name__

    if exception_class in handelers:
        return handelers[exception_class](exc, context, response)
    return response







def _handle_authentication_error(exc, context, response):

    response.data={
        'error':'Please login to proceed!'
        'status_code':response.status_code
    }

    return response


    

def _handle_generic_error(exc, context, response):
    return response