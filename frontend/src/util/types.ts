export type Player = {
    id: string;
    full_name: string;
    first_name?: string;
    last_name?: string;
    position?: string;
    team_id?: number;
    headshot_url?: string;
    active?: number;
    age?: number;
    height_in?: number;
    weight_lb?: number;
    updated_at?: string;
    jersey_number?: number;
    nflverse_player_id?: string
  };

export type Team = {
  full_team_name: string;
  id: number;
  team_abbrev: string;
  team_alt_color?: string;
  team_location: string;
  team_logo?: string;
  team_nickname: string;
  team_prim_color?: string;
  updated_at?: string;
}

export type Suggestion = {
  id: string;
  full_name: string;
};

export type Candle = {
  time: string;
  open: number;
  high: number;
  low: number;
  close: number;
}