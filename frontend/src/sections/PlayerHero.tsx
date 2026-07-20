import type { Player, Team } from "../util/types";

type PageProps = {
  player: Player | null;
  error: string | null;
  isLoading: boolean;
  team: Team | null;
};

const Page = ({ player, error, isLoading, team }: PageProps) => {
  const getPlayerPos = (pos: string | undefined) => {
    if (pos == "QB") {
      return "Quarterback";
    } else if (pos == "WR") {
      return "Wide Receiver";
    } else if (pos == "TE") {
      return "Tight End";
    } else if (pos == "RB") {
      return "Running Back";
    } else {
      return "Position Unavailable";
    }
  };

  const getPlayerHeightFeet = (player: Player) => {
    if (player.height_in == null) {
      return;
    } else {
      var agefeet = Math.floor(player.height_in / 12);
      return agefeet;
    }
  };

  const getPlayerHeightInches = (player: Player) => {
    if (player.height_in == null) {
      return;
    } else {
      var ageinches = player.height_in % 12;
      return ageinches;
    }
  };

  if (isLoading) return <div style={{ padding: 24 }}>Loading...</div>;

  if (error) {
    return <div style={{ padding: 24, color: "crimson" }}>{error}</div>;
  }

  if (!player) {
    return (
      <div style={{ padding: 24, opacity: 0.75 }}>
        Search for a player to see results.
      </div>
    );
  }

  return (
    <>
      <div
        className="playerHero-container"
        style={
          {
            "--team-primary": team?.team_prim_color || "#3b82f6",
            "--team-secondary": team?.team_alt_color || "#fff",
          } as React.CSSProperties
        }
      >
        <div className="playerHero-teamname">
          <div
            className="teamname"
            style={
              {
                "--team-primary": team?.team_prim_color || "#3b82f6",
                "--team-secondary": team?.team_alt_color || "#fff",
              } as React.CSSProperties
            }
          >
            {team?.full_team_name}
          </div>
        </div>
        <div className="playerHero-player">
          <div className="headshot">
            <img
              src={player.headshot_url}
              alt={player.full_name}
              style={{ width: 140, height: 100, borderRadius: 12 }}
            />
          </div>
          <div className="playername">
            <div className="firstname">{player.first_name}</div>
            <div className="lastname">{player.last_name}</div>
          </div>
        </div>
        <div className="playerHero-info">
          <table className="infotable">
            <tbody>
              <tr>
                <td>
                  <div className="infotable-label">Position:</div>
                </td>
                <td>
                  <div className="infotable-info">
                    {getPlayerPos(player.position) ?? "?"}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div className="infotable-label">Age:</div>
                </td>
                <td>
                  <div className="infotable-info">
                    {player.age != null ? `${player.age} yrs` : "?"}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div className="infotable-label">Height: </div>
                </td>
                <td>
                  <div className="infotable-info">
                    {getPlayerHeightFeet(player) != null &&
                    getPlayerHeightInches(player) != null
                      ? `${getPlayerHeightFeet(
                          player
                        )}' ${getPlayerHeightInches(player)}"`
                      : "?"}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div className="infotable-label">Weight:</div>
                </td>
                <td>
                  <div className="infotable-info">
                    {player.weight_lb != null ? `${player.weight_lb} lbs` : "?"}
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
};

export default Page;
