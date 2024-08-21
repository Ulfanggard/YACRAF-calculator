import os
import tkinter as tk

from program_paths import *
from settings import Settings
from general_calculations import *

settings = Settings()

# The pixel width of each block in the grid
LENGTH_UNIT = 25
LENGTH_UNIT_ZOOM_LIMITS = (5, 50)



# File paths
SAVES_DIRECTORY = "saved_views"
SCRIPTS_PATHS = [os.path.join(BASE_PATH, "scripts")]

if settings.is_testing():
    TESTING_DIRECTORY = "testing"
    TESTING_PATH = os.path.join(BASE_PATH, TESTING_DIRECTORY)
    
    SAVES_DIRECTORY = os.path.join(TESTING_DIRECTORY, SAVES_DIRECTORY)
    SCRIPTS_PATHS.append(os.path.join(TESTING_PATH, "scripts"))
    
SAVES_PATH = os.path.join(BASE_PATH, SAVES_DIRECTORY)
FILE_PATHS_SAVES_PATH = os.path.join(SAVES_PATH, "view_file_paths.csv")
CONFIGURATION_SAVES_DIRECTORY = os.path.join(SAVES_DIRECTORY, "configurations")
SETUP_SAVES_DIRECTORY = os.path.join(SAVES_DIRECTORY, "setups")

# Ensure directories exist
for saves_directory in [CONFIGURATION_SAVES_DIRECTORY, SETUP_SAVES_DIRECTORY]:
    os.makedirs(os.path.join(BASE_PATH, saves_directory), exist_ok=True)
    
for script_path in SCRIPTS_PATHS:
    os.makedirs(script_path, exist_ok=True)
    
    
    

# Available types of attribute values
VALUE_TYPES = (ValueTypeString, ValueTypeNumber, ValueTypeTriangleDistribution)

# Available types of calculation operations between input attribute values
CALCULATION_TYPES = (CalculationTypeMean, CalculationTypeAND, CalculationTypeOR, CalculationTypeMultiplication, CalculationTypeSampleTriangle, CalculationTypeQualitative)



BACKGROUND_COLOR = "white" # Window default value

# Default text values
FONT = ("Arial", 11)
FONT_DECREASE_LINE_BREAK = 3
TEXT_COLOR = "black"

OUTLINE_WIDTH = 1
OUTLINE_COLOR = "black"

# The width of class blocks in setup views compared to configuration views
SETUP_WIDTH_MULTIPLIER = 2

SELECT_COLOR = "cyan"



# Highlight around blocks
HIGHLIGHT_BORDER_WIDTH = 4
HIGHLIGHT_SELECTED_COLOR = SELECT_COLOR # Selecting a block
HIGHLIGHT_INPUT_COLOR = "orange" # Showing which currently connected setup attributes are considered when calculating an attribute value
HIGHLIGHT_OPTIONS = "light green" # Border around options

# Class block
CLASS_WIDTH = 5
CLASS_HEIGHT = 1
CLASS_COLOR = "gray"

# Attribute block
ATTRIBUTE_WIDTH = CLASS_WIDTH
ATTRIBUTE_HEIGHT = 1
ATTRIBUTE_TEXT_OFFSET = 5
ATTRIBUTE_COLOR = "light gray"

# Input block in configuration views
INPUT_WIDTH = CLASS_HEIGHT
INPUT_HEIGHT = CLASS_HEIGHT
INPUT_COLOR = "orange"

# Connections
CONNECTION_WIDTH = 2
CONNECTION_COLOR = "black"
CONNECTION_END_WIDTH = CLASS_HEIGHT # Used for triangle in setup views
CONNECTION_END_HEIGHT = CLASS_HEIGHT # Used for triangle in setup views
CONNECTION_END_COLOR = "black" # Used for triangle in setup views
CONNECTION_DASH = (5, 2) # Used for external connections in configuration view
CORNER_WIDTH = CLASS_HEIGHT / 4
CORNER_HEIGHT = CLASS_HEIGHT / 4
CORNER_COLOR = "black"



# Settings button
SETTINGS_WIDTH = 4
SETTINGS_HEIGHT = 1
SETTINGS_COLOR = "light green"

# Save button
SAVE_WIDTH = SETTINGS_WIDTH
SAVE_HEIGHT = SETTINGS_HEIGHT
SAVE_COLOR = SETTINGS_COLOR

# Change view buttons
CHANGE_VIEW_WIDTH = 5
CHANGE_VIEW_HEIGHT = 1
CHANGE_VIEW_COLOR = "orange"
CHANGE_VIEW_SELECTED_COLOR = SELECT_COLOR

# Button for create a new configuration class in the current configuration view
ADD_CLASS_WIDTH = 5
ADD_CLASS_HEIGHT = 1
ADD_CLASS_COLOR = "green"

# Button for creating an input block in the current configuration view
ADD_INPUT_WIDTH = ADD_CLASS_WIDTH
ADD_INPUT_HEIGHT = ADD_CLASS_HEIGHT
ADD_INPUT_COLOR = ADD_CLASS_COLOR

# Button for adding class from configuration views to the current setup view
ADD_TO_SETUP_WIDTH = ADD_CLASS_WIDTH
ADD_TO_SETUP_HEIGHT = ADD_CLASS_HEIGHT
ADD_TO_SETUP_COLOR = ADD_CLASS_COLOR

# Add directional connection to setup view
ADD_CONNECTION_WIDTH = ADD_CLASS_WIDTH
ADD_CONNECTION_HEIGHT = ADD_CLASS_HEIGHT
ADD_CONNECTION_COLOR = "light green"

# Button for calculating values in all setup views
CALCULATE_VALUES_WIDTH = ADD_CLASS_WIDTH
CALCULATE_VALUES_HEIGHT = ADD_CLASS_HEIGHT
CALCULATE_VALUES_COLOR = "light green"

# Button found at the bottom of a class block that adds another attribute to the class
ADD_ATTRIBUTE_WIDTH = 1
ADD_ATTRIBUTE_HEIGHT = 1
ADD_ATTRIBUTE_COLOR = "green"

# Button found at the bottom of all buttons that change view that adds another view
ADD_CHANGE_VIEW_WIDTH = ADD_ATTRIBUTE_WIDTH
ADD_CHANGE_VIEW_HEIGHT = ADD_ATTRIBUTE_HEIGHT
ADD_CHANGE_VIEW_COLOR = ADD_ATTRIBUTE_COLOR

# Button for running scripts in setup views
RUN_SCRIPT_WIDTH = 5
RUN_SCRIPT_HEIGHT = 1
RUN_SCRIPT_COLOR = "red"
RUN_SCRIPT_CLEAR_COLOR = "gray"



# Indicator for which order input attributes are considered when calculating
NUM_ORDER_CIRCLE_RADIUS = ATTRIBUTE_HEIGHT / 3
NUM_ORDER_CIRCLE_OUTLINE = 2
NUM_ORDER_CIRCLE_COLOR = "orange"

# Indicator for which other classes a class is a copy and linked to
LINKED_GROUP_CIRCLE_RADIUS = NUM_ORDER_CIRCLE_RADIUS
LINKED_GROUP_CIRCLE_OUTLINE = NUM_ORDER_CIRCLE_OUTLINE
LINKED_GROUP_CIRCLE_COLOR = "light green"

# Indicator for scalar and offset applied on input values in configuration views
INPUT_INDICATOR_CIRCLE_RADIUS = ATTRIBUTE_HEIGHT / 2
INPUT_INDICATOR_CIRCLE_OUTLINE = NUM_ORDER_CIRCLE_OUTLINE
INPUT_SCALAR_INDICATOR_CIRCLE_COLOR = "red"
INPUT_OFFSET_INDICATOR_CIRCLE_COLOR = "yellow"

# Indicator for scalars applied on input values in setup views
INPUT_SCALARS_INDICATOR_WIDTH = 3
INPUT_SCALARS_INDICATOR_HEIGHT = 1
INPUT_SCALARS_INDICATOR_COLOR = "red"

# Indicator placed by script in setup views
SCRIPT_MARKER_CIRCLE_RADIUS = ATTRIBUTE_HEIGHT / 2
SCRIPT_MARKER_CIRCLE_OUTLINE = NUM_ORDER_CIRCLE_OUTLINE



# Used in the option windows that pop up
OPTIONS_GRID_WIDTH = 7
OPTIONS_GRID_HEIGHT = 1
OPTIONS_TITLE_COLOR = "dim gray"
OPTIONS_HEADER_COLOR = "gray"
OPTIONS_BUTTON_COLOR = "light gray"
OPTIONS_BACKGROUND_COLOR = "gainsboro"



# Circle and square used for radio buttons and toggle buttons, respectively
BUTTON_SELECT_INDICATOR_COLOR = "white"
BUTTON_SELECT_INDICATOR_COLOR_SELECTED = "black"
BUTTON_SELECT_INDICATOR_SIZE = OPTIONS_GRID_HEIGHT * 2 / 3



# Tags used to find specific items
TAG_OPTIONS = "options"
TAG_OPTIONS_TEXT = "options_text"
TAG_OPTIONS_BACKGROUND = "options_background"
TAG_BUTTON = "button"
TAG_BUTTON_TEXT = "button_text"
TAG_INDICATOR = "number_indicator"
TAG_INDICATOR_TEXT = "number_indicator_text"
TAG_CONNECTION_LINE = "connection_line"
TAG_CONNECTION_CORNER = "connection_corner"
TAG_INPUT = "input"
TAG_INPUT_TEXT = "input_text"



# Mappings to mouse actions
MOUSE_LEFT_PRESS = "<ButtonPress-1>"
MOUSE_LEFT_DRAG = "<B1-Motion>"
MOUSE_LEFT_RELEASE = "<ButtonRelease-1>"
MOUSE_RIGHT_PRESS = "<ButtonPress-3>"
MOUSE_MOTION = "<Motion>"
MOUSE_WHEEL = "<MouseWheel>"
MOUSE_WHEEL_UP = "<Button-4>"
MOUSE_WHEEL_DOWN = "<Button-5>"

MOUSE_PRESS = "MOUSE_PRESSABLE"
MOUSE_DRAG = "MOUSE_DRAGGABLE"
