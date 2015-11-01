import os
import sys
from .xcconfig_line_resolver import *

class xcconfig(object):
    
    def __init__(self, path):
        self.path = path;
        self.lines = [];
        
        
        if self.path != None:
            config_lines = [];
            if os.path.exists(self.path):
                config_lines = [line.strip() for line in open(self.path)];
        
            for line in config_lines:
                line_type = xcconfig_line_type(line);
                type_constructor = xcconfig_line_resolver(line, line_type);
                if type_constructor[0] == True:
                    line_obj = type_constructor[1](line);
                    self.lines.append(line_obj);
    
    @classmethod
    def pathForBuiltinConfigWithName(self, name):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), name);
