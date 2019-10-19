import axios from 'axios';
//import AuthService from '../auth/AuthService';
const API_URL = 'http://localhost:8000';

export class APIService{
    constructor(){

    }

    /* The other methods go here */
    getClients() {
        const url = `${API_URL}/api/clients/`;
        return axios.get(url).then(response => response.data);
    }
    getClient(pk) {
        const url = `${API_URL}/api/clients/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    getClientsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);

    }
    deleteClient(client){
        const url = `${API_URL}/api/clients/${client.pk}`;
        return axios.delete(url);

    }
    createClient(client){
        const url = `${API_URL}/api/clients/`;
        //const headers = {Authorization: `Bearer ${AuthService.getAuthToken()}`};
        return axios.post(url,client);
    }
    updateClient(client){
        const url = `${API_URL}/api/clients/${client.pk}`;
        //const headers = {Authorization: `Bearer ${AuthService.getAuthToken()}`};
        return axios.put(url,client);
    }
}