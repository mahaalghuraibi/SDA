
export async function sendRequest(url) {
	try {
		const res = await fetch(url);
		if (res.ok) return await res.json();
        else throw new Error("bad request")
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}