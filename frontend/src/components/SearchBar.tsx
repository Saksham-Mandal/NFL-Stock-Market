import { useState, useEffect } from "react";
import Button from "../components/Button";
import { suggestPlayers, type Suggestion } from "../util/suggestplayers";

type SearchProps = {
  placeholder?: string;
  onSubmit?: (value: string) => void;
  btnClassName?: string;
};

const SearchBar = ({ placeholder, onSubmit, btnClassName }: SearchProps) => {
  const [value, setValue] = useState("");
  const [results, setResults] = useState<Suggestion[]>([]);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const q = value.trim();

    if (q.length < 2) {
      setResults([]);
      setOpen(false);
      return;
    }

    const timer = window.setTimeout(async () => {
      const suggestions = await suggestPlayers(q);
      setResults(suggestions);
      setOpen(true);
    }, 200);

    return () => window.clearTimeout(timer);
  }, [value]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit?.(value.trim());
  };

  const pickSuggestion = (name: string) => {
    setValue(name);
    setOpen(false);
    setResults([]);
    onSubmit?.(name);
  };

  return (
    <form className="searchbar-form" onSubmit={handleSubmit}>
      <div className="searchbar-input-wrap">
        <input
          id="player-search"
          name="player-search"
          className="searchbar-input"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder={placeholder}
          onFocus={() => results.length > 0 && setOpen(true)}
          onBlur={() => window.setTimeout(() => setOpen(false), 120)}
        />

        {open && results.length > 0 && (
          <div className="searchbar-dropdown">
            {results.map((r, index) => (
              <div
                key={r.id}
                className={`searchbar-dropdown-item ${
                  index !== 0 ? "with-border" : ""
                }`}
                onMouseDown={(e) => {
                  e.preventDefault();
                  pickSuggestion(r.full_name);
                }}
              >
                {r.full_name}
              </div>
            ))}
          </div>
        )}
      </div>

      <Button
        type="submit"
        className={`searchbar-btn ${btnClassName ?? ""}`.trim()}
      >
        Search
      </Button>
    </form>
  );
};

export default SearchBar;
