# modules/machine_tasks.py

class MachineTask:
    def __init__(self, task_id, machine_id, task_description, start_time, end_time=None, status="Pending"):
        self.task_id = task_id
        self.machine_id = machine_id
        self.task_description = task_description
        self.start_time = start_time
        self.end_time = end_time
        self.status = status  # "Pending", "Running", "Completed"

    def update_status(self, new_status):
        if new_status in ["Pending", "Running", "Completed"]:
            self.status = new_status
            return True
        return False

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_details(self):
        return {
            "Task ID": self.task_id,
            "Machine ID": self.machine_id,
            "Description": self.task_description,
            "Start Time": self.start_time,
            "End Time": self.end_time,
            "Status": self.status
        }


class MachineTaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: MachineTask):
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

    def set_task_end_time(self, task_id, end_time):
        task = self.get_task_by_id(task_id)
        if task:
            task.set_end_time(end_time)
            return True
        return False

    def list_all_tasks(self):
        return [task.get_details() for task in self.tasks]

    def list_tasks_by_status(self, status):
        return [task.get_details() for task in self.tasks if task.status == status]
