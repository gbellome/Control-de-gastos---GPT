// src/index.tsx
import React from "react";
import {createRoot} from "react-dom/client";
import App from "./App";
import dotenv from 'dotenv';

// Inicializo todas las variables de entorno según el entorno iniciado
dotenv.config()

// Renderiza el componente principal de la aplicación en el elemento con id 'root'
const container = document.getElementById('root')

createRoot(container!).render(
<React.StrictMode>
    <App />
  </React.StrictMode>
)