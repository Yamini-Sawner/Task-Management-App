import { api } from "../api";

function Navbar({ setPage }) {
  const handleLogout = async () => {
    try {
      await api.logout();
    } finally {
      setPage("login");
    }
  };

  return (
    <nav className="navbar">
      <h2>Task Manager</h2>

      <button onClick={handleLogout}>
        Logout
      </button>
    </nav>
  );
}

export default Navbar;