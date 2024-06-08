import nfl_data_py as nfl
import duckdb
from datetime import datetime
import os

YEARS = [2023]
DB_PATH = str(os.path.join(os.getenv("HOME"), ".nfl_data", "data", "fantasy_db.duckdb"))


def fetch_pbp_data(years):
    print(f"> Fetching play by play data for {years} {datetime.now().isoformat()}")
    play_by_play_df = nfl.import_pbp_data(
        years, downcast=True, cache=False, alt_path=None
    )
    print(f"> Retrieved play by play data for {years} {datetime.now().isoformat()}")
    return play_by_play_df


def fetch_player_data():
    print(f"> Fetching player data {datetime.now().isoformat()}")
    player_df = nfl.import_players()
    print(f"> Retrieved player data{datetime.now().isoformat()}")
    return player_df


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
    query = f"CREATE TABLE {table_name} AS SELECT * FROM df;"
    print(query)
    conn.sql(query)


def load_table(conn, table_name):
    query = f"INSERT INTO {table_name} SELECT * FROM df;"
    conn.sql(query)


def main():
    table_name = "play_by_play_2023"
    df = fetch_pbp_data(years=YEARS)
    conn = connect_to_db(file_path=DB_PATH)
    drop_table_if_exists(conn=conn, table_name=table_name)
    create_table(conn=conn, table_name=table_name)
    load_table(conn=conn, table_name=table_name)

    table_name = "player_data"
    df = fetch_player_data()
    conn = connect_to_db(file_path=DB_PATH)
    drop_table_if_exists(conn=conn, table_name=table_name)
    create_table(conn=conn, table_name=table_name)
    load_table(conn=conn, table_name=table_name)


if __name__ == "__main__":
    main()
