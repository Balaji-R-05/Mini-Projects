import tkinter as tk
def bmi_cal(weight, height):
  return weight/(height*height)

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.mainloop()
