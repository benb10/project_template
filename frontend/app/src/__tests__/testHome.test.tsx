import React, { useEffect, useState } from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { http } from 'msw';
import { setupServer } from 'msw/node';
import { beforeAll, afterEach, afterAll, vi, expect, test } from 'vitest';

import Home from "../app/page"

// Mock backend API responses using MSW
const handlers = [
  http.get('http://localhost:8000/hello_world', (req, res, ctx) => {
    return res(
      ctx.status(200),
      ctx.json({ message: 'Hello World' })
    );
  }),

  http.post('http://localhost:8000/add', (req, res, ctx) => {
    const { nums } = req.body as { nums: number[] };
    return res(
      ctx.status(200),
      ctx.json({ result: nums.reduce((acc, num) => acc + num, 0) })
    );
  }),
];

// Set up the mock service worker
const server = setupServer(...handlers);
// Start and stop the mock service worker during tests
beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())


// Test the component
test('renders API data without crashing', async () => {
  render(<Home />);

  await waitFor(() => screen.getByText(/Hello World/));

  expect(screen.getByText(/Hello World/)).toBeInTheDocument();
});
