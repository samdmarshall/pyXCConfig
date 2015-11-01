from .xcconfig_item_base import *
import os

class xcconfig_include(xcconfig_item_base):
    
    def __init__(self, line):
        super(xcconfig_include, self).__init__(line);
        self.type = 'INCLUDE';
    
    def includePath(self, base_path):
        quote_start = self.contents.find('"') + 1;
        path = self.contents[quote_start:];
        quote_end = path.find('"');
        path = path[:quote_end];
        if path.startswith('<DEVELOPER_DIR>'):
            developer_directory = os.environ.get('DEVELOPER_DIR')
            if not developer_directory:
                print('Could not find defined environment variable "DEVELOPER_DIR"!')
                raise Exception
            path = path.replace('<DEVELOPER_DIR>', developer_directory, 1);
        if path[0] != '/':
            path = os.path.join(base_path, path);
        print path
        return os.path.normpath(path);