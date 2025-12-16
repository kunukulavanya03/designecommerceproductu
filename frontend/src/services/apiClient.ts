// Auto-generated simple API client to reach the backend
const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

async function apiRequest(method, path, data) {
  const url = `${API_BASE}${path}`;
  const opts = {
    method,
    headers: {
      'Content-Type': 'application/json'
    }
  };
  if (data) {
    opts.body = JSON.stringify(data);
  }
  const res = await fetch(url, opts);
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Request failed ${res.status}: ${text}`);
  }
  try {
    return await res.json();
  } catch {
    return await res.text();
  }
}

// Known endpoints derived from the project spec
export const endpoints = {
  "/api/register": {
    "method": "POST",
    "path": "/api/register"
  },
  "/api/login": {
    "method": "POST",
    "path": "/api/login"
  },
  "/api/products": {
    "method": "GET",
    "path": "/api/products"
  },
  "/api/admin/products": {
    "method": "POST",
    "path": "/api/admin/products"
  },
  "/api/admin/products/{product_id}": {
    "method": "DELETE",
    "path": "/api/admin/products/{product_id}"
  }
};

export function buildUrl(path) {
  return `${API_BASE}${path}`;
}

export async function callEndpoint(name, payload) {
  const ep = endpoints[name];
  if (!ep) {
    throw new Error(`Unknown endpoint: ${name}`);
  }
  return apiRequest(ep.method || 'GET', ep.path || '/', payload);
}

export { apiRequest };
