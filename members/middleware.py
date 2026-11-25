import time


class SimpleLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Request: {request.method} {request.path}")   # before the view
        response = self.get_response(request)
        print(f"Response status: {response.status_code}")    # after the view
        return response


class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()  # before the view
        response = self.get_response(request)
        duration_ms = (time.perf_counter() - start) * 1000  # after the view
        response["X-Response-Time-ms"] = f"{duration_ms:.1f}"
        print(f"{request.method} {request.path} took {duration_ms:.1f} ms")
        return response


class PageViewCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before the view
        request.session["page_views"] = request.session.get("page_views", 0) + 1
        response = self.get_response(request)
        return response
