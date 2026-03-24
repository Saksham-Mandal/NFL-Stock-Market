const API_BASE = "http://127.0.0.1:5000";

export async function searchPlayerByName(name: string) {
    const url = `${API_BASE}/api/player?name=${encodeURIComponent(name)}`;
  
    const res = await fetch(url);
  
    if (res.status === 404) {
      return { found: false as const };
    }
  
    const data = await res.json();
    return data;
  }