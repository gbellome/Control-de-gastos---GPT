// src/components/auth/Enable2FA.tsx
/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { useState } from "react";
import { Container, Button, TextField, Typography, Alert } from "@mui/material";
import { getAuth, PhoneAuthProvider, RecaptchaVerifier } from "firebase/auth";
import { useUser } from "../../contexts/UserContext";

const Enable2FA: React.FC = () => {
  const [phoneNumber, setPhoneNumber] = useState<string>("");
  const [verificationCode, setVerificationCode] = useState<string>("");
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const auth = getAuth();
  const user = useUser();

  const setupRecaptcha = () => {
    window.recaptchaVerifier = new RecaptchaVerifier(
      "recaptcha-container",
      {
        size: "invisible",
        callback: (response: any) => {
          // reCAPTCHA solved, allow signInWithPhoneNumber.
          console.log(response)
        },
      },
      auth
    );
  };

  const sendVerificationCode = () => {
    setupRecaptcha();
    const appVerifier = window.recaptchaVerifier;
    const provider = new PhoneAuthProvider(auth);
    provider
      .verifyPhoneNumber(phoneNumber, appVerifier)
      .then((verificationId) => {
        window.verificationId = verificationId;
        setSuccess("Código de verificación enviado.");
      })
      .catch((error) => setError(error.message));
  };

  const verifyCode = () => {
    const credential = PhoneAuthProvider.credential(
      window.verificationId,
      verificationCode
    );
    user?.multiFactor
      .enroll(credential, "My Phone")
      .then(() => setSuccess("Autenticación en dos factores habilitada."))
      .catch((error: any) => setError(error.message));
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" component="h1" gutterBottom>
        Habilitar Autenticación en Dos Factores
      </Typography>
      {error && <Alert severity="error">{error}</Alert>}
      {success && <Alert severity="success">{success}</Alert>}
      <TextField
        label="Número de Teléfono"
        value={phoneNumber}
        onChange={(e) => setPhoneNumber(e.target.value)}
        fullWidth
        margin="normal"
      />
      <Button
        variant="contained"
        color="primary"
        onClick={sendVerificationCode}
      >
        Enviar Código de Verificación
      </Button>
      <TextField
        label="Código de Verificación"
        value={verificationCode}
        onChange={(e) => setVerificationCode(e.target.value)}
        fullWidth
        margin="normal"
      />
      <Button variant="contained" color="secondary" onClick={verifyCode}>
        Verificar Código
      </Button>
      <div id="recaptcha-container"></div>
    </Container>
  );
};

export default Enable2FA;
