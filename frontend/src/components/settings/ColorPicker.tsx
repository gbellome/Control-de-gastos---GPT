// src/components/settings/ColorPicker.tsx
import React, { useState } from "react";
import { Container, Typography, Button, Grid } from "@mui/material";
import { SketchPicker } from "react-color";

interface ColorPickerProps {
  onSave: (colors: { primary: string; secondary: string }) => void;
}

const ColorPicker: React.FC<ColorPickerProps> = ({ onSave }) => {
  const [primaryColor, setPrimaryColor] = useState<string>("#1976d2");
  const [secondaryColor, setSecondaryColor] = useState<string>("#dc004e");

  const handleSave = () => {
    onSave({ primary: primaryColor, secondary: secondaryColor });
  };

  return (
    <Container>
      <Typography variant="h4" component="h1" gutterBottom>
        Personalizar Colores
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Typography variant="h6">Color Principal</Typography>
          <SketchPicker
            color={primaryColor}
            onChangeComplete={(color) => setPrimaryColor(color.hex)}
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <Typography variant="h6">Color Secundario</Typography>
          <SketchPicker
            color={secondaryColor}
            onChangeComplete={(color) => setSecondaryColor(color.hex)}
          />
        </Grid>
      </Grid>
      <Button variant="contained" color="primary" onClick={handleSave}>
        Guardar Colores
      </Button>
    </Container>
  );
};

export default ColorPicker;
