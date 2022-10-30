from tkinter import ttk
import customtkinter
from Autos import Auto
from Autos import Inventario

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    WIDTH = 1080
    HEIGHT = 720
    TEXT = ("Roboto Medium", -16)
    
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestión de Autos: Carlos")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ 2 Frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   
        self.frame_left.grid_rowconfigure(6, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)   
        self.frame_left.grid_rowconfigure(11, minsize=10)  

        self.title = customtkinter.CTkLabel(master=self.frame_left, text="Menu", text_font=App.TEXT)
        self.title.grid(row=1, column=0, pady=10, padx=10)
        
        self.add_car_button = customtkinter.CTkButton(master=self.frame_left, text="Agregar Nuevo Auto", text_font=App.TEXT, command=self.agregar_auto)
        self.add_car_button.grid(row=3, column=0, pady=10, padx=20)

        #self.search_button = customtkinter.CTkButton(master=self.frame_left, text="Buscar", text_font=App.TEXT, command=self.search_car_function)
        #self.search_button.grid(row=4, column=0, pady=10, padx=20)

        #self.payment_button = customtkinter.CTkButton(master=self.frame_left, text="Payments", text_font=App.TEXT, command=self.payment_function)
        #self.payment_button.grid(row=5, column=0, pady=10, padx=20)

        #self.color_mode_title = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:", text_font=App.TEXT)
        #self.color_mode_title.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.color_mode_toggle = customtkinter.CTkOptionMenu(master=self.frame_left, values=["Light", "Dark", "System"], text_font=App.TEXT, command=self.change_appearance_mode)
        self.color_mode_toggle.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============
        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_right ============
        # set default values
        self.color_mode_toggle.set("Dark")
   


    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def agregar_auto(self):
        """ Creates frame for a form containing: Marca, Modelo, Año, KM"""
        def get_items():
            print(f'Car({ctk_items[1][0].get()}, {ctk_items[1][1].get()}, {ctk_items[1][2].get()},  {ctk_items[1][3].get()} {ctk_items[1][4].get()})')
            
            if (ctk_items[1][3].get().isnumeric()) is False:
                self.add_car_error.config(text='Año debe ser un numero', fg='#821515')
                print('Año debe ser un numero')
                return
            
            if (ctk_items[1][4].get().isnumeric()) is False:
                self.add_car_error.config(text='km debe ser un numero', fg='#821515')
                print('km debe ser un numero')
                return
            
            for i in range(5):
                current_Element = ctk_items[1][i].get()
                if current_Element != current_Element.lower():
                    self.add_car_error.config(text='Make entry lowercase', fg='#821515')
                    print('solo letras minusculas')
                    return
            
            self.add_car_error.config(text='Marca, Modelo, Color deben ser en minúscula.\n\nAño y km deben ser numericos.', fg='white')
           
            newCar = Auto(ctk_items[1][0].get(), ctk_items[1][1].get(), ctk_items[1][2].get(), ctk_items[1][3].get())
            newCar.save_to_file()

            ctk_items[1][0].delete(0, customtkinter.END)
            ctk_items[1][1].delete(0, customtkinter.END)
            ctk_items[1][2].delete(0, customtkinter.END)
            ctk_items[1][3].delete(0, customtkinter.END)
            ctk_items[1][4].delete(0, customtkinter.END)
                
        ctk_items = [[],[]]
        items = ('Marca', 'Modelo', 'Color', 'Año', 'km')
                
        self.add_car_frame = customtkinter.CTkFrame(master=self)                        
        self.add_car_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)       
            
        for element in range(5):
            ctk_items[0].append(customtkinter.CTkLabel(master=self.add_car_frame, text=f'{items[element]}:', text_font=App.TEXT))
            ctk_items[0][element].grid(row=element, column=0, padx=0, pady=15)
            
            ctk_items[1].append(customtkinter.CTkEntry(master=self.add_car_frame, text_font=App.TEXT))
            ctk_items[1][element].grid(row=element, column=1, padx=0, pady=15)  
                
        self.output_car_button = customtkinter.CTkButton(master=self.add_car_frame, text="Agregar Auto", command=get_items)
        self.output_car_button.grid(row=4, column=1, pady=15, padx=0)
        
        self.add_car_error = customtkinter.CTkLabel(master=self.add_car_frame, text='Marca, Modelo, Color deben ser en minúscula.\n\nAño y km deben ser numericos.', text_font=("Roboto Medium", 11))
        self.add_car_error.grid(column=1, row=5, padx=0, pady=15)




if __name__ == "__main__":
    app = App()
    app.mainloop()