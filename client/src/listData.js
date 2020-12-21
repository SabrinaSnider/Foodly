import axios from 'axios'

const SERVER_BASE_URL =
  process.env.SERVER_BASE_URL || 'http://localhost:5000';

const axiosConfig = { 
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    "Access-Control-Allow-Methods": "DELETE, POST, GET, OPTIONS"
  }
}

export function getList(listId) {
  return axios.get(`${SERVER_BASE_URL}/lists/${listId}`)
}

export function addProduct(listId, product) {
  return axios.post(
    `${SERVER_BASE_URL}/lists/${listId}/add-product`, 
    {product: product},
    axiosConfig
  );
}

export function deleteProduct(listId, productId) {
  return axios.delete(`${SERVER_BASE_URL}/lists/${listId}/delete-product/${productId}`) 
}

export function toggleProduct(listId, productId) {
  return axios.post(
    `${SERVER_BASE_URL}/lists/${listId}/toggle-product/${productId}`, 
    {},
    axiosConfig
  );
}
