import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound  # Windows-specific library for sound

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        self.label_time = tk.Label(root, textvariable=self.time_var, font=('Helvetica', 48))
        self.label_time.pack(pady=20)

        self.entry_time = tk.Entry(root, font=('Helvetica', 18))
        self.entry_time.insert(0, "00:00")
        self.entry_time.pack(pady=10)

        self.btn_set_alarm = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.btn_set_alarm.pack(pady=10)

        self.btn_stop_alarm = tk.Button(root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.btn_stop_alarm.pack(pady=10)

        self.alarm_active = False
        self.update_time()
        self.root.after(1000, self.update_time)  # Update time every second

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_var.set(current_time)

        if self.alarm_active:
            self.check_alarm()

        self.root.after(1000, self.update_time)

    def set_alarm(self):
        alarm_time_str = self.entry_time.get()

        try:
            alarm_time = datetime.datetime.strptime(alarm_time_str, '%H:%M')
            current_time = datetime.datetime.now().time()

            if alarm_time.time() > current_time:
                self.alarm_active = True
                self.btn_set_alarm.config(state=tk.DISABLED)
                self.btn_stop_alarm.config(state=tk.NORMAL)
                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_str}")

        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time (HH:MM)")

    def check_alarm(self):
        current_time = datetime.datetime.now().time()
        alarm_time_str = self.entry_time.get()
        alarm_time = datetime.datetime.strptime(alarm_time_str, '%H:%M').time()

        if current_time >= alarm_time:
            self.alarm_active = False
            self.btn_set_alarm.config(state=tk.NORMAL)
            self.btn_stop_alarm.config(state=tk.DISABLED)
            messagebox.showinfo("Alarm", "Time to wake up!")
            winsound.PlaySound(r"C:\Users\Rohan Sharma\OneDrive\Desktop\innovixion internship\alarm_sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    def stop_alarm(self):
        self.alarm_active = False
        self.btn_set_alarm.config(state=tk.NORMAL)
        self.btn_stop_alarm.config(state=tk.DISABLED)
        winsound.PlaySound(None, winsound.SND_ASYNC)  # Stop the alarm sound


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()
