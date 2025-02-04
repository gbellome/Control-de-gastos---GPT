// src/auth/Login.tsx
import React, { useState } from "react";
import { Container, TextField, Typography, Button, Alert } from "@mui/material";
import { useSignInWithGoogle } from "react-firebase-hooks/auth";
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
import { Navigate } from "react-router-dom";
import { useUser } from "../../contexts/UserContext";
import { initializeApp } from "firebase/app";
import { firebaseConfig } from "../../firebase/firebaseConfig";
import styles from './styles/Login.module.scss'

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

const Login: React.FC = () => {
  const user = useUser();
  const [signInWithGoogle] = useSignInWithGoogle(auth);
  const [error, setError] = useState<string | null>(null);

  const handleEmailLogin = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const { email, password } = event.currentTarget
      .elements as typeof event.currentTarget.elements & {
      email: { value: string };
      password: { value: string };
    };
    signInWithEmailAndPassword(auth, email.value, password.value).catch(
      (error) => setError(error.message)
    );
  };

  if (user) {
    return <Navigate to="/dashboard" />;
  }

  return (
    <Container maxWidth="sm" className={styles.Container}>
      <Typography variant="h4" component="h1" gutterBottom>
        Login
      </Typography>
      {error && <Alert severity="error">{error}</Alert>}
      <form onSubmit={handleEmailLogin}>
        <TextField
          label="Email"
          name="email"
          fullWidth
          margin="normal"
          required
        />
        <TextField
          label="Password"
          name="password"
          type="password"
          fullWidth
          margin="normal"
          required
        />
        <Button className={styles.Button} type="submit" variant="contained" color="primary" fullWidth>
          Login
        </Button>
      </form>
      <Button className={styles.Button} 
        variant="contained"
        color="secondary"
        fullWidth
        onClick={() =>
          signInWithGoogle().catch((error) => setError(error.message))
        }
      >
        Login with Google
      </Button>
    </Container>
  );
};

export default Login;
