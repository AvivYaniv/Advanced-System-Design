from pathlib import Path
import http.server
from _datetime import datetime
from functools import partial 

from website import Website 

web_server = Website()

class CDataConverter():
    @staticmethod
    def getBytesFromString(str, encoding = 'utf-8'):
        return bytes(str.encode(encoding))

class CThoughtsFileSystem():  
    @staticmethod
    def getFileNameWithoutExtension(file_path):
        return Path(file_path).stem
           
    @staticmethod
    def readFile(file_path):
        file_exists = Path(file_path).is_file()
        if not file_exists:
            return ''
        
        lines = []        
        with open(file_path, "r") as file:
            lines = file.readlines()               
            file.close()
            
        return lines
    
    @staticmethod
    def getUsersDirs(data_dir):
        users = []
        path_data_dir = Path(data_dir)
        for user_dir in path_data_dir.iterdir():
            users.append(user_dir.name)
        return users
          
    @staticmethod
    def getFilesUnderDir(data_dir, extension='*'):
        p = Path(data_dir).glob(extension)
        files = [x for x in p if x.is_file()]
        return files
          
    @staticmethod
    def getUsersHTML(data_dir):
        _INDEX_HTML = \
        '''
        <html>
            <head></head>
            <body>
                <ul>
                    {users}
                </ul>
            </body>
        </html>
        '''
        _USER_LINE_HTML = '''
        <li><a href="/users/{user_id}">user {user_id}</a></li>
        '''
    
        users_html = []    
        users_dirs = CThoughtsFileSystem.getUsersDirs(data_dir)
        users_dirs.sort()    
        for user_dir in users_dirs:
            users_html.append(_USER_LINE_HTML.format(user_id=user_dir))
        
        index_html = _INDEX_HTML.format(users='\n'.join(users_html))
        
        return index_html
    
    @staticmethod
    def getUserThoughtsHTML(data_dir, user_id):        
        _USER_THOUGHTS_TITLE_ = f'<title>Brain Computer Interface: User {user_id}</title>' 
        
        _USER_THOUGHTS_HTML = \
        '''
        <html>
            <head>
                {user_title}
            </head>
            <body>
                <table>                
                    {thoughts}
                </table>
            </body>
        </html>
        '''
        
        _THOUGHT_LINE_HTML = \
        '''
        <tr>
            <td>{thought_name}</td>
            <td>{thought_data}</td>
        </tr>
        '''
        
        thoughts_html = [] 
        thoughts_files = CThoughtsFileSystem.getFilesUnderDir(f'{data_dir}/{user_id}', '*.txt')
        thoughts_files.sort(reverse=True)       
        for thought_file_path in thoughts_files:
            thought_file_name = \
                CThoughtsFileSystem.getFileNameWithoutExtension(thought_file_path)
            thought_file_data = \
                CThoughtsFileSystem.readFile(thought_file_path)
            for thought_file_line in thought_file_data:                
                thoughts_html.append( \
                    _THOUGHT_LINE_HTML.format( \
                        thought_name=datetime \
                            .strptime(thought_file_name, '%Y-%m-%d_%H-%M-%S')\
                            .strftime('%Y-%m-%d %H:%M:%S'), \
                        thought_data=thought_file_line))
                    
        user_thoughts_html = \
            _USER_THOUGHTS_HTML.format( \
                user_title=_USER_THOUGHTS_TITLE_, \
                thoughts='\n'.join(thoughts_html))
        
        return user_thoughts_html

selected_data_dir = ''
    
@staticmethod
def getPageNotFoundResponse():
    return 404, ''
    
@web_server.route('/')
def index():
    # Return users
    data_str    = CThoughtsFileSystem.getUsersHTML(selected_data_dir)
    return 200, data_str

@staticmethod
@web_server.route('/users/([0-9]+)')
def user(user_id):
    # If user ID not found
    if user_id not in CThoughtsFileSystem.getUsersDirs(selected_data_dir):
        return getPageNotFoundResponse()
    
    # Return user thoughts
    data_str    = CThoughtsFileSystem.getUserThoughtsHTML(selected_data_dir, user_id)
    return 200, data_str

def run_webserver(address, data_dir):
    server_ip_str, server_port_int  = address
    global selected_data_dir
    selected_data_dir = data_dir
    web_server.run(address)

def main(argv):
    if 3 != len(argv):
        print(f'USAGE: {argv[0]} <address> <data_dir>')
        return 1
    try:
        file, raw_address, data_dir = argv
        
        # Parse server address
        server_ip_str, server_port_str  = raw_address.split(":")
        server_port_int                 = int(server_port_str)
        
        # Setting address
        address                         = (server_ip_str, server_port_int)
        
        # Running server
        run_webserver(address, data_dir)
        
        # Print done
        print('done')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    