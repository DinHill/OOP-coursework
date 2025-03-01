import psycopg2 as pg
import config
import sys

class PostgresDB:
    def __init__(self, conn_string=config.DB_CONN) -> None:
        self.conn_string = conn_string
        self.conn = None
        self.cursor = None
        return

    def connect(self):
        try:
            # Connect to db
            self.conn = pg.connect(self.conn_string)
            # Define the cursor
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"Got exception on DB connection: {e}")
            # Handle the exception appropriately, for example, print an error message
            raise e

    def close(self):
        self.cursor.close()
        self.conn.close()
        return

    def select_all_videos(self):
        self.connect()
        query_string = "SELECT * FROM videos"
        self.cursor.execute(query_string)
        results = self.cursor.fetchall()
        self.close()
        return results

    def select_video(self, id):
        self.connect()
        query_string = "SELECT * FROM videos WHERE id=%s;"
        self.cursor.execute(query_string, (id,))
        results = self.cursor.fetchall()
        self.close()
        return results[0] if results else None

    def select_video_by_name(self, name):
        self.connect()
        query_string = "SELECT * FROM videos WHERE video_name=%s;"
        self.cursor.execute(query_string, (name,))
        results = self.cursor.fetchall()
        self.close()
        return results[0] if results else None
    
    def select_video_by_director(self, director):
        self.connect()
        query_string = "SELECT * FROM videos WHERE director=%s;"
        self.cursor.execute(query_string, (director,))
        results = self.cursor.fetchall()
        self.close()
        return results

    def update_row(self, row_tuple):
        self.connect()
        query_string = f"UPDATE videos \
                        SET video_name = '{row_tuple[1]}', \
                            director = '{row_tuple[2]}', \
                            rate = {row_tuple[3]}, \
                            play_count = {row_tuple[4]}, \
                            file_path = '{row_tuple[5]}' \
                        WHERE id = {row_tuple[0]};"
        self.cursor.execute(query_string)
        self.conn.commit()
        self.close()
        return
