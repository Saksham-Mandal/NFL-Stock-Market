const API_BASE = "http://127.0.0.1:5050";


export async function getChartOHLC(nflverse_id: string){
    try {
        const url = `${API_BASE}/api/stats?nflverse_id=${encodeURIComponent(nflverse_id)}`;
      
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