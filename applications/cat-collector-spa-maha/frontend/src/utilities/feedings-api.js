import sendRequest from "./sendRequest";

export function catFeedings(catId) {
    return sendRequest(`/cats/${catId}/feedings/`)
}

export function create(formData, catId) {
    return sendRequest(`/cats/${catId}/feedings/`, "POST", formData)
}