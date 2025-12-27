class Timer:
    def __init__(self, label):
        self.label = label
        self.running = False
        self.time = 0

    def start(self):
        self.running = True
        self.time = 0
        self._update()

    def stop(self):
        self.running = False

    def _update(self):
        if not self.running:
            return

        try:
            self.label.configure(text=f"Time: {self.time} sec")
        except:
            return

        self.time += 1
        self.label.after(1000, self._update)
