class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # we can manage our request in this middleware
        response = self.get_response(request)

        print("Middleware: Processing Response")

        return response