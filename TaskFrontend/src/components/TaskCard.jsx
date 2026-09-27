function TaskCard({ task, onComplete, onDelete, onEdit }) {
  return (
    <div className={`task-card ${task.completed ? "completed" : ""}`}>
      <div>
        <h3>{task.title}</h3>

        <p>{task.description}</p>

        <p className="task-date">
          Added on: {new Date(task.created_at).toLocaleDateString()}
        </p>

        <span className="status">
          {task.completed ? "Completed" : "Pending"}
        </span>
      </div>

      <div className="task-actions">
        {!task.completed && (
          <button onClick={() => onComplete(task.id)}>
            Complete
          </button>
        )}

        <button onClick={() => onEdit(task)}>
          Edit
        </button>

        <button
          className="delete-button"
          onClick={() => onDelete(task.id)}
        >
          Delete
        </button>
      </div>
    </div>
  );
}

export default TaskCard;