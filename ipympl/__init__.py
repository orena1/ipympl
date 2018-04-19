import sys
from ._version import version_info, __version__

npm_pkg_name = 'jupyter-matplotlib'

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': npm_pkg_name,
        'require': npm_pkg_name + '/extension'
    }]


# Ensure that `widget` is not selected as the backend name by IPython,
# which causes a UsageError.
if 'IPython' in sys.modules:
    from IPython.core.pylabtools import backend2gui
    backend2gui['module://ipympl.backend_nbagg'] = 'ipympl'

# __init__.py is used by the nbextension installation.
# Conda cannot have dependencies for post-link scripts.
if 'matplotlib' in sys.modules:
    import matplotlib
    matplotlib.use('module://ipympl.backend_nbagg')
