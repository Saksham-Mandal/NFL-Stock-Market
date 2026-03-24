import Nav from "./sections/Nav";
import PlayerHero from "./sections/PlayerHero";
import { useState, useEffect } from "react";
import { searchPlayerByName } from "./util/searchplayer";
import type { Player } from "./util/types";

const Layout = () => {
  const [player, setPlayer] = useState<Player | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    handleSearch("Josh Allen");
  }, []);

  const handleSearch = async (name: string) => {
    const trimmed = name.trim();
    if (!trimmed) return;

    setIsLoading(true);
    setError(null);
    setPlayer(null);

    try {
      const data = await searchPlayerByName(trimmed);

      if (!data.found) {
        setError("Player not found in database.");
        return;
      }

      setPlayer(data.player);
    } catch (e) {
      setError("Failed to reach backend.");
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <>
      <Nav onSearch={handleSearch}></Nav>
      <div className="pageLayout">
        <div className="leftPanel"></div>
        <div className="rightPanel">
          <PlayerHero
            player={player}
            error={error}
            isLoading={isLoading}
          ></PlayerHero>
        </div>
      </div>
    </>
  );
};

export default Layout;
