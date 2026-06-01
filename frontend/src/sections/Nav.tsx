import SearchBar from "../components/SearchBar";

type NavProps = {
  onSearch?: (player: string) => void;
};

const Nav = ({ onSearch }: NavProps) => {
  return (
    <>
      <div className="navsearch">
        <SearchBar
          onSubmit={onSearch}
          placeholder="Search NFL Players"
          btnClassName="btn-primary"
        ></SearchBar>
      </div>
    </>
  );
};

export default Nav;
