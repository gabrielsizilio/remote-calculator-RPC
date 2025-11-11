import xmlrpc.client
import logging
import sys

logging.basicConfig(level=logging.INFO)

SERVER_URL = "http://localhost:8000"

def get_user_input():
    operation = input("Type the operation 'add', 'sub', 'mul', 'div' or 'exit'\n")

    if operation == 'exit':
        return None, None, None
    
    if operation not in ['add', 'sub', 'mul', 'div']:
        logging.warning("Invalid operation. Try again.")
        return get_user_input()
    
    try:
        num_str_x = input("x: ").strip()
        num_str_y = input("y: ").strip()

        num_x = float(num_str_x)
        num_y = float(num_str_y)

        return operation, num_x, num_y
    except ValueError:
        logging.error("Invalid Input. Try again.")
        return get_user_input()
    

def run_client():
    try:
        proxy = xmlrpc.client.ServerProxy(SERVER_URL)
        print("Conected to the Calculator RPC Server")

        while True:
            operation, num_x, num_y = get_user_input()

            if operation is None and num_x is None and num_y is None:
                print("Cosing client connection")
                break

            try:
                method = getattr(proxy, operation)
                logging.info(f"Sending: {operation}({num_x}, {num_y})")

                result = method(num_x, num_y);
                print(f"Result: {result}")

            except xmlrpc.client.Fault as e:
                print(f"{e.faultString}")
            except AttributeError:
                logging.error(f"Operation {operation} is not exist.")
            except Exception as e:
                logging.error(f"Error {e}")
                
    except ConnectionRefusedError:
        logging.critical(f"We were unable to connect to the server at {SERVER_URL}. Please check if 'server.py' is running.")
    except Exception as e:
        logging.critical(f"Fatal error: {e}")
    finally:
        sys.exit(0)

if __name__ == "__main__":
    run_client()