"""This is the entry point of the JetCAP (Jet Engine Cycle Analysis and Performace) software GUI."""

import sys,os

#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# In the following code files, we will use any of the below mentioned code to import the modules

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # no-use since current dir is already included in the path 

# sys.path.insert(0,"\\".join(os.path.abspath(__file__).split("\\")[:-1])+"\\MAIN_GUI")

# if os.path.dirname(os.path.abspath(__file__)) not in sys.path:
#     sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from MAIN_GUI.main_window import main_window

sys.path.append(resource_path("MAIN_GUI"))
sys.path.append(resource_path("MAIN_BACKEND"))
sys.path.append(resource_path("MAIN_BACKEND\\data_files"))
sys.path.append(resource_path("MAIN_GUI\\symbols"))
sys.path.append(resource_path("MAIN_GUI\\images"))
sys.path.append(resource_path("MAIN_GUI\\themes"))

from main_window import main_window_class          #type:ignore

selected_theme= "forest-light"
main_gui= main_window_class(selected_theme)
main_gui.create_window()