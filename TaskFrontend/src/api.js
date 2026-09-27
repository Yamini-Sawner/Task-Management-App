
const BASE_URL = import.meta.env.VITE_API_URL;

async function request(path, 
  {
     method = "GET", body 
  } = {}) 
  {
  const res = await fetch(`${BASE_URL}${path}`, {
    method,
    credentials: "include",
    headers: body !== undefined ? { "Content-Type": "application/json" } : {},
    body: body !== undefined ? JSON.stringify(body) : undefined,
  });

  if (res.status === 204) return null;

  const data = await res.json().catch(() => null);

  if (!res.ok) {
    throw new Error((data && data.detail) || `Request failed (${res.status})`);
  }
  return data;
}

export const api = {
  register: (name, email, password) =>
    request("/auth/register", { method: "POST", body: { name, email, password } }),

  login: (email, password) =>
    request("/auth/login",
       { method: "POST", 
        body: 
        { 
          email, password 
        } 
      }),

  logout: () => request("/auth/logout", { method: "POST" }),

  listTasks: () => request("/tasks"),

  createTask: (title, description) =>
    request("/tasks",
       {
         method: "POST", 
         body:
        { 
          title, description 
        }
       }),

  updateTask: (id, updates) =>
    request(`/tasks/${id}`, 
      { 
        method: "PUT", 
        body: updates 
      }),

  completeTask: (id) => request(`/tasks/${id}/complete`, { method: "PATCH" }),

  deleteTask: (id) => request(`/tasks/${id}`, { method: "DELETE" }),
};