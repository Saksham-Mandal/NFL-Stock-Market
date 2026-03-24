import type { Player } from "../util/types";

type PageProps = {
  player: Player | null;
  error: string | null;
  isLoading: boolean;
};

const Page = ({ player, error, isLoading }: PageProps) => {
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
      <div style={{ padding: 24 }}>
        <div style={{ display: "flex", gap: 16, alignItems: "center" }}>
          <img
            src={player.headshot_url}
            alt={player.full_name}
            style={{ width: 96, height: 96, borderRadius: 12 }}
          />

          <div>
            <div style={{ fontSize: 24, fontWeight: 800 }}>
              {player.full_name}
            </div>
            <div style={{ opacity: 0.8 }}>
              {player.position ?? "?"} • Team ID: {player.team_id ?? "?"}
            </div>
          </div>
        </div>

        <div style={{ marginTop: 16, lineHeight: 1.8 }}>
          <div>Age: {player.age ?? "?"}</div>
          <div>Height (in): {player.height_in ?? "?"}</div>
          <div>Weight (lb): {player.weight_lb ?? "?"}</div>
          <div>Active: {player.active === 1 ? "Yes" : "No"}</div>
          <div>Updated: {player.updated_at ?? "?"}</div>
        </div>
      </div>
    </>
  );
};

export default Page;
