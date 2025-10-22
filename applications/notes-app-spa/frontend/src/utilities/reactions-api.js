import sendRequest from "./sendRequest"; 
const BASE_URL = "/reactions/";

export function index() {
  return sendRequest(BASE_URL);
}

export function show(id) {
  return sendRequest(`${BASE_URL}${id}/`);
}

export function create(formData) {
  return sendRequest(BASE_URL, "POST", formData);
}

export function update(id, formData) {
  return sendRequest(`${BASE_URL}${id}/`, "PUT", formData);
}

export function deleteReaction(id) {
  return sendRequest(`${BASE_URL}${id}/`, "DELETE");
}
