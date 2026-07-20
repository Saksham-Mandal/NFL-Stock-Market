import Nav from "./sections/Nav";
import PlayerHero from "./sections/PlayerHero";
import PlayerChart from "./sections/PlayerChart";
import Selector from "./components/Selector";
import Banner from "./components/Banner";
import logo from "./imgs/logo-5.png";
import { useState, useEffect } from "react";
import { searchPlayerByName } from "./util/searchplayer";
import { searchTeamByID } from "./util/getteaminfo";
import { getChartOHLC } from "./util/getcandlechart";
import type { Player, Team, Candle } from "./util/types";

const Layout = () => {
  const [player, setPlayer] = useState<Player | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [team, setTeam] = useState<Team | null>(null);
  const [candles, setCandles] = useState<Candle[]>([]);

  //useEffect(() => {
  //  handlePlayer("Josh Allen");
  //}, []);
  useEffect(() => {
    handleTeam(player?.team_id);
  }, [player]);

  useEffect(() => {
    handleCandles(player?.nflverse_player_id);
  }, [player]);

  const handlePlayer = async (name: string) => {
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

  const handleTeam = async (id: number | undefined) => {
    if (id == null) return;

    setIsLoading(true);
    setError(null);
    setTeam(null);

    try {
      const data = await searchTeamByID(id);

      if (!data.found) {
        //setError("Team not found in database.");
        return;
      }

      setTeam(data.team);
    } catch (e) {
      setError("Failed to reach backend.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleCandles = async (nflverse_id: string | undefined) => {
    if (nflverse_id == null) return;

    setCandles([]); //clearing candles array;
    setIsLoading(true);
    setError(null);

    try {
      console.log("Fetching candles for nflverse_id:", nflverse_id);

      const data = await getChartOHLC(nflverse_id);

      console.log("Raw candle response:", data);
      console.log("Candles from response:", data.candles);

      if (!data.found) {
        //setError("Player stats not found in server")
        return;
      }

      setCandles(data.candles);
    } catch (e) {
      console.error("Candle fetch error:", e);
      setError("Failed to generate chart");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <div className="pageLayout">
        <Banner />
        <div className="selection-container">
          <Selector></Selector>
        </div>
        <div className="search-container">
          <Nav onSearch={handlePlayer}></Nav>
        </div>

        <div className="content-container">
          <div className="leftPanel">
            <PlayerChart candles={candles}></PlayerChart>
          </div>
          <div className="rightPanel">
            <PlayerHero
              player={player}
              error={error}
              isLoading={isLoading}
              team={team}
            ></PlayerHero>
          </div>
        </div>
      </div>
    </>
  );
};

export default Layout;
