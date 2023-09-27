import laspy
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar, Frame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

las_file_path = "2743_1234.las"

# Gauname informaciją apie LAS failą
with laspy.open(las_file_path, mode="r") as lasfile:
    all_points = lasfile.read()
    total_points = len(all_points)
    x_min, x_max = all_points['X'].min(), all_points['X'].max()
    y_min, y_max = all_points['Y'].min(), all_points['Y'].max()
    z_min, z_max = all_points['Z'].min(), all_points['Z'].max()


def plot_filtered_points():
    x_center = float(x_var.get())
    y_center = float(y_var.get())
    range_val = float(range_var.get())

    x_min_range = x_center - range_val
    x_max_range = x_center + range_val
    y_min_range = y_center - range_val
    y_max_range = y_center + range_val

    mask = (all_points['X'] >= x_min_range) & (all_points['X'] <= x_max_range) & (all_points['Y'] >= y_min_range) & (
                all_points['Y'] <= y_max_range)

    x = all_points['X'][mask]
    y = all_points['Y'][mask]
    z = all_points['Z'][mask]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(x, y, z, c=z, cmap='viridis', s=1)

    ax.set_xlabel('X koordinatė')
    ax.set_ylabel('Y koordinatė')
    ax.set_zlabel('Z koordinatė')

    cbar = plt.colorbar(sc)
    cbar.set_label('Z koordinatė')

    plt.title('Filtruoti taškai pagal X, Y reikšmes ir rėžius')
    plt.show()


root = tk.Tk()
root.title("Taškų filtravimas")

# Informacija apie LAS failą
info_frame = Frame(root)
info_frame.pack(pady=10)

Label(info_frame, text=f"Taškų skaičius: {total_points}").grid(row=0, column=0, columnspan=2)
Label(info_frame, text=f"X: ({x_min}, {x_max})").grid(row=1, column=0)
Label(info_frame, text=f"Y: ({y_min}, {y_max})").grid(row=1, column=1)
Label(info_frame, text=f"Z: ({z_min}, {z_max})").grid(row=1, column=2)

# Įvesties laukai
input_frame = Frame(root)
input_frame.pack(pady=10)

Label(input_frame, text="X koordinatė:").grid(row=0, column=0)
x_var = StringVar()
Entry(input_frame, textvariable=x_var).grid(row=0, column=1)

Label(input_frame, text="Y koordinatė:").grid(row=1, column=0)
y_var = StringVar()
Entry(input_frame, textvariable=y_var).grid(row=1, column=1)

Label(input_frame, text="Range:").grid(row=2, column=0)
range_var = StringVar()
Entry(input_frame, textvariable=range_var).grid(row=2, column=1)

Button(root, text="Atvaizduoti taškus", command=plot_filtered_points).pack(pady=10)

root.mainloop()
