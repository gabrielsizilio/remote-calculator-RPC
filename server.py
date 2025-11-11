import logging
import xmlrpc.server

logging.basicConfig(level=logging.INFO)

class Calculator: 
    def add(self, x, y):
        print(f"Calculating: x={x} add y={y}")
        return x + y
    
    def sub(self, x, y):
        print(f"Calculating: x={x} sub y={y}")
        return x - y
    
    def mul(self, x, y):
        print(f"Calculating: x={x} mul y={y}")
        return x * y
    
    def div(self, x, y):
        print(f"Calculating: x={x} div y={y}")
        if y == 0:
            raise ValueError("Division by 0 is invalid operation!")
        return x / y
    

PORT = 8000
SERVER_ADDRESS = ("localhost", PORT)

try:
    server = xmlrpc.server.SimpleXMLRPCServer(SERVER_ADDRESS, logRequests=True, allow_none=True)
    server.register_instance(Calculator());

    logging.info(f"Server started in http://{SERVER_ADDRESS[0]}:{PORT}/")

    server.serve_forever()

except KeyboardInterrupt:
    logging.info("Server turn off by user.")
except Exception as e:
    logging.error(f"Error: {e}")