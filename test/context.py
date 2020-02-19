# -*- coding: utf-8 -*-
import sys
import os


cwd = os.path.dirname(__file__)
parent = os.path.join(cwd, '..')
abs_parent = os.path.abspath(parent)
app = os.path.join(cwd, '..\\app')
abs_app = os.path.abspath(app)

print(f'''cwd={cwd}
    parent={parent}
    abs_parent={abs_parent}
    app_folder={app}
    abs_app_folder={abs_app}''')

sys.path.insert(0, abs_parent)
sys.path.insert(1, abs_app)
