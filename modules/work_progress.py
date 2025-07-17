# modules/work_progress.py

class WorkProgress:
    def __init__(self, task_id, product_name, quantity, assigned_workers, machine_id, status="Pending"):
        self.task_id = task_id
        self.product_name = product_name
        self.quantity = quantity
        self.assigned_workers = assigned_workers  # List of worker names or IDs
        self.machine_id = machine_id
        self.status = status  # e.g., "Pending", "In Progress", "Completed"

    def update_status(self, new_status):
        if new_status in ["Pending", "In Progress", "Completed"]:
            self.status = new_status
            return True
        return False

    def get_details(self):
        return {
            "Task ID": self.task_id,
            "Product": self.product_name,
            "Quantity": self.quantity,
            "Workers": self.assigned_workers,
            "Machine ID": self.machine_id,
            "Status": self.status
        }


class WorkProgressManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: WorkProgress):
        self.tasks.append(task)

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task_status(self, task_id, new_status):
        task = self.get_task_by_id(task_id)
        if task:
            return task.update_status(new_status)
        return False

    def list_all_tasks(self):
        return [task.get_details() for task in self.tasks]

    def list_tasks_by_status(self, status):
        return [task.get_details() for task in self.tasks if task.status == status]
