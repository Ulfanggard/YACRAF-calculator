import os
import tkinter as tk

from program_paths import *
from settings import Settings

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
    
    
    
BACKGROUND_COLOR = "white" # Window default value
GUI_BLOCK_START_COORDINATES = ((10, 10), (12, 12)) # Default grid coordinates when creating new blocks, where subsequent values are used when multiple blocks are created at the same time to avoid stacking

# Available types of attribute values
SYMBOL_VALUE_TYPE_NUMBER = "N"
SYMBOL_VALUE_TYPE_TRIANGLE = "T"
# Symbol, explaining text, and number of values delimited by "/"
ACTIVE_VALUE_TYPE_SYMBOLS_CONFIGS = [("", "Simple text (no calculations)", None), \
                                     (SYMBOL_VALUE_TYPE_NUMBER, "Number (integer or float)", 1), \
                                     (SYMBOL_VALUE_TYPE_TRIANGLE, "Triangle distribution (a / b / c)", 3)]

# Available types of calculation operations between input attribute values
SYMBOL_CALCULATION_TYPE_MEAN = "M"
SYMBOL_CALCULATION_TYPE_AND = "&"
SYMBOL_CALCULATION_TYPE_OR = "|"
SYMBOL_CALCULATION_TYPE_MULTIPLICATION = "*"
SYMBOL_CALCULATION_TYPE_TRIANGLE = "T"
SYMBOL_CALCULATION_TYPE_QUALITATIVE = "Q"
# Symbol and explaining text
ACTIVE_CALCULATION_TYPE_SYMBOLS_CONFIGS = [(SYMBOL_CALCULATION_TYPE_MEAN, "Mean of inputs"), \
                                           (SYMBOL_CALCULATION_TYPE_AND, "AND (addition) of inputs"), \
                                           (SYMBOL_CALCULATION_TYPE_OR, "OR (minimum) of inputs"), \
                                           (SYMBOL_CALCULATION_TYPE_MULTIPLICATION, "Multiplication of input values"), \
                                           (SYMBOL_CALCULATION_TYPE_TRIANGLE, "Sample two triangle distributions - ratio of input (1) > (2)"), \
                                           (SYMBOL_CALCULATION_TYPE_QUALITATIVE, "Manual and qualitative evaluation of inputs")]

# Which calculation operations rely on the order of inputs
ENUMERATED_INPUT_CALCULATION_TYPE_SYMBOLS = [SYMBOL_CALCULATION_TYPE_TRIANGLE]

# Default text values
FONT = ("Arial", 11)
FONT_DECREASE_LINE_BREAK = 3
TEXT_COLOR = "black"

OUTLINE_WIDTH = 1
OUTLINE_COLOR = "black"

# The width of class blocks in setup views compared to configuration views
SETUP_WIDTH_MULTIPLIER = 2

DEFAULT_INPUT_SCALAR = 1



# Highlight around blocks
HIGHLIGHT_BORDER_WIDTH = 4
HIGHLIGHT_SELECTED_COLOR = "cyan" # Selecting a block
HIGHLIGHT_INPUT_COLOR = "orange" # Showing which currently connected setup attributes are considered when calculating an attribute value

# Class block
CLASS_WIDTH = 5
CLASS_HEIGHT = 1
CLASS_COLOR = "gray"

# Attribute block
ATTRIBUTE_WIDTH = CLASS_WIDTH
ATTRIBUTE_HEIGHT = 1
ATTRIBUTE_TEXT_OFFSET = 5
ATTRIBUTE_COLOR = "lightgray"

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
SETTINGS_COLOR = "cyan"
SETTINGS_POSITION = (0, settings.get_canvas_height() / LENGTH_UNIT - SETTINGS_HEIGHT)

# Save button
SAVE_WIDTH = SETTINGS_WIDTH
SAVE_HEIGHT = SETTINGS_HEIGHT
SAVE_COLOR = SETTINGS_COLOR
SAVE_POSITION = (0, settings.get_canvas_height() / LENGTH_UNIT - SETTINGS_HEIGHT - SAVE_HEIGHT)

# Change view buttons
CHANGE_VIEW_WIDTH = 5
CHANGE_VIEW_HEIGHT = 1
CHANGE_VIEW_COLOR = "orange"
CHANGE_VIEW_SELECTED_COLOR = "cyan"
CHANGE_VIEW_CONFIGURATION_START_POSITION = (settings.get_canvas_width() / LENGTH_UNIT - 2 * CHANGE_VIEW_WIDTH, 0)
CHANGE_VIEW_SETUP_START_POSITION = (settings.get_canvas_width() / LENGTH_UNIT - CHANGE_VIEW_WIDTH, 0)

# Button for create a new configuration class in the current configuration view
ADD_CLASS_WIDTH = 5
ADD_CLASS_HEIGHT = 1
ADD_CLASS_COLOR = "green"
ADD_CLASS_POSITION = (0, 0)

# Button for creating an input block in the current configuration view
ADD_INPUT_WIDTH = ADD_CLASS_WIDTH
ADD_INPUT_HEIGHT = ADD_CLASS_HEIGHT
ADD_INPUT_COLOR = ADD_CLASS_COLOR
ADD_INPUT_POSITION = (0, ADD_CLASS_HEIGHT)

# Button for adding class from configuration views to the current setup view
ADD_TO_SETUP_WIDTH = ADD_CLASS_WIDTH
ADD_TO_SETUP_HEIGHT = ADD_CLASS_HEIGHT
ADD_TO_SETUP_COLOR = ADD_CLASS_COLOR
ADD_TO_SETUP_START_POSITION = (0, 0)

# Add directional connection to setup view
ADD_CONNECTION_WIDTH = ADD_CLASS_WIDTH
ADD_CONNECTION_HEIGHT = ADD_CLASS_HEIGHT
ADD_CONNECTION_COLOR = "cyan"
ADD_CONNECTION_POSITION = (settings.get_canvas_width() / (2 * LENGTH_UNIT) - ADD_CONNECTION_WIDTH, 0)

# Button for calculating values in all setup views
CALCULATE_VALUES_WIDTH = ADD_CLASS_WIDTH
CALCULATE_VALUES_HEIGHT = ADD_CLASS_HEIGHT
CALCULATE_VALUES_COLOR = "cyan"
CALCULATE_VALUES_POSITION = (settings.get_canvas_width() / (2 * LENGTH_UNIT), 0)

# Button found at the bottom of a class block that adds another attribute to the class
ADD_ATTRIBUTE_WIDTH = 1
ADD_ATTRIBUTE_HEIGHT = 1
ADD_ATTRIBUTE_COLOR = "green"
ADD_ATTRIBUTE_OFFSET_POSITION = (ATTRIBUTE_WIDTH // 2, 0)

# Button found at the bottom of all buttons that change view that adds another view
ADD_CHANGE_VIEW_WIDTH = ADD_ATTRIBUTE_WIDTH
ADD_CHANGE_VIEW_HEIGHT = ADD_ATTRIBUTE_HEIGHT
ADD_CHANGE_VIEW_COLOR = ADD_ATTRIBUTE_COLOR
ADD_CHANGE_VIEW_CONFIGURATION_X = CHANGE_VIEW_CONFIGURATION_START_POSITION[0] + CHANGE_VIEW_WIDTH // 2
ADD_CHANGE_VIEW_SETUP_X = CHANGE_VIEW_SETUP_START_POSITION[0] + CHANGE_VIEW_WIDTH // 2

# Button for running scripts in setup views
RUN_SCRIPT_WIDTH = 5
RUN_SCRIPT_HEIGHT = 1
RUN_SCRIPT_COLOR = "red"
RUN_SCRIPT_CLEAR_COLOR = "gray"
RUN_SCRIPT_START_POSITION = (settings.get_canvas_width() / LENGTH_UNIT - RUN_SCRIPT_WIDTH, settings.get_canvas_height() / LENGTH_UNIT - RUN_SCRIPT_HEIGHT)



# Indicator for which order input attributes are considered when calculating
NUM_ORDER_CIRCLE_RADIUS = ATTRIBUTE_HEIGHT / 3
NUM_ORDER_CIRCLE_OUTLINE = 2
NUM_ORDER_CIRCLE_COLOR = "orange"

# Indicator for which other classes a class is a copy and linked to
LINKED_GROUP_CIRCLE_RADIUS = NUM_ORDER_CIRCLE_RADIUS
LINKED_GROUP_CIRCLE_OUTLINE = NUM_ORDER_CIRCLE_OUTLINE
LINKED_GROUP_CIRCLE_COLOR = "cyan"

# Indicator for scalar applied on input values in configuration views
INPUT_SCALAR_CIRCLE_RADIUS = ATTRIBUTE_HEIGHT / 2
INPUT_SCALAR_CIRCLE_OUTLINE = NUM_ORDER_CIRCLE_OUTLINE
INPUT_SCALAR_CIRCLE_COLOR = "red"

# Indicator for scalars applied on input values in setup views
INPUT_SCALARS_INDICATOR_WIDTH = 3
INPUT_SCALARS_INDICATOR_HEIGHT = 1
INPUT_SCALARS_INDICATOR_COLOR = "red"

# Indicator placed by script in setup views
SCRIPT_MARKER_CIRCLE_RADIUS = ATTRIBUTE_HEIGHT / 2
SCRIPT_MARKER_CIRCLE_OUTLINE = NUM_ORDER_CIRCLE_OUTLINE



# Used in the option windows that pop up
OPTION_FIELDS_PADDING = 5
OPTION_RADIO_BUTTON_CONFIGURATION_ATTRIBUTE_WIDTH = 10
OPTION_RADIO_BUTTON_CONFIGURATION_INPUT_WIDTH = 50



# Tags used to find specific items
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