const taskForm = document.getElementById('task-form');
const taskList = document.getElementById('task-list');

function loadTasks() {
  fetch('/api/tasks')
    .then(res => res.json())
    .then(tasks => {
      taskList.innerHTML = '';
      tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task[1];
        li.onclick = () => deleteTask(task[0]);
        taskList.appendChild(li);
      });
    });
}

function deleteTask(id) {
  fetch('/api/tasks/' + id, { method: 'DELETE' })
    .then(() => loadTasks());
}

taskForm.addEventListener('submit', e => {
  e.preventDefault();
  const task = document.getElementById('task-input').value;
  fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task })
  }).then(() => {
    document.getElementById('task-input').value = '';
    loadTasks();
  });
});

loadTasks();