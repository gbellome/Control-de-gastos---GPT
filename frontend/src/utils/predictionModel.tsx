// src/utils/predictionModel.ts
import * as tf from "@tensorflow/tfjs";

interface DataPoint {
  month: number;
  amount: number;
}

/**
 * trainModel - Entrena un modelo de TensorFlow.js con los datos proporcionados.
 * @param {DataPoint[]} data - Array de puntos de datos con mes y monto.
 * @returns {Promise<tf.LayersModel>} - Promesa que resuelve con el modelo entrenado.
 */
export const trainModel = async (
  data: DataPoint[]
): Promise<tf.LayersModel> => {
  const model = tf.sequential();
  model.add(tf.layers.dense({ units: 1, inputShape: [1] }));
  model.compile({ loss: "meanSquaredError", optimizer: "sgd" });

  const xs = tf.tensor2d(
    data.map((d) => d.month),
    [data.length, 1]
  );
  const ys = tf.tensor2d(
    data.map((d) => d.amount),
    [data.length, 1]
  );

  await model.fit(xs, ys, { epochs: 500 });

  return model;
};

/**
 * predict - Realiza una predicción utilizando el modelo entrenado.
 * @param {tf.LayersModel} model - El modelo entrenado de TensorFlow.js.
 * @param {number} month - El mes para el cual se desea predecir el monto.
 * @returns {number} - El monto predicho.
 */
export const predict = (model: tf.LayersModel, month: number): number => {
  const input = tf.tensor2d([month], [1, 1]);
  const prediction = model.predict(input) as tf.Tensor;
  return prediction.dataSync()[0];
};
