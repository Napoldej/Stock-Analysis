import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib
from tkcalendar import DateEntry
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Stockcontroller import *
matplotlib.use("TkAgg")


class StockUI(tk.Tk):
    def __init__(self,controller: StockController):
        super().__init__()
        self.controller = controller
        self.title("Stock Analysis")
        self.stock = ["NVDA","META","RCL", "BLDR", "UBER", "CCL"
                                     ,"AMD","CCL","PHM", "AAPL", "TSLA"]
        self.price = ["Open","Close","Low","High", "Adj Close", "Volume"]
        self.graph_type = ["line", "hist"]
        self.all_data = self.controller.load_data()
        self.from_date = "2022-01-01"
        self.to_date  = "2023-12-31"
        self.init_component()





    def init_component(self):
        self.init_graph()
        self.selectionFrame = tk.LabelFrame(self, text = "Selection", height = 100, width= 100)
        self.buttonFrame = tk.Frame(self)
        self.selectionFrame.grid(row = 0, column = 1, sticky = "NSEW")
        self.buttonFrame.grid(row = 1, column = 0, sticky = "NSEW")
        for j in range(4):
            self.selectionFrame.columnconfigure(j, weight = 1)
            self.buttonFrame.columnconfigure(j, weight = 1)
        self.buttonFrame.rowconfigure(0,weight = 1)

        for i in range(2):
            self.columnconfigure(i,weight = 1)
        self.init_combobox()
        self.load_combobox()
        self.init_checkbox()
        self.init_button()


    def init_combobox(self):
        self.stock_var = tk.StringVar(value = "Select the stock")
        self.value_var = tk.StringVar(value = "Select the attribute")
        self.graph_var = tk.StringVar(value = "Select the graph")
        self.compare_var = tk.StringVar(value = "Select the compare attribute")

        self.selectStock = ttk.Combobox(self.selectionFrame, textvariable= self.stock_var)
        self.selectValue = ttk.Combobox(self.selectionFrame, textvariable= self.value_var)
        self.selectGraph = ttk.Combobox(self.selectionFrame, textvariable= self.graph_var)
        self.selectcompare = ttk.Combobox(self.selectionFrame, textvariable = self.compare_var)

        self.selectStock.grid(row=0, column=0,padx=5,pady = 5, sticky="NSEW")
        self.selectValue.grid(row=1, column=0, padx= 30, pady =30 , sticky="NSEW")
        self.selectGraph.grid(row=2, column=0, padx =30, pady = 30, sticky= "NSEW")

    def checkbox_handler(self):
        if self.checkbox_var.get():
            self.selectcompare.grid(row = 3, column = 0, padx = 30, pady = 30, sticky = "NSEW")
        else:
            self.selectcompare.grid_remove()


    def init_button(self):
        self.plot = tk.Button(self.selectionFrame, text = "Plot",width = 2,height = 2,command= self.plot_handler)
        self.clear = tk.Button(self.selectionFrame, text = "Reset", command = self.clear_handler)
        self.exit = tk.Button(self.selectionFrame, text  = "Exit", command = self.exit_handler)
        self.time_selection = tk.Button(self.selectionFrame, text = "Time selection", command= self.time_selection_handler)

        self.distribution = tk.Button(self.buttonFrame, text = "Distribution", command= self.show_distribution_page)
        self.descriptive_statistic = tk.Button(self.buttonFrame, text = "Descriptive Statistics",command = self.show_descriptive_page)
        self.dataStory = tk.Button(self.buttonFrame,text = "Data Storytelling", command = self.show_data_storytelling_page)
        self.attributes_rela = tk.Button(self.buttonFrame, text = "Attributes Relationship", command = self.show_attribute_rela)




        self.time_selection.grid(row = 0, column = 1, padx = 5, sticky= "NSEW")

        self.plot.grid(row = 4, column = 0,padx = 5, sticky = "NSEW")
        self.clear.grid(row = 4, column = 1,padx = 5, sticky = "NSEW")
        self.exit.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "NSEW")


        self.distribution.grid(row = 3, column = 0, padx = 5, sticky = "NSEW")
        self.descriptive_statistic.grid(row = 3, column = 1, padx = 5, sticky = "NSEW")
        self.dataStory.grid(row = 3, column = 2, padx = 5, sticky = "NSEW")
        self.attributes_rela.grid(row = 3, column = 3, padx = 5, sticky = "NSEW")


        button_self = [self.distribution, self.descriptive_statistic, self.dataStory, self.attributes_rela]
        for i,j in enumerate(button_self):
            j.grid_rowconfigure(0, weight = 0)
            j.grid_columnconfigure(i, weight = 0)

    def show_distribution_page(self):
        # Hide current frames
        self.selectionFrame.grid_remove()
        self.buttonFrame.grid_remove()

        # Create a new frame for the distribution page
        self.distribution_frame = tk.Frame(self)
        self.distribution_frame.grid(row=0, column=0, sticky="NSEW")

        # Add content to the distribution page
        distribution_label = tk.Label(self.distribution_frame, text="Distribution Page")
        distribution_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a back button to return to the initial page
        self.create_back_button(self.distribution_frame)

    def show_descriptive_page(self):
        num = 1
        num1 = 1
        self.selectionFrame.grid_remove()
        self.buttonFrame.grid_remove()
        self.descriptive_statistic_frame = tk.Frame(self)
        self.descriptive_statistic_frame.grid(row=0,column = 0, sticky = "NSEW")
        if len(self.controller.describe()) == 2:
            self.descrip_frame2 = tk.LabelFrame(self.descriptive_statistic_frame, text = f"Descriptive of {self.value_var.get()} and {self.compare_var.get()}")
            self.descrip_frame2.grid(row = 1,column = 0, sticky = "NSEW")
            self.descriptive_statistic_label2 = tk.Label(self.descriptive_statistic_frame,
                                                        text=f"Descriptive statistic of {self.stock_var.get()} between {self.value_var.get()} and {self.compare_var.get()} from {self.from_date} to {self.to_date}")
            self.descriptive_statistic_label2.grid(row=0, column=0, sticky="NSEW")
            self.describe_value,self.describe_value1= self.controller.describe()
            self.name_var1 = tk.Label(self.descrip_frame2, text= f"{self.value_var.get()}")
            self.name_var1.grid(row = 0, column = 0, sticky = "NSEW")
            for name,value in self.describe_value.items():
                self.describe1 = tk.Label(self.descrip_frame2, text=f"{name}  : {value:.3f}")
                self.describe1.grid(row=num, column=0,sticky="NSEW")
                num += 1
            self.name_var2 = tk.Label(self.descrip_frame2, text = f"{self.compare_var.get()}")
            self.name_var2.grid(row = 0, column = 1, sticky ="NSEW")
            for name,value in self.describe_value1.items():

                self.describe2 = tk.Label(self.descrip_frame2, text = f"{name} : {value:.3f}")
                self.describe2.grid(row = num1, column = 1,sticky = "NSEW")
                num1+=1
            self.descrip_frame2.columnconfigure(0,weight = 1)



        if len(self.controller.describe()) == 8:
            self.descrip_frame1 = tk.LabelFrame(self.descriptive_statistic_frame, text = f"{self.value_var.get()}")
            self.descrip_frame1.grid(row = 1, column = 0, padx =5, pady =5, sticky ="NSEW")
            self.descrip_frame1.columnconfigure(0,weight =1 )
            self.descriptive_statistic_label1 = tk.Label(self.descriptive_statistic_frame,
                                                        text=f"Descriptive statistic of {self.stock_var.get()} from {self.from_date} to {self.to_date}")
            self.descriptive_statistic_label1.grid(row=0, column=0, sticky="NSEW")
            self.describe_value =self.controller.describe()
            for name,value in self.describe_value.items():
                self.describe1 = tk.Label(self.descrip_frame1, text = f"{name}  : {value:.3f}")
                self.describe1.grid(row = num, column = 0,padx = 5,pady = 5, sticky = "NSEW")
                num+=1
        self.create_back_button(self.descriptive_statistic_frame,10,0)
        self.descriptive_statistic_frame.columnconfigure(0, weight=1)


    def show_data_storytelling_page(self):
        self.selectionFrame.grid_remove()
        self.buttonFrame.grid_remove()
        self.data_story_telling_frame = tk.Frame(self)
        self.data_story_telling_frame.grid(row = 0, column = 0, sticky = "NSEW")
        self.data_story_telling_label = tk.Label(self.data_story_telling_frame, text="Data Storytelling Page")
        self.data_story_telling_label.grid(row=0, column=0, sticky="NSEW")

        self.create_back_button(self.data_story_telling_frame)


    def show_attribute_rela(self):
        self.selectionFrame.grid_remove()
        self.buttonFrame.grid_remove()
        self.attributes_rela_frame = tk.Frame(self)

        self.attributes_rela_frame.grid(row = 0, column = 0, sticky = "NSEW")
        self.attributes_rela_label = tk.Label(self.attributes_rela_frame, text="Attributes Relationship Page")
        self.attributes_rela_label.grid(row=0, column=0, sticky="NSEW")

        self.create_back_button(self.attributes_rela_frame)







    def show_initial_page(self,frame):
        frame.grid_remove()
        self.selectionFrame.grid()
        self.buttonFrame.grid()



    def create_back_button(self,frame,row,column):
        back_button = tk.Button(frame, text = "Back", command= lambda :self.show_initial_page(frame))
        back_button.grid(row =row, column  = column, padx = 5, pady = 5, sticky = "NSEW")

    def init_checkbox(self):
        self.checkbox_var = tk.BooleanVar()

        self.compare_mode = tk.Checkbutton(self.selectionFrame, text = "Compare Mode?", variable = self.checkbox_var, command = self.checkbox_handler)

        self.compare_mode.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "NSEW")



    def init_graph(self):
        """Initialize graph"""
        self.fig = Figure(figsize = (4,4))
        self.axes = self.fig.add_subplot()
        self.fig_canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.fig_canvas.get_tk_widget().grid(
            row=0, column=0, sticky="NSWE", padx=10, pady=10)


    def clear_handler(self):
        self.stock_var.set("Select the stock")
        self.value_var.set("Select the attribute")
        self.compare_var.set("Select the compare attribute")
        self.graph_var.set("Select the graph")
        self.selectcompare.grid_remove()
        self.from_date = None
        self.to_date = None
        self.axes.clear()
        self.fig_canvas.draw()
        if self.checkbox_var.get():
            self.checkbox_var.set(False)

    def exit_handler(self):
        self.destroy()


    def plot_handler(self):
        self.axes.clear()
        get_value1 = self.value_var.get()
        get_compare1 = self.compare_var.get()
        all_value = [get_value1]
        get_ticker = self.stock_var.get()
        get_graph = self.graph_var.get()
        if self.checkbox_var.get() == True and self.compare_var.get() != "Select the compare attribute":
            all_value.append(get_compare1)
        self.controller.get_all_data_from_ui(self.all_data, get_ticker, all_value, get_graph,self.from_date,self.to_date,self.axes)
        self.controller.plotting()
        self.fig_canvas.draw()

    def time_selection_handler(self):
        self.time_selection = tk.Toplevel(self)
        self.time_selection.title("Date Selection")
        self.from_label = tk.Label(self.time_selection, text = "From date: yyyy-mm-dd")
        self.to_label = tk.Label(self.time_selection, text = "To date: yyyy-mm-dd")
        self.finish_button = tk.Button(self.time_selection, text = "Finish", command = self.finish_select_date)
        self.from_label.grid(row = 0, column  = 0, padx = 5, pady = 5, sticky = "NSEW")
        self.to_label.grid(row = 1, column = 0, padx = 5 , pady = 5, sticky ="NSEW")
        self.from_date_entry = DateEntry(self.time_selection, date_pattern='yyyy-mm-dd', fg = "Black")
        self.to_date_entry = DateEntry(self.time_selection,date_pattern =  "yyyy-mm-dd")
        self.from_date_entry.grid(row=0, column=1, padx=5, pady=5, sticky = "NSEW")
        self.to_date_entry.grid(row = 1, column = 1, padx = 5, pady =5, sticky = "NSEW")
        self.finish_button.grid(row = 2, column = 1, padx = 5, pady = 5 , sticky = "NSEW")
        for i in range(2):
            self.time_selection.columnconfigure(i, weight = 1)

    def finish_select_date(self):
        if self.from_date_entry.get_date().year > 2023 or self.to_date_entry.get_date().year > 2023:
            messagebox.showerror("Error", "Please enter a year not exceed 2023")
        if self.from_date_entry.get_date().year < 2022 or self.to_date_entry.get_date().year < 2022:
            messagebox.showerror("Error", "Please enter a year not below 2022")
        else:
            self.from_date = self.from_date_entry.get_date()
            self.to_date = self.to_date_entry.get_date()
            self.time_selection.destroy()




    def load_combobox(self):
        self.selectStock["values"] = self.stock
        self.selectcompare["values"] = self.price
        self.selectValue["values"] = self.price
        self.selectGraph["values"] = self.graph_type



    def run(self):
        self.mainloop()
