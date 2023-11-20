import tkinter as tk
import time
import threading

class SpeedReaderApp:
    def __init__(self, words, delay=0.1, current_word=0):
        self.words = words
        self.delay = delay
        self.current_word = current_word

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Speed Reader")

        # Create a label to display words
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24), anchor="center")
        self.word_label.pack(expand=True)

        # Start button to begin reading
        self.start_button = tk.Button(self.root, text="Start Reading", command=self.start_reading)
        self.start_button.pack()

        # Stop button to stop reading
        self.stop_button = tk.Button(self.root, text="Stop Reading", command=self.stop_reading)
        self.stop_button.pack()

        # Flag to control the reading loop
        self.reading = False

        # Additional labels for percentage and time remaining
        self.percentage_label = tk.Label(self.root, text="", font=("Helvetica", 12), anchor="w")
        self.percentage_label.pack(side="bottom", anchor="w")
        
        self.time_remaining_label = tk.Label(self.root, text="", font=("Helvetica", 12), anchor="w")
        self.time_remaining_label.pack(side="bottom", anchor="w")

    def update_word(self):
        if self.current_word < len(self.words):
            self.word_label.config(text=self.words[self.current_word])
            
            # Calculate and update percentage
            percentage = (self.current_word / len(self.words)) * 100
            self.percentage_label.config(text=f"{percentage:.2f}% complete")

            # Calculate and update time remaining
            time_remaining = (len(self.words) - self.current_word) * self.delay
            if time_remaining // 360 > 1:
                self.time_remaining_label.config(text=f"Time remaining: {time_remaining//360:.2f} hours")
            elif time_remaining // 60 > 1:
                self.time_remaining_label.config(text=f"Time remaining: {time_remaining//60:.2f} minutes")
            
            self.current_word += 1
        else:
            self.stop_reading()

    def reading_loop(self):
        while self.reading:
            self.update_word()
            time.sleep(self.delay)
            self.root.update()

    def start_reading(self):
        if not self.reading:
            self.reading = True
            threading.Thread(target=self.reading_loop).start()

    def stop_reading(self):
        self.reading = False
        print(self.current_word)

    def run(self):
        self.root.mainloop()