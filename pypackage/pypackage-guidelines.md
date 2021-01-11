## Pypackage Guidelines
To make a folder into a package   

```
__init__.py (from subfolder example: database)
from .file1 import *
from .file2 import *
```

**When import**
```
import database import *
```

**Rather than**
```
from database.insertion import *
from database.schema import *
```
