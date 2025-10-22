import sendRequest from "./sendRequest";
const url = "/notes/";

export async function index() {
  return sendRequest(url);
}

export async function show(noteId) {
  return sendRequest(`${url}${noteId}/`);
}

export async function create(formData) {
  return sendRequest(url, "POST", formData);
}

export async function update(formData, noteId) {
  return sendRequest(`${url}${noteId}/`, "PUT", formData);
}

export async function deleteNote(noteId) {
  return sendRequest(`${url}${noteId}/`, "DELETE");
}

export function addPhoto(noteId, formData) {
  return sendRequest(`${url}${noteId}/photo/`, "POST", formData);
}

export function addReactionToNote(noteId, reactionId) {
  return sendRequest(`${url}${noteId}/add-reaction/${reactionId}/`, "POST");
}

export function removeReactionFromNote(noteId, reactionId) {
  return sendRequest(`${url}${noteId}/remove-reaction/${reactionId}/`, "POST");
}
