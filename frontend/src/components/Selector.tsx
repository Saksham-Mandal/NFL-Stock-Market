import Button from "./Button";

const Selector = () => {
  return (
    <>
      <div className="selection-bar">
        <Button className="selector-button">Dashboard</Button>
        <Button className="selector-button">Stock Market</Button>
        <Button className="selector-button">Weekly Picker</Button>
        <Button className="selector-button">Leaderboard</Button>
        <Button className="selector-button">Leagues</Button>
        <Button className="selector-button">Log Out</Button>
      </div>
    </>
  );
};

export default Selector;
