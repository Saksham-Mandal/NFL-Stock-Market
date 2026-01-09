PRAGMA foreign_keys = ON;

-- We don't need a separate teams table for the current ingestion pipeline.
-- Store ESPN team id directly on each player row.

CREATE TABLE IF NOT EXISTS players (
    -- ESPN athlete id
    id TEXT PRIMARY KEY,
    
    -- ESPN athlete full name
    full_name TEXT NOT NULL,

    first_name TEXT NOT NULL,

    last_name TEXT NOT NULL,
    
    -- Position abbreviation from ESPN (QB/RB/WR/TE/etc.)
    position TEXT NOT NULL,
    
    -- ESPN team id from the roster URL (e.g., 12)
    team_id INTEGER NOT NULL,
    
    -- Active roster flag (1 = active). Useful when refreshing rosters.
    active INTEGER NOT NULL DEFAULT 1,
    
    -- Common fields present on the roster endpoint for many players
    height_in INTEGER,
    weight_lb INTEGER,
    age INTEGER,
    date_of_birth TEXT,
    
    -- URLs are often present (e.g., headshot or profile link); keep as text
    headshot_url TEXT,
    
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_players_name ON players(full_name);
CREATE INDEX IF NOT EXISTS idx_players_position ON players(position);
CREATE INDEX IF NOT EXISTS idx_players_team ON players(team_id);