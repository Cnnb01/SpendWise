#!/usr/bin/env/ python3

"""For defining table models, and the storage engine"""

import os
from .engine.db import DB

storage = DB()

storage.reload()
