import sendRequest from "./sendRequest";
const url = "/users";

export async function signup({ username, email, password }) {
  try {
    const response = await sendRequest(`${url}/signup/`, "POST", { username, email, password });
    localStorage.setItem("token", response.access);
    return response.user;
  } catch (err) {
    localStorage.removeItem("token");
    return null;
  }
}

export async function login({ username, password }) {
  try {
    const response = await sendRequest(`${url}/login/`, "POST", { username, password });
    localStorage.setItem("token", response.access);
    console.log(response, "login check response"); 
    return response.user;
  } catch (err) {
    localStorage.removeItem("token");
    return null;
  }
}

export async function logout() {
  localStorage.removeItem("token");
}

export async function getUser() {
  try {
    const token = localStorage.getItem('token');
    if (token) {
      const response = await sendRequest(`${url}/verify/`);
      localStorage.setItem('token', response.access);
      return response.user;
    }
    return null;
  } catch (err) {
    console.log(err);
    return null;
  }
}
