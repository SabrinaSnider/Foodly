import axios from 'axios'

let axiosConfig = { 
  headers: {
    'Content-Type': 'application/json',
    "Access-Control-Allow-Origin": "*",
  }
}

export function getAllData() {
  return axios.get('http://localhost:5000/all')
}

export function addItem(product) {
  return axios.post(
    "http://localhost:5000/add-item", 
    {product: product},
    axiosConfig
  );
}
