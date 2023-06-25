    import calendar
    import tkinter as tk
    from tkinter import messagebox

    def show_calendar():
        year = year_entry.get()
        if year.isdigit():  
            year = int(year)
            if 1900 <= year <= 2100:
                cal = calendar.calendar(year)
                messagebox.showinfo("Calendar", cal)
            else:
                messagebox.showerror("Error", "Please enter a valid year (1900-2100).")
        else:
            messagebox.showerror("Error", "Please enter a valid year.")

    # Create the main window
    window = tk.Tk()
    window.title("Calendar Application")

    # Create label and entry for year input
    year_label = tk.Label(window, text="Enter a year:")
    year_label.pack()
    year_entry = tk.Entry(window)
    year_entry.pack()

    # Create button to display the calendar
    show_button = tk.Button(window, text="Show Calendar", command=show_calendar)
    show_button.pack()

    # Start the main loop
    window.mainloop()





























