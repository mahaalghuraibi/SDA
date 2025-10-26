import sendRequest from "./sendRequest"
const baseURL = "/cats/"

export async function index(catId) {
    return sendRequest(`${baseURL}${catId}/feedings/`);
}

export async function create(catId, formData) {
    return sendRequest(`${baseURL}${catId}/feedings/`, "POST", formData);
}