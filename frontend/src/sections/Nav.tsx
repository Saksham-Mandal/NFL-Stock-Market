import SearchBar from "../components/SearchBar";

type NavProps = {
  onSearch?: (value: string) => void;
};

const Nav = ({ onSearch }: NavProps) => {
  return (
    <>
      <div className="navdiv">
        <h1>NFL Stock Market Simulator</h1>
        <div className="navsearch">
          <SearchBar
            onSubmit={onSearch}
            placeholder="Search NFL Players"
            btnClassName="btn-primary"
          ></SearchBar>
        </div>
      </div>
    </>
  );
};

export default Nav;
