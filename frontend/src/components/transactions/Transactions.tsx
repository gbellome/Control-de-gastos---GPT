// src/components/transactions/Transactions.tsx
import React from 'react';
import { List, ListItem, ListItemText } from '@mui/material';

const transactions = [
  { id: 1, description: 'Compra en supermercado', amount: 50 },
  { id: 2, description: 'Pago de alquiler', amount: 500 },
  { id: 3, description: 'Factura de electricidad', amount: 75 },
  // Agrega más transacciones según sea necesario
];

const Transactions: React.FC = () => {
  return (
    <List>
      {transactions.map((transaction) => (
        <ListItem key={transaction.id}>
          <ListItemText
            primary={transaction.description}
            secondary={`Monto: $${transaction.amount}`}
          />
        </ListItem>
      ))}
    </List>
  );
};

export default Transactions;