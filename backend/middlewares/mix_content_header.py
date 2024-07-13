# In a new file, e.g., middleware.py
class MixContentHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Content-Security-Policy"] = "upgrade-insecure-requests"
        return response
