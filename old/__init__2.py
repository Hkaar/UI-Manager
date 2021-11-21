# PySide2 & PyQt5 UI Manager
# Made by Hkaar

import os

try:
    from PySide2.QtCore import QFile, QIODevice
except:
    from PyQt5.QtCore import QFile, QIODevice

class Theme_Manager:
    def __init__(self, theme='light'):
        self.stored_themes = {}
        self.theme = None

        self.stored_widgets = {}

        self.import_theme('/'.join(os.path.dirname(os.path.abspath(__file__)), 
            'resources/themes'), None)

    def set_theme(self, theme='light'):
        if isinstance(theme, str) and self.stored_themes.get(theme):
            self.theme = self.stored_themes[theme]
        else:
            raise KeyError((f"There is no such theme: {theme}, due "
                "to not being a string or theme does not exist!"))

    def import_theme(self, directory, class_name=None, encoding="ascii"):
        def append_theme(file_dir, class_name, encoding):
            file_name = os.path.basename(file_dir)

            if file_name.endswith('.py'):
                theme_f = __import__(file_name.replace('.py', ''))

                if class_name != None and hasattr(theme_f, class_name):
                    theme = getattr(theme_f, class_name)
                else:
                    raise TypeError((f"There is no such class: {class_name} "
                        f"inside {file_name} file!"))

                if hasattr(theme, 'name') and hasattr(theme, 'stylesheets'):
                    if theme.name in self.stored_themes:
                        self.stored_themes[theme.name][0].stylesheets.update(theme.stylesheets)
                    else:
                        self.stored_themes[theme.name] = (theme, 'py')
                else:
                    raise KeyError((f"Theme: {class_name} does not have 'name' & "
                        "'stylesheets' keys!"))

            elif file_name.endswith('.qss'):
                sty_f = QFile(file_dir)

                if class_name != None:
                    self.stored_themes[class_name] = (sty_f, 'qss', encoding)
                else:
                    self.stored_themes[file_name.replace('.qss', '')] = (sty_f, 'qss', encoding)

            else:
                raise ImportError((f"Failed to import: {file_name} due to invalid "
                    "format or file does not exist!"))

        def import_file(file_dir, class_name, encoding):        
            if isinstance(class_name, (list, tuple)) and file_dir.endswith('.py'):
                for cls_name in class_name:
                    append_theme(file_dir, cls_name, encoding)

            elif not isinstance(class_name, (list, tuple)):
                append_theme(file_dir, class_name, encoding)

            else:
                raise TypeError(f"Cannot use: {class_name} is considered an invalid type!")

        if os.path.isfile(directory) or directory.endswith('.qss'):
            import_file(directory, class_name, encoding)

        elif os.path.isdir(directory):
            files = ['/'.join((directory, f)) for f in os.listdir(directory) if os.path.isfile(
            '/'.join((directory, f))) and f.endswith('.qss')]

            for f in files:
                f_index = files.index(f)

                if isinstance(class_name, (list, tuple)):
                    if len(class_name)-1 >= f_index:
                        import_file(f, class_name[f_index], encoding)
                    else:
                        import_file(f, None, encoding)
                else:
                    import_file(f, class_name, encoding)

        else:
            raise FileNotFoundError(f"There is no such file or directory: {directory}!")

    def add_widget(self, widget, theme='default'):
        def gen_id():
            for widget_id in range(0, 9999):
                if not self.stored_widgets.get(widget_id):
                    return widget_id
            return None

        if isinstance(theme, str):
            if isinstance(widget, (list, tuple, set)):
                for w in widget:
                    self.stored_widgets[gen_id()] = (w, theme)
            else:
                self.stored_widgets[gen_id()] = (widget, theme)
        else:
            raise TypeError(f"Cannot use: {theme} is considered an invalid type!")

    def set_widget_theme(self, widget, theme='default'):
        def apply_theme(widget, theme):
            get_name = lambda obj: obj.__class__.__name__

            if self.theme[1] == 'py':
                if theme == 'palette' and hasattr(self.theme[0], 'palette'):
                    widget.setPalette(self.theme[0].palette)
                else:
                    widget.setStyleSheet(self.theme[0].stylesheets['default'])

                    if self.theme[0].stylesheets.get(theme):
                        widget.setStyleSheet(self.theme[0].stylesheets[theme])

                if get_name(widget) != 'QApplication':
                    widget.update()

            elif self.theme[1] == 'qss':
                sty_f = self.theme[0]

                sty_f.open(QIODevice.ReadOnly)
                widget.setStyleSheet(((sty_f.readAll()).data()).decode(self.theme[2]))

                if get_name(widget) != 'QApplication':
                    widget.update()

            else:
                raise KeyError((f"Current theme: {theme} has an invalid file type: "
                    f"{self.theme[1]}!"))

        if isinstance(theme, str):
            if isinstance(widget, (list, tuple, set)):
                for w in widget:
                    apply_theme(w, theme)
            else:
                apply_theme(widget, theme)
        else:
            raise TypeError(f"Cannot use: {theme} is considered an invalid type!")

    def load_theme(self):
        for w_id in self.stored_widgets:
            self.set_widget_theme(
                self.stored_widgets[w_id][0],
                self.stored_widgets[w_id][1]
                )

if __name__ == "__main__":
    th = Theme_Manager()
    th.import_theme('/home/hkaar/Desktop/test.qss', 'test')
    print(th.stored_themes)
