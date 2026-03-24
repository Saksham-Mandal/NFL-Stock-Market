PRAGMA foreign_keys = ON;

--<-------------NFL Player Table------------->--
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

--<-------------NFL Teams Table------------->--
CREATE TABLE IF NOT EXISTS teams (
    -- ESPN team ID
    id INTEGER PRIMARY KEY,

    -- FULL TEAM NAME
    full_team_name TEXT NOT NULL,

    -- TEAM LOCATION
    team_location TEXT NOT NULL,

    -- TEAM NICKNAME
    team_nickname TEXT NOT NULL,

    -- TEAM ABBREVIATION
    team_abbrev TEXT NOT NULL,

    -- TEAM LOGO
    team_logo TEXT,

    -- PRIMARY COLOR
    team_prim_color TEXT NOT NULL,

    -- ALTERNATE COLOR
    team_alt_color TEXT NOT NULL,

    -- TIMESTAMP
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_teams_abbrev ON teams(team_abbrev);