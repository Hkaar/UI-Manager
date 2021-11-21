# UI Manager
*A UI Manager for PyQt & PySide*

**Copyright(c) 2021 Hkaar**

## Overview
UI Manger aims to help you in managing your ui more easily, and faster with less
code inside your program, with a easy to use interface so it's easy to use and learn
for use in your program.

## License
UI Manager is distributed under the MIT License. For more details please see
LICENSE.txt.

**Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the “Software”), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:**

**The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.**

**THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.**

## Installation
To install UI Manager on your device type these commands:
```
pip install ui-manager
```
or 
```
python setup.py build
python setup.py install
```

## How to use
UI Manager has a few classes to work with, and some functions. Here are some
examples on how to use them:
- Theme Manager:
```
import ui_manager

theme_manager = ui_manager.Theme_Manager()

theme_manager.import_theme('dark.qss', None, 'ascii') # import your theme.
theme_manager.set_theme('dark') # set your preffered theme.

theme_manager.set_widget_theme(widget1) # set the theme to your widget.
# or
theme_manager.add_widget(widget1) # add your widget to theme manager.
theme_manager.load_theme() # load the theme to your widget.
```
or
```
import ui_manager

theme_manager = ui_manager.Theme_Manager()

theme_manager.import_theme('dark.py', 'DarkTheme', None) # import your theme, from a class you select in the file.
theme_manager.set_theme('dark') # set your preffered theme.

theme_manager.set_widget_theme(widget1, 'default') # set the selected theme to your widget, with selecting a theme object from the theme.
# or
theme_manager.add_widget(widget1) # add your widget to theme manager.
theme_manager.load_theme() # load the theme to your widget.
```

## Dependecies
PyQt5 or PySide2
