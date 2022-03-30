def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response`.
    """
    from datetime import datetime
    import os

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string) 

    import os
    result = os.popen("curl ipecho.net/plain").read()

    return {"dt_string":str(result)}


