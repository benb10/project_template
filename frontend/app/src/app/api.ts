const BASE_URL = "http://localhost:8000";

// Helper function to make API calls
async function apiCall<T>(
	endpoint: string,
	method: string,
	body?: object,
): Promise<T> {
	const url = `${BASE_URL}${endpoint}`;

	const options: RequestInit = {
		method: method,
		headers: {
			"Content-Type": "application/json",
		},
		body: body ? JSON.stringify(body) : undefined,
	};

	try {
		const response = await fetch(url, options);

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}

		const data: T = await response.json();
		return data;
	} catch (error) {
		console.error("Error during API call:", error);
		throw error;
	}
}

const Api = {
	getHelloWorld: async (): Promise<{ message: string }> => {
		return await apiCall<{ message: string }>("/hello_world", "GET");
	},

	addNumbers: async (nums: number[]): Promise<{ result: number }> => {
		return await apiCall<{ result: number }>("/add", "POST", { nums });
	},
};

export default Api;
