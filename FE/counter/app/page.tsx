"use client";
import { useState } from "react";

export default function Home() {
  const [count, setCount] = useState(0);
  // return <h1>Hello World</h1>
  return (
    <div>
      <h1>Counter</h1>
      <p>Count: {count}</p>
      <button 
        onClick={() => setCount((c) => c + 1)}
        className="px-4 py-2 bg-blue-500 text-white rounded"
      >
        +1
      </button>
    </div>
  )
}