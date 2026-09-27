import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import TaskForm from "../components/TaskForm";
import TaskCard from "../components/TaskCard";
import { api } from "../api";

function Dashboard({ setPage }) {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadTasks();
  }, []);

  const loadTasks = async () => {
    setLoading(true);
    setError("");

    try {
      const data = await api.listTasks();
      setTasks(data);
    } catch (err) {
      // Not logged in / session expired -> send back to login
      setError(err.message);
      setPage("login");
    } finally {
      setLoading(false);
    }
  };

  const addTask = async (newTask) => {
    try {
      await api.createTask(newTask.title, newTask.description);
      loadTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  const completeTask = async (id) => {
    try {
      await api.completeTask(id);
      loadTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  const deleteTask = async (id) => {
    try {
      await api.deleteTask(id);
      loadTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  const editTask = async (task) => {
    const updatedTitle = prompt(
      "Enter new title",
      task.title
    );

    if (!updatedTitle) {
      return;
    }

    try {
      await api.updateTask(task.id, { title: updatedTitle });
      loadTasks();
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <Navbar setPage={setPage} />

      <main className="dashboard">
        <div className="dashboard-header">
          <div>
            <h1>My Tasks</h1>
            <p>Manage your daily tasks</p>
          </div>
        </div>

        <TaskForm onAddTask={addTask} />

        {error && <p className="error">{error}</p>}

        <div className="task-list">
          {loading ? (
            <p>Loading tasks...</p>
          ) : tasks.length === 0 ? (
            <p>No tasks available.</p>
          ) : (
            tasks.map((task) => (
              <TaskCard
                key={task.id}
                task={task}
                onComplete={completeTask}
                onDelete={deleteTask}
                onEdit={editTask}
              />
            ))
          )}
        </div>
      </main>
    </div>
  );
}

export default Dashboard;