# YACRAF-calculator

This is a graphical tool for doing calculations according to YACRAF (https://link.springer.com/article/10.1007/s10207-023-00713-y) used in the KTH courses EP2790 and EP279V.

## How to use

This tool allows calculations inherent to the threat modeling to be setup and calculated using graphical block diagrams, where one can place, drag, and connect different blocks across various `Views`.. The aim of the tool is to allow for the: (1) automation of the calculation process, where any changes to any block automatically propagate through the system, and (2) simulation of various scenarios.

The graphical interface consists of two types of `Views`: `Configuration Views` and `Setup Views`. `Class` blocks (for example, attack event) and their `Attributes` (for example, cost) are defined within `Configuration Views`, where one may also define connections or relationships between different `Attributes`: whether a specific `Attribute` takes other ones as input and what operation to perform between them. In practical terms, `Configuration Views` defines the metamodel used during the threat modeling. Meanwhile, `Setup Views` define the system-specific setup. That is, what instances of defined `Class` blocks exist within the analysed system, but also its system-specific connections.

### Views

In the top right corner of the GUI are two columns of buttons. These buttons switch between the different `Views` where the left-most column switches between `Configuration Views` and the right-most between `Setup Views`. The button with the `+` allows for an additional `View` to be added. The corresponding `View` can be configured by right clicking it, where one can:
1. Change its name
2. Switch their displayed order
3. Delete it

The `Save` button in the bottom left corner saves the current state of all `Configuration Views` and `Setup Views`.

### Configuration View

#### Class

A new metamodel `Class` is created by pressing the `Add class` button in the top left corner. The created `Class` can be dragged around the `Configuration View` and be configured by right clicking it, where one can
1. Change its name
2. Create a linked copy of this instance to another `Configuration View` (allowing relations between blocks across `Configuration Views`), identified by the marker in its upper right corner
3. Delete it

#### Attribute

Pressing the button with a `+` under a `Class` results in an `Attribute` being added to the `Class`, which can subsequently be edited by right clicking it, where on can:
1. Change its name
2. Change the displayed order of the `Attributes`
3. Change the type of value of the `Attribute`, such as a decimal number or a triangle distribution
4. Hide it from the corresponding `Setup Views`, meaning it is only visible in the `Configuration Views`
5. Delete it

#### Calculation input

By pressing the `Add input` in the top left corner, an `Input` block is created. `Input` blocks function take inputs from one or more `Attributes` and, through a specified mathematical operation, outputs the result to an adjacent `Attribute` that it has been dragged next to. The `Input` block can be configured by right clicking it, where one can:
1. Change its mathematical operation, for example AND, OR, multiplication, etc
2. Delete it

`Attributes` can be added as inputs (connecting them) to the `Input` block by first left clicking on the corresponding `Attribute` and then the `Input` block, creating a `Connection` between the two.

#### Connection

Right clicking a box on a `Connection` opens up its configuration, where one can:
1. Set the `Connection` as external, meaning it will only be connected to `Attributes` of other instances of its `Class` type, such as an attack event only considering the input of another attack event and not an internal `Attribute`
2. Delete it

### Setup View

#### Class

An instance of a `Class` from a `Configuration View` can be added to the current `Setup view` by pressing the corresponding button in the top left corner. The `Class` instance can be configured by right clicking it, where one can:
1. Change the name of the `Class` instance
2. Create a linked copy of the instance to another `Setup View` (any calculated value takes all linked versions into account), identified by the marker in its upper right corner
3. Delete it

#### Connection

Pressing the `Connection` button at the top creates a directional `Connection` that can be attached to `Classes` by dragging it. The `Attributes` of the `Class` that the `Connection` points to may take input from the other `Class`, if such a relation has been configured in the `Configuration Views`. Attaching a `Connecton` to a `Class` will automatically disable `Attribute` entries if the corresponding value is dependent on at least one connected `Class`. The `Connection` can be deleted by right clicking it.

#### Calculate

The `Calculate` button at the top calculate the values of all `Attributes` that do not have a entry field of all `Classes` in all `Setup Views`.

#### Scripts

Scripts to visualize or simulate different scenarios, such as finding the most optimal order of implementing defense mechanisms, or enumerating and visualising the easiest attack paths, can be created using Python scripts that interface to the tool. To create a script, create a copy of the template in the `scripts` directory and name it accordingly. Upon boot of the tool, a button to run the newly created script will appear in the bottom right corner of `Setup Views`. The scripts interface to the tool through different methods of a `ScriptInterface` class, each one explained in the top of the script file.
