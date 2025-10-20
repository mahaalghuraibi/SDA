import sendRequest from "./sendRequest";
const url = "/notes/";

export async function index() {
  return sendRequest(url);
}
