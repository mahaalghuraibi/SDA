import { sendRequest } from "./sendRequest";

export async function getTrendingGifs() {
	try {
        const url = `https://api.giphy.com/v1/gifs/trending?api_key=${import.meta.env.VITE_GIPHY_API_KEY}`;
		return sendRequest(url);
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}

export async function searchGifs(searchText) {
	try {
        const url = `https://api.giphy.com/v1/gifs/search?api_key=${import.meta.env.VITE_GIPHY_API_KEY}&q=${searchText}`;
		return sendRequest(url);
	} catch (err) {
		console.log(err, "error in send-request");
		return err;
	}
}