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
  };

export type Team = {
  id: number;
  team_name: string;
  primary_color?: string;
  secondary_color?: string;
}