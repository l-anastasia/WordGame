import sqlite3

class DBHandler:
    def __init__(self, db_name) -> None:
        self.conn = sqlite3.connect(db_name)


    def add_player(self, player_id):
        self.conn.cursor.execute("""
        INSERT INTO Player (id)
        VALUES (?) """, (player_id, ))
        self.conn.commit()
        info = self.conn.cursor.rowcount
        self.conn.cursor.close()
        return info

    def add_game(self, player_id, game):
        self.conn.cursor.execute("""
        INSERT INTO Games (game, player_id)
        VALUES (?, ?)""", (game, player_id))

        self.conn.commit()
        info = self.conn.cursor.rowcount
        self.conn.cursor.close()
        return info

    def update_game(self, user_id, game):
        self.conn.cursor.execute("""
        UPDATE Games (game)
        SET (?) WHERE player_id = user_id""", (game, ))

        self.conn.commit()
        info = self.conn.cursor.rowcount
        self.conn.cursor.close()
        return info

    def finish_game(self, user_id, game):
        self.conn.cursor.execute("""
        UPDATE Games (game)
        SET (?) WHERE player_id = user_id""", (game, ))

        self.conn.commit()
        info = self.conn.cursor.rowcount
        self.conn.cursor.close()
        return info

    def get_game(self, user_id):
        self.conn.cursor.execute("""
        SELECT (game) FROM Games
        WHERE player_id = user_id""")

        result = self.conn.cursor.fetchone()
        self.conn.cursor.close()
        return result
