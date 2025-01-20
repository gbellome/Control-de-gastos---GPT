// src/components/dashboard/Dashboard.tsx
import React from 'react';
import { Container, Grid, Paper, Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, BarChart, Bar } from 'recharts';
import Transactions from '../transactions/Transactions';

const data = [
  { name: 'Enero', Food: 400, Rent: 240, Utilities: 240 },
  { name: 'Febrero', Food: 300, Rent: 139, Utilities: 221 },
  { name: 'Marzo', Food: 200, Rent: 980, Utilities: 229 },
  { name: 'Abril', Food: 278, Rent: 390, Utilities: 200 },
  { name: 'Mayo', Food: 189, Rent: 480, Utilities: 218 },
  { name: 'Junio', Food: 239, Rent: 380, Utilities: 250 },
  { name: 'Julio', Food: 349, Rent: 430, Utilities: 210 },
];

const Dashboard: React.FC = () => {
  return (
    <Container maxWidth="lg">
      <Typography variant="h4" component="h1" gutterBottom>
        Dashboard
      </Typography>
      <Grid container spacing={3}>
        {/* Primera Fila */}
        <Grid item xs={12} md={3}>
          <Paper>
            <Typography variant="h6" component="h2">
              Gasto Total Mensual
            </Typography>
            <Typography variant="h4">$2000</Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} md={3}>
          <Paper>
            <Typography variant="h6" component="h2">
              Objetivos Alcanzados
            </Typography>
            <Typography variant="h4">5</Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} md={3}>
          <Paper>
            <Typography variant="h6" component="h2">
              Objetivos Superados
            </Typography>
            <Typography variant="h4">2</Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} md={3}>
          <Paper>
            <Typography variant="h6" component="h2">
              Objetivos Acumulados
            </Typography>
            <Typography variant="h4">7</Typography>
          </Paper>
        </Grid>

        {/* Segunda Fila */}
        <Grid item xs={12} md={6}>
          <Paper>
            <Typography variant="h6" component="h2">
              Gastos por Categoría
            </Typography>
            <LineChart
              width={500}
              height={300}
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
          </Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper>
            <Typography variant="h6" component="h2">
              Cumplimiento de Objetivos por Mes
            </Typography>
            <BarChart
              width={500}
              height={300}
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
              <Bar dataKey="Food" fill="#8884d8" />
              <Bar dataKey="Rent" fill="#82ca9d" />
              <Bar dataKey="Utilities" fill="#ffc658" />
            </BarChart>
          </Paper>
        </Grid>

        {/* Tercera Fila */}
        <Grid item xs={12}>
          <Paper>
            <Typography variant="h6" component="h2">
              Transacciones
            </Typography>
            <Transactions />
          </Paper>
        </Grid>

        {/* Enlaces a Nuevas Páginas */}
        <Grid item xs={12}>
          <Button variant="contained" color="primary" component={Link} to="/expense-prediction">
            Predicción de Gastos
          </Button>
          <Button variant="contained" color="secondary" component={Link} to="/trend-analysis">
            Análisis de Tendencias
          </Button>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;