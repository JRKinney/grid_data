import duckdb
from grid_data.config import DATA_DIR

# create a connection to grid_data.db (creates if it doesn't exist)
con = duckdb.connect(DATA_DIR / "grid_data.db")

# explicitly close the connection
con.close()
