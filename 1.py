import tkinter as tk


# Defining a Fuction to calculate gst 
def gst():
    net_price = float(net_price_entry.get())
    orignal_cost = float(orignal_cost_entry.get())
    gst_rate = ((net_price - orignal_cost) * 100) / orignal_cost
    gst_result_label.config(text=f"GST Rate: {gst_rate}%")

# Making a window
window = tk.Tk()

# Making a label to get entry for net price from the user 
net_price_label = tk.Label(text="Enter Net Price", width=40)
net_price_label.pack()

net_price_entry = tk.Entry()
net_price_entry.pack()

#  Making a label to get entry for the orignal cost from the user
orignal_cost_label = tk.Label(text='Original cost', width=40)
orignal_cost_label.pack()

orignal_cost_entry = tk.Entry()
orignal_cost_entry.pack()

#  Creating a button to execute the function to calculate gst
gst_button = tk.Button(text="GST Tax Calculator", command= gst)
gst_button.pack()

# creating a label to display the results 
gst_result_label = tk.Label(window)
gst_result_label.pack()

window.mainloop()