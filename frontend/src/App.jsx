import { useState } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askWeather = async () => {
    if (!query) return;

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: query,
        }),
      });

      const data = await response.json();
      setAnswer(data.answer);
    } catch (error) {
      setAnswer("Error connecting to backend");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>🌤 Weather Assistant</h1>

      <input
        type="text"
        placeholder="What is the weather in Pune?"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{
          padding: "10px",
          width: "300px",
          marginRight: "10px",
        }}
      />

      <button onClick={askWeather} style={{ padding: "10px" }}>
        Ask
      </button>

      <div style={{ marginTop: "20px" }}>
        {loading && <p>Loading...</p>}
        {answer && <p><strong>{answer}</strong></p>}
      </div>
    </div>
  );
}

export default App;
