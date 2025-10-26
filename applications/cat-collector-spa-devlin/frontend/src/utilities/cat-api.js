import sendRequest from "./sendRequest"
const baseURL = "/cats/"

export async function index() {
    return sendRequest(baseURL);
}

export async function detail(id) {
    return sendRequest(`${baseURL}${id}/`);
}

export async function create(formData) {
    return sendRequest(baseURL, "POST", formData);
}

export async function update(formData, catId) {
    return sendRequest(`${baseURL}${catId}/`, "PUT", formData)
}

export async function deleteCat(catId) {
    return sendRequest(`${baseURL}${catId}/`, "DELETE")
}

export async function createPhoto(catId, formData) {
    return sendRequest(`${baseURL}${catId}/add-photo/`, "POST", formData)
}

export async function addToyToCat(catId, toyId) {
    return sendRequest(`${baseURL}${catId}/associate-toy/${toyId}/`, "POST")
}

export async function removeToyToCat(catId, toyId) {
    return sendRequest(`${baseURL}${catId}/remove-toy/${toyId}/`, "POST")
}

