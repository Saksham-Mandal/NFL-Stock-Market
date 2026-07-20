const API_BASE = "http://127.0.0.1:5050";

export async function searchPlayerByName(name: string) {
  try {
    const url = `${API_BASE}/api/player?name=${encodeURIComponent(name)}`;
  
    const res = await fetch(url);
  
    if (res.status === 404) {
      return { found: false as const };
    }

    if (!res.ok) {
      throw new Error(`Request failed with status ${res.status}`);
    }

    return await res.json();
  } catch (err) {
    console.error("Backend request failed:", err);
    throw new Error("Backend unavailable. Try again in a moment.");
  }
  }