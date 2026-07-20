import "./App.css";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import NFLStockMarket from "./pages/NFLStockMarket";

function App() {
  return (
    <>
      <title>DarkHorse Sports</title>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate to="/nflstockmarket" />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/nflstockmarket" element={<NFLStockMarket />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
