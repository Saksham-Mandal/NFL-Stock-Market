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

  // Helper Functions:
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit?.(value);
  };

  const pickSuggestion = (name: string) => {
    setValue(name);
    setOpen(false);
    setResults([]);
    onSubmit?.(name); // triggers your existing /api/player wiring
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ display: "flex", gap: 10, alignItems: "flex-start" }}
    >
      <div style={{ position: "relative", width: "100%", maxWidth: 520 }}>
        <input
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder={placeholder}
          style={{
            width: "100%",
            padding: "10px 12px",
            borderRadius: 8,
            border: "1px solid #333",
          }}
          onFocus={() => results.length > 0 && setOpen(true)}
          onBlur={() => window.setTimeout(() => setOpen(false), 120)}
        />

        {open && results.length > 0 && (
          <div
            style={{
              position: "absolute",
              top: "calc(100% + 8px)",
              left: 0,
              right: 0,
              border: "1px solid #333",
              borderRadius: 8,
              overflow: "hidden",
              background: "black",
              zIndex: 50,
            }}
          >
            {results.map((r) => (
              <div
                key={r.id}
                onMouseDown={(e) => {
                  e.preventDefault();
                  pickSuggestion(r.full_name);
                }}
                style={{
                  padding: "10px 12px",
                  cursor: "pointer",
                  borderTop: "1px solid #222",
                  color: "white",
                }}
              >
                {r.full_name}
              </div>
            ))}
          </div>
        )}
      </div>

      <Button type="submit" className={btnClassName}>
        Search
      </Button>
    </form>
  );
};

export default SearchBar;
