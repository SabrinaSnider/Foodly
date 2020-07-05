import axios from 'axios'

export function getAllData() {
  return axios.get('http://localhost:5000/all')
}
