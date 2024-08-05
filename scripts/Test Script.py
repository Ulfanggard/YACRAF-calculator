# Available functions:

# Meaning of values passed to methods for finding/matching blocks in setup views, where None considers all:
# class_type: Name of class type (for example, Attack event)
# class_instance: Name of class instance (for example, DoS attack)
# attribute: Name of attribute (for example, Local difficulty)
# view: Setup view name to consider, where None considers all

# script_if.get_class_type_names(view=None)
#     Returns a list of class names (those specified in configuration views) found in the specified setup views

# script_if.get_class_instance_names(class_type, view=None)
#     Returns a list of class instance names (those specified in setup views) found in the specified setup views

# script_if.get_attribute_names(class_type)
#     Returns a list of attribute names for a specific class type

# script_if.get_input_class_names(class_type, class_instance)
#     Returns a list of tuples including the class type and class instance names of all classes which the specified setup class instance takes input fro
#     [(input_class_type, input_class_instance), ...]

# script_if.get_attribute_value(class_type, class_instance, attribute, view=None)
#     Returns the value displayed by a specific setup attribute, which is a list if there are overlapping attribute names for a specific class type

# script_if.override_attribute_values(override_value, *, class_type=None, class_instance=None, attribute=None, view=None)
#     Overrides the displayed value of matching attributes with a temporary one

# script_if.reset_override_attribute_values(*, class_type=None, class_instance=None, attribute=None, view=None)
#     Resets any override value of matching attributes

# script_if.set_class_marker(value, color, *, class_type=None, class_instance=None, view=None)
#     Adds a visual marker on all matching class instances

# script_if.calculate_values()
#     Calculates all attribute values in the setup views based on the current configuration

def script_logic(script_if):
    # Insert logic here
    print("Class types in all views: " + str(script_if.get_class_type_names()))
    print("Class types in first view: " + str(script_if.get_class_type_names("Setup 1")))
    
    print("Class instances of Attack event AND in all views: " + str(script_if.get_class_instance_names("Attack event AND")))
    print("Class instances of Attack event AND in first view: " + str(script_if.get_class_instance_names("Attack event AND", "Setup 1")))
    
    print("Attributes of Attack event AND: " + str(script_if.get_attribute_names("Attack event AND")))
    
    print("Input classes to Attack event AND: Top 1: " + str(script_if.get_input_class_names("Attack event AND", "Top 1")))
    
    print("Value of Global difficulty in Attack event AND: Top 1: " + str(script_if.get_attribute_value("Attack event AND", "Top 1", "Global difficulty")))
    
    script_if.override_attribute_values("0 / 1 / 2", class_type="Attack event AND", class_instance="Top 1", attribute="Local difficulty")
    
    script_if.override_attribute_values("0 / 1 / 2", class_type="Attack event AND", class_instance="Top 1", attribute="Global difficulty")
    script_if.reset_override_attribute_values(class_type="Attack event AND", class_instance="Top 1", attribute="Global difficulty")
    
    script_if.set_class_marker("A", "red", class_type="Attack event AND", class_instance="Top 1")
    script_if.set_class_marker("B", "blue", class_type="Attack event AND", class_instance="Top 1")
    script_if.set_class_marker("C", "yellow", class_type="Attack event AND", class_instance="Left 1")
    script_if.set_class_marker("D", "green", class_type="Attack event AND", class_instance="Right 1")
    
    script_if.calculate_values()
    
def script_control(script_if):
    script_if.update_setup_structure()
    script_if.reset_script_changes()
    script_logic(script_if)