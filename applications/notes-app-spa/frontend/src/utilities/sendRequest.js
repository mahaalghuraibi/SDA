export default async function sendRequest(url, method = "GET") {
  const options = { method };
  try {
    const res = await fetch(`http://localhost:8000${url}`, options);
    if (res.ok) return res.json();
    console.error("Request failed:", res.status, url);
    return [];
  } catch (err) {
    console.error("Network error in send-request:", err);
    return [];
  }
}
