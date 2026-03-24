const API_BASE = "http://127.0.0.1:5000";

export type Suggestion = {
  id: string;
  full_name: string;
};

export async function suggestPlayers(q: string): Promise<Suggestion[]> {
  const trimmed = q.trim();
  if (trimmed.length < 2) return [];

  const res = await fetch(
    `${API_BASE}/api/suggest?q=${encodeURIComponent(trimmed)}`
  );

  if (!res.ok) return [];

  const data = await res.json();
  return Array.isArray(data.results) ? data.results : [];
}