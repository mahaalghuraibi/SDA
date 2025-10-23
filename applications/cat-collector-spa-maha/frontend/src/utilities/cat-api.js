import sendRequest from "./sendRequest"
const baseURL = "/cats/"

export async function index() {
    return sendRequest(baseURL);
}

export async function detail(id) {
    return sendRequest(`${baseURL}${id}/`);
}

export function show(catId) {
    return sendRequest(`${baseURL}${catId}/`);
}

export async function create(formData) {
    return sendRequest(baseURL, "POST", formData);
}

export async function update(formData, catId) {
    return sendRequest(`${baseURL}${catId}/`, "PUT", formData);
}

export async function deleteCat(catId) {
    return sendRequest(`${baseURL}${catId}/`, "DELETE");
}

export function addPhoto(catId, formData) {
    return sendRequest(`${baseURL}${catId}/add-photo/`, "POST", formData);
}

export function addToyToCat(catId, toyId) {
    return sendRequest(`${baseURL}${catId}/associate-toy/${toyId}/`, "POST");
}

export function removeToyFromCat(catId, toyId) {
    return sendRequest(`${baseURL}${catId}/remove-toy/${toyId}/`, "POST");
}
