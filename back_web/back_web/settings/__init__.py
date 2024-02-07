import os 
from .base import *

# development/test server
if os.environ.get('mode') == 'dev':
    from .dev import *
# production server
elif os.environ.get('mode') == 'prod':
    from .prod import *
# local testing
else:
    from .local import *