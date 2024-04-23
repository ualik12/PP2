import psycopg2

def connect_db():
    return psycopg2.connect('snake_game.db')

def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS User_Score (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            speed INTEGER DEFAULT 1,
            walls TEXT DEFAULT '',
            state TEXT DEFAULT '',
            FOREIGN KEY (user_id) REFERENCES User (id)
        )
    ''')

    
def get_or_create_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM User WHERE username = ?', (username,))
    user_id = cursor.fetchone()
    if user_id:
        user_id = user_id[0]
    else:
        cursor.execute('INSERT INTO User (username) VALUES (?)', (username,))
        conn.commit()
        user_id = cursor.lastrowid
        cursor.execute('INSERT INTO User_Score (user_id, score, level, speed, walls) VALUES (?, 0, 1, 1, "")', (user_id,))
        conn.commit()
    conn.close()
    return user_id

def fetch_user_level(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT level FROM User_Score WHERE user_id = ?', (user_id,))
    level = cur.fetchone()[0]
    conn.close()
    return level

def update_game_state(user_id, score, level, speed, walls, state):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE User_Score
        SET score = ?, level = ?, speed = ?, walls = ?, state = ?
        WHERE user_id = ?
    ''', (score, level, speed, walls, state, user_id))
    conn.commit()
    conn.close()

def pause_game(user_id, game_state):
    # game_state should be a dictionary or similar structure that includes score, level, speed, walls, state
    update_game_state(user_id, game_state['score'], game_state['level'], game_state['speed'], game_state['walls'], game_state['state'])
    print("Game paused and state saved.")