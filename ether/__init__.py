import sys
import types
class TestClass:
    def __init__(self, test):
        self.__test = test
    def __str__(self):
        return "Generated Test Class is Actually Working. Test String {}".format(self.__test)
class EtherLoader:
    def __init__(self):
        self.modules = []

    def find_module(self, fullname, path=None):
        if 'ether' in fullname:
            self.modules.append(fullname)
            return self
        return None
    
    def load_module(self, name):
        module = types.ModuleType(name)
        module.__loader__ = self
        sys.modules[name] = module
        module.__dict__['GeneratedClass'] = TestClass
        return module

sys.meta_path = [EtherLoader()]