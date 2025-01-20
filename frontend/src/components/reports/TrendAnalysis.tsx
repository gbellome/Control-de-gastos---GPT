// src/components/reports/TrendAnalysis.tsx
import React from 'react';
import { Container, Typography } from '@mui/material';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const data = [
  { name: 'Enero', Food: 400, Rent: 240, Utilities: 240 },
  { name: 'Febrero', Food: 300, Rent: 139, Utilities: 221 },
  { name: 'Marzo', Food: 200, Rent: 980, Utilities: 229 },
  { name: 'Abril', Food: 278, Rent: 390, Utilities: 200 },
  { name: 'Mayo', Food: 189, Rent: 480, Utilities: 218 },
  { name: 'Junio', Food: 239, Rent: 380, Utilities: 250 },
  { name: 'Julio', Food: 349, Rent: 430, Utilities: 210 },
];

const TrendAnalysis: React.FC = () => {
  return (
    <Container maxWidth="lg">
      <Typography variant="h4" component="h1" gutterBottom>
        Análisis de Tendencias
      </Typography>
      <LineChart
        width={800}
        height={400}
        data={data}
        margin={{
          top: 5, right: 30, left: 20, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="Food" stroke="#8884d8" />
        <Line type="monotone" dataKey="Rent" stroke="#82ca9d" />
        <Line type="monotone" dataKey="Utilities" stroke="#ffc658" />
      </LineChart>
    </Container>
  );
};

export default TrendAnalysis;