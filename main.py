import http.server
import socketserver
import json
import random
import time

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    request_counter = 0

    def do_GET(self):
        self.request_counter += 1
        
        # The core concept of the article: Always send HTTP 200 OK,
        # regardless of the application's internal outcome.
        self.send_response(200) 
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_data = {}
        if self.path == "/api/data":
            # Simulate different application-level outcomes
            # even when the HTTP status is technically "OK" (200).
            if self.request_counter % 3 == 0:
                # Scenario 1: Application-level error, but HTTP status is 200 OK.
                response_data = {
                    "app_status": "error",
                    "code": "INTERNAL_PROCESSING_FAILURE",
                    "message": "An internal application error occurred during data processing.",
                    "data": None,
                    "timestamp": int(time.time())
                }
            elif self.request_counter % 3 == 1:
                # Scenario 2: Application-level success, data returned.
                response_data = {
                    "app_status": "success",
                    "code": "DATA_RETRIEVED",
                    "message": "Data successfully retrieved and processed.",
                    "data": {
                        "id": random.randint(1000, 9999),
                        "name": f"Product {self.request_counter}",
                        "price": round(random.uniform(10.0, 500.0), 2)
                    },
                    "timestamp": int(time.time())
                }
            else: # self.request_counter % 3 == 2
                # Scenario 3: Application-level "not found" or "no content", but HTTP status is 200 OK.
                response_data = {
                    "app_status": "warning",
                    "code": "NO_MATCHING_DATA",
                    "message": "No data found for your request, but the server processed it successfully.",
                    "data": [],
                    "timestamp": int(time.time())
                }
        else:
            # For any other path, still return 200 OK, but with a "not found" message.
            response_data = {
                "app_status": "error",
                "code": "ENDPOINT_NOT_FOUND",
                "message": f"The requested endpoint '{self.path}' was not found.",
                "data": None,
                "timestamp": int(time.time())
            }

        self.wfile.write(json.dumps(response_data, indent=2).encode("utf-8"))

# Start the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on http://localhost:{PORT}")
    print("\nAccess http://localhost:8000/api/data multiple times.")
    print("Observe that the HTTP status code is ALWAYS 200 OK,")
    print("but the 'app_status' field in the JSON response changes,")
    print("demonstrating the article's point about 'real' success.")
    print("Press Ctrl+C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
