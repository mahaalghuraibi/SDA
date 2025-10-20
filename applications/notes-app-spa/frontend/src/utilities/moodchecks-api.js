import sendRequest from "./sendRequest";

export function noteMoodChecks(noteId) {
  return sendRequest(`/notes/${noteId}/moodchecks/`);
}

export function create(formData, noteId) {
  return sendRequest(`/notes/${noteId}/moodchecks/`, "POST", formData);
}
