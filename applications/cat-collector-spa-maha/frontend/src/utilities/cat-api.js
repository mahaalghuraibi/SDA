import sendRequest from "./sendRequest";

const baseURL = "/cats/";

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
