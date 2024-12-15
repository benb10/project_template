import { render, screen, waitFor } from "@testing-library/react";
import { http, HttpResponse } from "msw";
import { setupServer } from "msw/node";
import React, { useEffect, useState } from "react";
import { afterAll, afterEach, beforeAll, expect, test, vi } from "vitest";

import Home from "../app/page";

const handlers = [
	http.get("http://localhost:8000/hello_world", () => {
		return HttpResponse.json({ message: "Hello World" });
	}),
];

const server = setupServer(...handlers);
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test("renders API data without crashing", async () => {
	render(<Home />);

	await waitFor(() => screen.getByText(/Hello World/));
});

test("test math", async () => {
	expect(2 + 3).toBe(5);
});
