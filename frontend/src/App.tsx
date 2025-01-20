// src/App.tsx
import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import { ThemeProvider, createTheme, Theme } from "@mui/material/styles";
import Login from "./components/auth/Login";
import Dashboard from "./components/dashboard/Dashboard";
import ColorPicker from "./components/settings/ColorPicker";
import ExpensePrediction from "./components/reports/ExpensePrediction";
import TrendAnalysis from "./components/reports/TrendAnalysis";
import { UserProvider, useUser } from "./contexts/UserContext";

const App: React.FC = () => {
  const [theme, setTheme] = useState<Theme>(
    createTheme({
      palette: {
        primary: { main: "#1976d2" },
        secondary: { main: "#dc004e" },
      },
    })
  );

  const handleColorChange = (colors: {
    primary: string;
    secondary: string;
  }) => {
    const newTheme = createTheme({
      palette: {
        primary: { main: colors.primary },
        secondary: { main: colors.secondary },
      },
    });
    setTheme(newTheme);
    localStorage.setItem("theme", JSON.stringify(colors));
  };

  useEffect(() => {
    const savedTheme = JSON.parse(localStorage.getItem("theme") || "{}");
    if (savedTheme.primary && savedTheme.secondary) {
      handleColorChange(savedTheme);
    }
  }, []);

  return (
    <UserProvider>
      <ThemeProvider theme={theme}>
        <Router>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route
              path="/dashboard"
              element={<PrivateRoute component={Dashboard} />}
            />
            <Route
              path="/color-picker"
              element={
                <PrivateRoute>
                  <ColorPicker onSave={handleColorChange} />
                </PrivateRoute>
              }
            />
            <Route
              path="/expense-prediction"
              element={<PrivateRoute component={ExpensePrediction} />}
            />
            <Route
              path="/trend-analysis"
              element={<PrivateRoute component={TrendAnalysis} />}
            />
            <Route path="*" element={<Navigate to="/login" />} />
          </Routes>
        </Router>
      </ThemeProvider>
    </UserProvider>
  );
};

interface PrivateRouteProps {
  component?: React.ComponentType;
  children?: React.ReactNode;
}

const PrivateRoute: React.FC<PrivateRouteProps> = ({
  component: Component,
  children,
}) => {
  const user = useUser();
  if (!user) {
    return <Navigate to="/login" />;
  }
  return Component ? <Component /> : <>{children}</>;
};

export default App;
