import time
import socket
from datetime import datetime
from struct import *

class CThought:
    ERROR_DATA_INCOMPLETE           = 'incomplete data'
        
    THOUGHT_HEADER_FORMAT           = '<QQI'
    HEADER_SIZE                     = calcsize(THOUGHT_HEADER_FORMAT)
    DATETIME_FORMAT                 = '%Y-%m-%d %H:%M:%S' 
        
    @staticmethod
    def parse_thought_header(thought_header):
        # If data isn't enough to contain header
        if (CThought.HEADER_SIZE > len(thought_header)):
            raise RuntimeError(CThought.ERROR_DATA_INCOMPLETE)
        
        # Parsing the data header
        user_id_number, timestamp, thought_size = \
            unpack(CThought.THOUGHT_HEADER_FORMAT, thought_header[:CThought.HEADER_SIZE])
                
        # Formatting datetime
        datetime_formatted              = datetime.fromtimestamp(timestamp).strftime(CThought.DATETIME_FORMAT)
        
        # Return parsed thought
        return (datetime_formatted, user_id_number, thought_size)
    
    @staticmethod
    def parse_thought_data(thought_data):
        # Parsing thought data
        THOUGHT_DATA_FORMAT             = '<{0}s'.format(len(thought_data))
        parsed_thought_data             = unpack(THOUGHT_DATA_FORMAT, thought_data)[0].decode("utf-8")
        
        return parsed_thought_data
        
def recive_data(connection, is_close_after, amount):
    from_client = b''
    remaining_to_recive = amount    
    while 0 < remaining_to_recive:
         data = connection.recv(remaining_to_recive)
         if not data: break             
         from_client += data
         remaining_to_recive -= len(data)
    if is_close_after:         
        connection.close()          
    return from_client   
   
def recive_thought_header(connection):
    return recive_data(connection, False, CThought.HEADER_SIZE)
    
def recive_thought_data(connection, thought_size):
    return recive_data(connection, True, thought_size)
        
def run_server(address):
    SLEEP_SECONDS_DELAY             = 1
    
    server_ip_str, server_port_int  = address
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind((server_ip_str, server_port_int))
    server.listen(5)
    
    while True:        
        # Accept client
        conn, addr                                          = server.accept()
        
        # Recive thought header from client
        thought_header                                      = recive_thought_header(conn)

        # Parsing thought
        (datetime_formatted, user_id_number, thought_size)  = CThought.parse_thought_header(thought_header)

        # Recive thought data from client
        raw_thought_data                                    = recive_thought_data(conn, thought_size)
        
        actual_thought_data_size                            = len(raw_thought_data)
        
        # If thought data dosen't match thought size 
        if (actual_thought_data_size != thought_size):
            raise RuntimeError(CThought.ERROR_DATA_INCOMPLETE)
        
        # Parse thought data
        parsed_thought_data                                 = CThought.parse_thought_data(raw_thought_data)
            
        # Sleeping to simulate computation
        time.sleep(SLEEP_SECONDS_DELAY)
            
        # Printing thought
        print("[{0}] user {1}: {2}".format(datetime_formatted, user_id_number, parsed_thought_data))
    
def main(argv):
    if len(argv) != 2:
        print(f'USAGE: {argv[0]} <address>')
        return 1
    try:
        file, raw_address = argv
        
        # Parse server address
        server_ip_str, server_port_str  = raw_address.split(":")
        server_port_int                 = int(server_port_str)
        
        # Setting address
        address                         = (server_ip_str, server_port_int)
        
        # Running server
        run_server(address)
        
        # Print done
        print('done')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
