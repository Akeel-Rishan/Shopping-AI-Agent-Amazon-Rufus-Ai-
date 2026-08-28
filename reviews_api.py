"""
Reviews API — reads from the `reviews` table in store.db and returns
aggregated rating information for products.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "store.db")