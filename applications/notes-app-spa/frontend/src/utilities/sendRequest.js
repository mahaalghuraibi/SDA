export default async function sendRequest(url, method = "GET", payload) {
  const options = { method };

  if (payload) {
    options.headers = { "Content-Type": "application/json" };
    options.body = JSON.stringify(payload);
  }

  try {
    const res = await fetch(`http://127.0.0.1:8000${url}`, options);
    if (res.ok) return res.json();
    throw new Error(`Request failed with status ${res.status}`);
  } catch (err) {
    console.error("Error in send-request:", err);
    return err;
  }
}
