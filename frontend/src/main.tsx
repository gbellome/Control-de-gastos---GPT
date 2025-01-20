// src/index.tsx
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import dotenv from 'dotenv';

dotenv.config()

// Renderiza el componente principal de la aplicación en el elemento con id 'root'
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
