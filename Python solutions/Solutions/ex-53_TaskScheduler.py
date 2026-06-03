class TaskScheduler:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def run_tasks(self):
        while self.tasks:
            task = self.tasks.pop(0)
            print("Executing:", task)
scheduler = TaskScheduler()
scheduler.add_task("Backup Database")
scheduler.add_task("Send Email")
scheduler.add_task("Generate Report")
scheduler.run_tasks()