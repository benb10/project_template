export class Api {
  private static BASE_URL = 'http://localhost:8000';

  // Helper function to make API calls
  private static async apiCall<T>(endpoint: string, method: string, body?: object): Promise<T> {
    const url = `${this.BASE_URL}${endpoint}`;

    const options: RequestInit = {
      method: method,
      headers: {
        'Content-Type': 'application/json',
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
      console.error('Error during API call:', error);
      throw error;
    }
  }

  // New method to get a "Hello World" message
  static async getHelloWorld(): Promise<{ message: string }> {
    return await this.apiCall<{ message: string }>('/hello_world', 'GET');
  }

  // New method to add two numbers
  static async addNumbers(nums: number[]): Promise<{ result: number }> {
    return await this.apiCall<{ result: number }>('/add', 'POST', { nums });
  }
}
