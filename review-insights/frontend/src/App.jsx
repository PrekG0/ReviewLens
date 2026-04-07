import { useState } from "react";

export default function App() {
  const [data, setData] = useState(null);

  async function analyze() {
    const res = await fetch(
      "http://127.0.0.1:8000/analyze?product=iphone_17"
    );
    const result = await res.json();
    setData(result);
  }

  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif" }}>
      <h1>ReviewLens</h1>

      <button onClick={analyze}>Analyze</button>

      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
}