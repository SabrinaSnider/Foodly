import axios from 'axios'

const SERVER_BASE_URL =
  process.env.SERVER_BASE_URL || 'http://localhost:5000';

const axiosConfig = { 
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }
}

export function getAllData() {
  return axios.get(`${SERVER_BASE_URL}/publix/all`)
}

export function addItem(product) {
  return axios.post(
    `${SERVER_BASE_URL}/publix/add-item`, 
    {product: product},
    axiosConfig
  );
}

export function removeItem(id) {
  return axios.delete(`${SERVER_BASE_URL}/publix/delete-item/${id}`) 
}

export function toggleItemObtained(id) {
  return axios.post(
    `${SERVER_BASE_URL}/publix/toggle-item-obtained/${id}`, 
    {},
    axiosConfig
  );
}
