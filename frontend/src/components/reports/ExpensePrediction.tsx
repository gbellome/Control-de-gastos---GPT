// src/components/reports/ExpensePrediction.tsx
import React, { useState, useEffect } from 'react';
import { Container, Typography, Button, TextField } from '@mui/material';
import * as tf from '@tensorflow/tfjs';
import { trainModel, predict } from '../../utils/predictionModel';

interface DataPoint {
  month: number;
  amount: number;
}

const historicalData: DataPoint[] = [
  { month: 1, amount: 400 },
  { month: 2, amount: 300 },
  { month: 3, amount: 200 },
  { month: 4, amount: 278 },
  { month: 5, amount: 189 },
  { month: 6, amount: 239 },
  { month: 7, amount: 349 },
];

const ExpensePrediction: React.FC = () => {
  const [model, setModel] = useState<tf.LayersModel | null>(null);
  const [month, setMonth] = useState<string>('');
  const [prediction, setPrediction] = useState<number | null>(null);

  useEffect(() => {
    const train = async () => {
      const trainedModel = await trainModel(historicalData);
      setModel(trainedModel);
    };
    train();
  }, []);

  const handlePredict = () => {
    if (model && month) {
      const predictedAmount = predict(model, parseInt(month));
      setPrediction(predictedAmount);
    }
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" component="h1" gutterBottom>
        Predicción de Gastos
      </Typography>
      <TextField
        label="Mes (1-12)"
        value={month}
        onChange={(e) => setMonth(e.target.value)}
        fullWidth
        margin="normal"
      />
      <Button variant="contained" color="primary" onClick={handlePredict}>
        Predecir Gasto
      </Button>
      {prediction !== null && (
        <Typography variant="h6" component="h2">
          Gasto Predicho: ${prediction.toFixed(2)}
        </Typography>
      )}
    </Container>
  );
};

export default ExpensePrediction;