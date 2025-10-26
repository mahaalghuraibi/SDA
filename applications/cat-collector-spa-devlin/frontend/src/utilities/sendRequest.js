export default async function sendRequest(url, method = 'GET', payload) {
	const token = localStorage.getItem('accessToken');

	const options = { method };

	if (payload) {
		options.headers = { 'Content-Type': 'application/json' };
		options.body = JSON.stringify(payload);
	}

    if (token) {
        options.headers = options.headers || {};
        options.headers.Authorization = `Bearer ${token}`;
    }

	try {
		const res = await fetch(`http://localhost:8000${url}`, options);
		if (res.ok) return res.json();
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}