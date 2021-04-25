try:
    import Tkinter as tkinter
except ImportError:
    import tkinter

ModuleVersion = None


def enable(interpreter):
    """Imports the module to the provided Tk/Tcl interpreter"""
    global ModuleVersion
    try:
        import os.path
        import platform

        supported = ["Darwin", "Linux", "Windows"] #Supported platforms
        if platform.system() in supported: pass
        else: raise RuntimeError('Platform not supported.')
        
        module_path = os.path.join(os.path.dirname(__file__), 'extrafont')
        interpreter.tk.call('lappend', 'auto_path', module_path)
       ModuleVersion = interpreter.tk.call('package', 'require', 'module_name_here')
    except tkinter.TclError:
        raise RuntimeError('Unable to load library.')
    return ModuleVersion

def func1(interpreter):
    """No arguments function"""
    interpreter.tk.call('module_name_here::module_function')
 
def func2(interpreter, argument):
    """One argument function"""
    interpreter.tk.call('module_name_here::module_function', argument)
