# SimpleNet
College assignment about graphs. 

The assignment was as follows:

"""
The main objective of this work is to implement an application that simulates a social network,
using the knowledge acquired in class in order to carry out loading, handling and
checking a set of in-memory data structures.
A social network can be defined as a social structure composed of people or
organizations, connected by various types of relationships, that share common values ​​and goals. You
Minimum functional requirements of the application to be developed are:
• People or organizations can create profiles on the network and are users of the application.
• People can choose to keep certain profile information private.
• People can relate to other people in different ways: friendship (two-way),
family (bidirectional) or known (unidirectional).
• People or organizations can be customers of organizations.
• Users can search for People or Organizations for any of the registered information
in profiles. The search must be carried out by levels, that is, first in those connected to the user
and then the connected to the connected and so on.
• It should be possible to visualize the social network graph centered on the user, with at least two levels.

These are non-functional requirements:
• The application must have a graphical interface to run all the functionalities.
• Interface can be operating system dependent desktop or Web
"""

For this assignment I've used PyQt for the GUI and NetworkX library for graph visualization.

###### Windows folder:
It's where all .ui files as well as their convertions to .py are located. NOTE: the .py files were manually edited after the convertion from .ui to .py. 

###### graph.png:
Last graph visualization state. This file is updated every time the visualization tool is used. 

###### back.png:
Background image.

###### mysocialnet2.pkl:
A saved instance of SimpleNet. Some users have already been registered:
    - User: ajm ; Password: 123
    - User: alessandra ; Password: 1234
    - User: FelipeM ; Password: Abacaxi
    - User: renan ; Password: 105285
    - User: org ; Password: 123
    - User: LucasK ; Password: oioi
 
 
###### myWidgets.py:
Just some additional widgets for the GUIs.

###### graphClass.py:
Graph implentation.

###### socialNet.py:
Interface between GUIs and the graph instance.

###### main.py:
Execute this to run the application. 


