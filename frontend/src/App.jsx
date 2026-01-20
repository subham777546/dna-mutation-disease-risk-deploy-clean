import { Routes, Route } from "react-router-dom";
import Home from "./Home";
import DetailedDescription from "./pages/DetailedDescription";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/details" element={<DetailedDescription />} />
    </Routes>
  );
}

export default App;
