from .xcconfig_item_base import *
from xcrunHelper.xcrun import xcrun
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
            path = path.replace('<DEVELOPER_DIR>', xcrun.resolve_developer_path(), 1);
        if path[0] != '/':
            path = os.path.join(base_path, path);
        print path
        return os.path.normpath(path);