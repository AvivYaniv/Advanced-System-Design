from pathlib import Path, PurePath
import time
import socket
from thought import *
from listener import *
from datetime import datetime
from struct import *

import threading
        
class CConnectionReciver:
    def __init__(self, connection):
        self.connection = connection
    
    def recive_data(self, is_close_after, amount):
        from_client = self.connection.receive(amount)
        if is_close_after:         
            self.connection.close()          
        return from_client           
        
class CHandler(threading.Thread):
    lock       = threading.Lock()
    def __init__(self, connection, data_dir):    
        super().__init__()
        self.connection = connection    
        self.reciver    = CConnectionReciver(connection)
        self.data_dir   = data_dir

    def recive_thought_header(self):
        return self.reciver.recive_data(False, Thought.HEADER_SIZE)
        
    def recive_thought_data(self, thought_size):
        return self.reciver.recive_data(True, thought_size)
    
    def write_append_file(self, file_path, data_line):        
        self.lock.acquire()
        try:
            file_existed = Path(file_path).is_file()
            with open(file_path, "a+") as file:                             
                if file_existed:
                    file.write('\n')                
                file.write(data_line)
                file.flush()   
                file.close()             
        finally:            
            self.lock.release()
        
    @staticmethod
    def toSafeFileName(str):
        return str.replace(":", "-")
        
    def write_user_thought(self, datetime_formatted, user_id_number, thought_data):
        # Creating path
        user_dir        = str(user_id_number)
        thought_file    = CHandler.toSafeFileName(datetime_formatted) + '.txt'
        
        thought_file_dir = PurePath(self.data_dir, user_dir)
        
        Path(thought_file_dir).mkdir(parents=True, exist_ok=True)
        
        thought_file_path = PurePath(thought_file_dir, thought_file)
        
        # Write user thought
        self.write_append_file(thought_file_path, thought_data)
    
    def run(self): # start invokes run  		
        # Recive thought header from client
        thought_header                                      = self.recive_thought_header()

        # Parsing thought
        (datetime_raw, user_id_number, thought_size)        = Thought.parse_thought_header(thought_header)

        # Recive thought data from client
        raw_thought_data                                    = self.recive_thought_data(thought_size)
        
        actual_thought_data_size                            = len(raw_thought_data)
        
        # If thought data dosen't match thought size 
        if (actual_thought_data_size != thought_size):
            raise RuntimeError(Thought.ERROR_DATA_INCOMPLETE)
        
        # Parse thought data
        parsed_thought_data                                 = Thought.parse_thought_data(raw_thought_data)
        
        datetime_formatted                                  = datetime_raw.strftime(Thought.DATETIME_FORMAT)
        
        # Writing user thought to disk
        self.write_user_thought(datetime_formatted, user_id_number, parsed_thought_data)

from cli import CommandLineInterface

cli = CommandLineInterface()
      
@cli.command  
def run(address, data):  
    # Parse server address
    server_ip_str, server_port_str  = address.split(":")
    server_port_int                 = int(server_port_str)
    
    listener = Listener(server_port_int, server_ip_str)
    listener.start()
	
    while True:
    	# Accept client		
    	connection = listener.accept()  
    	
    	# Initialize client CHandler
    	handler = CHandler(connection, data)    
    	
    	# Handle client
    	handler.start()

if __name__ == '__main__':
    import sys    
    sys.exit(cli.main())
