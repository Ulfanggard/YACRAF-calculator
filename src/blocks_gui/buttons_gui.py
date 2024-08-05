import os
import importlib.util
from helper_functions import convert_grid_coordinate_to_actual
from general_gui import GUIModelingBlock
from options import OptionsView
from script_interface import ScriptInterface
from config import *

class GUIBlockButton(GUIModelingBlock):
    def __init__(self, model, view, text, x, y, width, height, fill_color):
        super().__init__(model, view, text, x, y, width, height, fill_color, bind_left=MOUSE_PRESS)
        
    def left_pressed(self, event):
        pass
        
    """
    def set_text(self, text):
        self.get_canvas().itemconfig(self.__label, text=text)
        
    def delete(self):
        self.get_canvas().delete(self.__rect)
        self.get_canvas().delete(self.__label)
    """
        
class GUIAddAttributeButton(GUIBlockButton):
    def __init__(self, model, view, x, y, configuration_class_gui):
        super().__init__(model, view, "+", x, y, ADD_ATTRIBUTE_WIDTH, ADD_ATTRIBUTE_HEIGHT, ADD_ATTRIBUTE_COLOR)
        self.__configuration_class_gui = configuration_class_gui
        
    def left_pressed(self, event):
        self.__configuration_class_gui.create_attribute()
        
class GUIAddChangeViewButton(GUIBlockButton):
    def __init__(self, model, view, x, y, is_configuration_view):
        super().__init__(model, view, "+", x, y, ADD_CHANGE_VIEW_WIDTH, ADD_CHANGE_VIEW_HEIGHT, ADD_CHANGE_VIEW_COLOR)
        self.__is_configuration_view = is_configuration_view
        
    def left_pressed(self, event):
        if self.__is_configuration_view:
            self.get_model().create_view(True, "New configuration")
        else:
            self.get_model().create_view(False, "New setup")
        
class GUISaveButton(GUIBlockButton):
    def __init__(self, model, view, x, y):
        super().__init__(model, view, "Save", x, y, SAVE_WIDTH, SAVE_HEIGHT, SAVE_COLOR)
        
    def left_pressed(self, event):
        self.get_model().save()
        
class GUIChangeViewButton(GUIBlockButton):
    def __init__(self, model, view, x, y, view_name, view_to_change_to):
        if view == view_to_change_to:
            color = CHANGE_VIEW_SELECTED_COLOR
        else:
            color = CHANGE_VIEW_COLOR
            
        super().__init__(model, view, view_name, x, y, CHANGE_VIEW_WIDTH, CHANGE_VIEW_HEIGHT, color)
        self.__view_to_change_to = view_to_change_to
        
    def left_pressed(self, event):
        self.get_model().change_view(self.__view_to_change_to)
        
class GUIAddConfigurationClassButton(GUIBlockButton):
    def __init__(self, model, view, x, y):
        super().__init__(model, view, "Add class", x, y, ADD_CLASS_WIDTH, ADD_CLASS_HEIGHT, ADD_CLASS_COLOR)
        
    def left_pressed(self, event):
        self.get_view().create_configuration_class_gui()
        
class GUIAddToSetupButton(GUIBlockButton):
    def __init__(self, model, view, x, y, configuration_class_gui):
        super().__init__(model, view, configuration_class_gui.get_name(), x, y, ADD_TO_SETUP_WIDTH, ADD_TO_SETUP_HEIGHT, ADD_TO_SETUP_COLOR)
        self.__configuration_class_gui = configuration_class_gui
        
        configuration_class_gui.add_to_setup_button(view, self)
        
    def left_pressed(self, event):
        self.get_view().create_setup_class_gui(self.__configuration_class_gui)
        
class GUIAddInputButton(GUIBlockButton):
    def __init__(self, model, view, x, y):
        super().__init__(model, view, "Add input", x, y, ADD_INPUT_WIDTH, ADD_INPUT_HEIGHT, ADD_INPUT_COLOR)
        
    def left_pressed(self, event):
        self.get_view().create_configuration_input_gui()
        
class GUICalculateValuesButton(GUIBlockButton):
    def __init__(self, model, view, x, y):
        super().__init__(model, view, "Calculate", x, y, CALCULATE_VALUES_WIDTH, CALCULATE_VALUES_HEIGHT, CALCULATE_VALUES_COLOR)
        
    def left_pressed(self, event):
        self.get_model().calculate_values()
        
class GUIAddConnectionButton(GUIBlockButton):
    def __init__(self, model, view, x, y):
        super().__init__(model, view, "Connection", x, y, ADD_CONNECTION_WIDTH, ADD_CONNECTION_HEIGHT, ADD_CONNECTION_COLOR)
        
    def left_pressed(self, event):
        self.get_view().create_connection_with_blocks()
        
class GUIRunScriptButton(GUIBlockButton):
    def __init__(self, model, view, script_name, x, y, is_clear_button=False):
        if not is_clear_button:
            color = RUN_SCRIPT_COLOR
        else:
            color = RUN_SCRIPT_CLEAR_COLOR
            
        super().__init__(model, view, script_name, x, y, RUN_SCRIPT_WIDTH, RUN_SCRIPT_HEIGHT, color)
        self.__script_interface = ScriptInterface(model)
        self.__is_clear_button = is_clear_button
        
        if not is_clear_button:
            # Import the module of the script
            script_path = os.path.join(BASE_PATH, SCRIPTS_PATH, f"{script_name}.py")
            spec = importlib.util.spec_from_file_location(script_name, script_path)
            self.__script_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.__script_module)
            
    def left_pressed(self, event):
        if self.__is_clear_button:
            self.get_model().reset_script_changes()
            
        else:
            self.__script_module.script_control(self.__script_interface)