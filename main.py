#%%
import nfl_data_py as nfl
import duckdb
from datetime import datetime
import os

YEARS = [2023]
DB_PATH = str(os.path.join(os.getenv("HOME"), ".nfl_data", "data", "fantasy_db.duckdb"))


def connect_to_db(file_path):
    if os.path.exists(str(os.path.join(os.getenv("HOME"), ".nfl_data", "data"))):
        print(f"Found .nfl_data directory")
        return duckdb.connect(file_path)
    else:
        print(f"Creating .nfl_data directory")
        os.mkdir(str(os.path.join(os.getenv("HOME"), ".nfl_data")))
        os.mkdir(str(os.path.join(os.getenv("HOME"), ".nfl_data", "data")))
        return duckdb.connect(file_path)


def drop_table_if_exists(conn, table_name):
    sql = """
        select
            table_name
        from
            information_schema.tables
        group by
            table_name;
    """
    results = [item[0] for item in conn.sql(sql).fetchall()]
    if table_name in results:
        print("Dropping table")
        conn.sql(f"drop table {table_name};")
    else:
        print("Did not find table to drop")


def create_table(conn, table_name):
    query = f"CREATE TABLE {table_name} AS SELECT * FROM data;"
    print(query)
    conn.sql(query)


def fetch_data(name: str, python_callable: callable, kwargs: dict):
    print(f"> Fetching {name} data {datetime.now().isoformat()}")
    data = python_callable(**kwargs)
    print(f"> Retrieved {name} data{datetime.now().isoformat()}")
    return data


def put_data(conn, table_name):
    drop_table_if_exists(conn, table_name)
    create_table(conn, table_name)


def update_table(conn, table_name, python_callable, kwargs={}):
    print("=" * 8, "Updating", table_name, "=" * (40 - len(table_name)))
    data = fetch_data(table_name, python_callable, kwargs)
    put_data(conn, table_name)
    print("")


def main():
    # reusable connection
    conn = connect_to_db(file_path=DB_PATH)
    # Load PBP
    update_table(
        conn,
        "play_by_play_2023",
        nfl.import_pbp_data,
        kwargs={"years": YEARS, "downcast": True, "cache": False, "alt_path": None},
    )
    # Load Player Data
    update_table(conn, "player_data", nfl.import_players)
    # Load Team Data
    update_table(conn, "team_data", nfl.import_team_desc)


if __name__ == "__main__":
    main()
