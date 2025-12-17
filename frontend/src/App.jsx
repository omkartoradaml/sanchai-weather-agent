import { useState } from "react";
import "./App.css";

import { MapContainer, TileLayer } from "react-leaflet";

function getWeatherIcon(condition) {
  if (!condition) return "🌍";
  const text = condition.toLowerCase();

  if (text.includes("clear")) return "☀️";
  if (text.includes("cloud")) return "☁️";
  if (text.includes("rain")) return "🌧";
  if (text.includes("storm")) return "⛈";
  if (text.includes("snow")) return "❄️";

  return "🌍";
}

function App() {
  const [query, setQuery] = useState("");
  const [weather, setWeather] = useState(null);
  const [loading, setLoading] = useState(false);

  const askWeather = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setWeather(null);

    try {
      const res = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      setWeather(data); // ✅ FIX
    } catch {
      setWeather({
        city: "Error",
        weather: {
          temperature: "--",
          condition: "Error",
          description: "Unable to fetch weather",
        },
      });
    }

    setLoading(false);
  };

  return (
    <div className="map-wrapper">
      {/* 🌍 MAP BACKGROUND */}
      <MapContainer
        center={[18.5204, 73.8567]}
        zoom={5}
        scrollWheelZoom={false}
        className="map"
      >
        <TileLayer
          attribution="© OpenStreetMap contributors"
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
      </MapContainer>

      {/* 🧊 GLASS UI */}
      <div className="glass-card">
        <div className="icon">
          {getWeatherIcon(weather?.weather?.condition)}
        </div>

        <h1>Weather Assistant</h1>

        <input
          type="text"
          placeholder="What is the weather in Pune?"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && askWeather()}
        />

        <button onClick={askWeather} disabled={loading}>
          {loading ? "Fetching..." : "Ask"}
        </button>

        {weather && (
          <div className="result">
            <strong>{weather.city}</strong>
            <br />
            🌡 {weather.weather.temperature}°C
            <br />
            ☁ {weather.weather.description}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
