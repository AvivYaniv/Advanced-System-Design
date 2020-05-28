import socket

class Connection:
    NOT_ALL_DATA_RECEIVED_ERROR  =   'Error! not all data received'
    
    def __init__(self, sock):
        self.sock = sock
    
    def __repr__(self):
        local_ip, local_port = self.sock.getsockname()
        other_ip, other_port = self.sock.getpeername()
        return f'<Connection from {local_ip}:{local_port} to {other_ip}:{other_port}>'

    def send(self, data):
        self.sock.sendall(data)

    def receive(self, size):
        from_client = b''
        remaining_to_recive = size    
        while 0 < remaining_to_recive:
             data = self.sock.recv(remaining_to_recive)
             if not data: break             
             from_client += data
             remaining_to_recive -= len(data)  
        if 0 < remaining_to_recive:
            raise RuntimeError(Connection.NOT_ALL_DATA_RECEIVED_ERROR)
        return from_client 
    
    def close(self):
        self.sock.close()
    