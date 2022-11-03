import customtkinter
from tkinter import DISABLED, END, NORMAL, Text

from models.Inventory import Inventory
from models.CarStorage import CarStorage
from models.Car import Car
#------------------------------------------------------------------------------------------------------
APPEARANCE_MODE = "System"
DEFAULT_COLOR_THEME = "dark-blue"
DB_FILENAME = "database/database.txt"

customtkinter.set_appearance_mode(APPEARANCE_MODE)  
customtkinter.set_default_color_theme(DEFAULT_COLOR_THEME) 
# --------------------------------------------------------------------------------------------------
class App(customtkinter.CTk):
    WIDTH = 1080
    HEIGHT = 500
    TEXT = ("Roboto Medium", -16)
    
    
    def __init__(self):
        super().__init__()
        
        # ---- General ---
        self.title("Sistema de Gestión de Autos")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing) 

        # ---- Se crean 2 frames ----
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.frame_left = customtkinter.CTkFrame(
            master=self,
            width=180,
            corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ---- Frame left ----
        self.frame_left.grid_rowconfigure(0, minsize=10)   
        self.frame_left.grid_rowconfigure(6, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)   
        self.frame_left.grid_rowconfigure(11, minsize=10)  

        # Frame title -> 'Menu'
        self.title = customtkinter.CTkLabel(
            master=self.frame_left, 
            text="Menu", 
            text_font=App.TEXT
        )
        self.title.grid(row=1, column=0, pady=10, padx=10)


        ### Comando de Botones --------------------------------------------------------------------------------
        
        # Pantalla Inicio (Boton Menu) -----------------------------------------------------------------------
        self.show_car_button = customtkinter.CTkButton(
            master=self.frame_left, 
            text="Inicio", 
            text_font=App.TEXT, 
            command=self.show_car #show car OJOOOOOOOOOOOOOOOOOOOOOOOO
        )
        self.show_car_button.grid(row=2, column=0, pady=10, padx=20)
        
        
        # Agregar -----------------------------------------------------------------------
        self.add_car_button = customtkinter.CTkButton(
            master=self.frame_left, 
            text="Agregar Auto", 
            text_font=App.TEXT, 
            command=self.add_car
        )
        self.add_car_button.grid(row=3, column=0, pady=10, padx=20)
        # Borrar -----------------------------------------------------------------------
        self.borrar_button = customtkinter.CTkButton(
            master=self.frame_left, 
            text="Borrar Auto", 
            text_font=App.TEXT, 
            command=self.remove_car
        )
        self.borrar_button.grid(row=4, column=0, pady=10, padx=20)
        # Editar -----------------------------------------------------------------------
        self.editar_button = customtkinter.CTkButton(
            master=self.frame_left, 
            text="Editar Datos", 
            text_font=App.TEXT, 
            command=self.edit_car
        )
        self.editar_button.grid(row=5, column=0, pady=10, padx=20)
        # Visualización Totales -----------------------------------------------------------------------
        self.reporting_button = customtkinter.CTkButton(
            master=self.frame_left, 
            text="Reporte total", 
            text_font=App.TEXT, 
            command=self.report
        )
        self.reporting_button.grid(row=7, column=0, pady=10, padx=20)


        # Modo -----------------------------------------------------------------------
        self.color_mode_toggle = customtkinter.CTkOptionMenu(
            master=self.frame_left, 
            values=["Light", "Dark", "System"], 
            text_font=App.TEXT, 
            command=self.change_appearance_mode
        )
        self.color_mode_toggle.grid(
            row=10, 
            column=0, 
            pady=10, 
            padx=20, 
            sticky="w"
        )
        # ---- Inventory & Storage ----
        self.__storage = CarStorage(DB_FILENAME)
        self.__inventory = Inventory(self.__storage.read())

    #Visualización de los datos en Pantalla Inicial
        # Create frame
        self.delete_frame = customtkinter.CTkFrame(master=self)                       
        self.delete_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)       
        
        # Display inventory output indexed
        inventory_output = Text(
            self.delete_frame, 
            font=App.TEXT, 
            width=70, 
            height=16, 
            bg='#363636',
            fg='white', 
            spacing3=10
        )
        inventory_output.grid(row=5, column=1, columnspan=2, padx=0, pady=15)
        inventory_output.insert(
            0.0, 
            Inventory.convert_to_literal_indexed(
                self.__inventory.get_vehicles()
            )
        )
        inventory_output.config(state=DISABLED)



### Funciones --------------------------------------------------------------------------------

    ## Función Inicio -------------------------------------------------------------------
    def show_car(self):
        def show_car_action():
            car_id = int(car_id_entry.get())
            customtkinter.CTkLabel(
                master=self.show_frame, 
                text=self.__inventory.show_car(car_id),
                text_font=("Roboto Medium", 12)
            ).grid(column=1, row=15, padx=0, pady=15)

        
        # Crear frame
        self.delete_frame = customtkinter.CTkFrame(master=self)                       
        self.delete_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30) 


        # Create frame
        self.show_frame = customtkinter.CTkFrame(master=self)                       
        self.show_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)       
        
        # Display Autos en inventario
        inventory_output = Text(
            self.show_frame, 
            font=App.TEXT, 
            width=70, 
            height=16, 
            bg='#363636',
            fg='white', 
            spacing3=10
        )
        inventory_output.grid(row=5, column=1, columnspan=2, padx=0, pady=15)
        inventory_output.insert(
            0.0, 
            Inventory.convert_to_literal_indexed(
                self.__inventory.get_vehicles()
            )
        )
        inventory_output.config(state=DISABLED)
        
        
        # Crea Label
        customtkinter.CTkLabel(
            master=self.show_frame, 
            text='Marca auto:', 
            text_font=App.TEXT
        ).grid(
            row=0, 
            column=0, 
            padx=0, 
            pady=15
        )

        # Crea ID entry
        car_id_entry = customtkinter.CTkEntry(
            master=self.show_frame, 
            text_font=App.TEXT
        )
        car_id_entry.grid(
            row=0, 
            column=1, 
            padx=0, 
            pady=15               
        )
        
        # Boton Agregar Auto
        customtkinter.CTkButton(
            master=self.show_car_frame, 
            text="Filtro", 
            command=show_car_action
        ).grid(row=0, column=2, pady=15, padx=0)
    
    
    ## Función Agregar -------------------------------------------------------------------
    def add_car(self):
        def get_label(name):
            return customtkinter.CTkLabel(
                master=self.add_car_frame, 
                text=f'{name}:', 
                text_font=App.TEXT
            )

        def get_entry():
            return customtkinter.CTkEntry(
                master=self.add_car_frame, 
                text_font=App.TEXT
            )

        def add_car_action():
            # Validación: Año y KM deben ser Nros
            if not headers["Año"]["entry"].get().isnumeric():
                customtkinter.CTkLabel(
                    master=self.add_car_frame, 
                    text='Año debe ser un numero',
                    text_font=("Roboto Medium", 12)
                ).grid(column=1, row=15, padx=0, pady=15)
                return
            
            if not headers["km"]["entry"].get().isnumeric():
                customtkinter.CTkLabel(
                    master=self.add_car_frame, 
                    text='km debe ser un numero',
                    text_font=("Roboto Medium", 12)
                ).grid(column=1, row=15, padx=0, pady=15)
                return

            car = Car(
                headers["Marca"]["entry"].get(), 
                headers["Modelo"]["entry"].get(), 
                headers["Color"]["entry"].get(), 
                headers["Año"]["entry"].get(),
                headers["km"]["entry"].get()
            )

            customtkinter.CTkLabel(
                master=self.add_car_frame, 
                text=self.__inventory.add_car(car),
                text_font=("Roboto Medium", 12)
            ).grid(column=1, row=15, padx=0, pady=15)

            del car


        # Se crea el Frame
        self.add_car_frame = customtkinter.CTkFrame(master=self)                        
        self.add_car_frame.grid(
            row=0, 
            column=1, 
            sticky="nswe", 
            padx=30, 
            pady=30
        )      
         
        # Caja contenedora CTK & inputs  
        headers = { 'Marca': {}, 'Modelo': {}, 'Color': {}, 'Año': {}, 'km': {} }
        for row, key in enumerate(headers.keys()):
            headers[key]["label"] = get_label(key)
            headers[key]["label"].grid(
                row=row, 
                column=0, 
                padx=0, 
                pady=15
            )
            headers[key]["entry"] = get_entry()
            headers[key]["entry"].grid(
                row=row, 
                column=1, 
                padx=0, 
                pady=15               
            )

        # Boton Agregar Auto
        customtkinter.CTkButton(
            master=self.add_car_frame, 
            text="Agregar Auto", 
            command=add_car_action
        ).grid(row=6, column=1, pady=15, padx=0)

    ## Función Eliminar -------------------------------------------------------------------
    def remove_car(self):
        def delete_car_action():
            if not car_id_entry.get():
                return
            if not car_id_entry.get().isnumeric():
                customtkinter.CTkLabel(
                    master=self.delete_frame, 
                    text='El ID debe ser un numero',
                    text_font=("Roboto Medium", 12)
                ).grid(column=1, row=15, padx=0, pady=15)
                return

            car_id = int(car_id_entry.get())
            customtkinter.CTkLabel(
                master=self.delete_frame, 
                text=self.__inventory.delete_car(car_id),
                text_font=("Roboto Medium", 12)
            ).grid(column=1, row=15, padx=0, pady=15)

        # Crear frame
        self.delete_frame = customtkinter.CTkFrame(master=self)                       
        self.delete_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)       
        
        # Display Autos en inventario
        inventory_output = Text(
            self.delete_frame, 
            font=App.TEXT, 
            width=70, 
            height=16, 
            bg='#363636',
            fg='white', 
            spacing3=10
        )
        inventory_output.grid(row=5, column=1, columnspan=2, padx=0, pady=15)
        inventory_output.insert(
            0.0, 
            Inventory.convert_to_literal_indexed(
                self.__inventory.get_vehicles()
            )
        )
        inventory_output.config(state=DISABLED)

        # Crea Label
        customtkinter.CTkLabel(
            master=self.delete_frame, 
            text='ID auto:', 
            text_font=App.TEXT
        ).grid(
            row=0, 
            column=0, 
            padx=0, 
            pady=15
        )

        # Crea ID entry
        car_id_entry = customtkinter.CTkEntry(
            master=self.delete_frame, 
            text_font=App.TEXT
        )
        car_id_entry.grid(
            row=0, 
            column=1, 
            padx=0, 
            pady=15               
        )

        # Boton Borrar Auto
        customtkinter.CTkButton(
            master=self.delete_frame, 
            text="Borrar Auto", 
            command=delete_car_action
        ).grid(row=0, column=2, pady=15, padx=0)

    ## Función Editar ---------------------------------------------------------------------
    def edit_car(self):

        def edit_car_action():

            brand_id = int((car_drop_menu.get()).split(". ")[0])

            if feature_drop_menu.get() == "Marca":
                cars[brand_id].brand = value_input.get()

            elif feature_drop_menu.get() == "Modelo":
                cars[brand_id].model = value_input.get()

            elif feature_drop_menu.get() == "Color":
                cars[brand_id].color = value_input.get()           

            elif feature_drop_menu.get() == "Año":
                cars[brand_id].year = value_input.get()

            customtkinter.CTkLabel(
                master=self.edit_frame, 
                text="Auto modificado",
                text_font=("Roboto Medium", 12)
            ).grid(column=1, row=15, padx=0, pady=15)


        # Crea Frame
        self.edit_frame = customtkinter.CTkFrame(master=self)                       
        self.edit_frame.grid(
            row=0, 
            column=1, 
            sticky="nswe", 
            padx=30, 
            pady=30
        )       
        # Get cars
        cars = self.__inventory.get_vehicles()
        if not cars:
            customtkinter.CTkLabel(
                master=self.edit_frame, 
                text="No hay autos",
                text_font=("Roboto Medium", 12)
            ).grid(column=1, row=15, padx=0, pady=15)
            return

        # Seleccionar Auto a Editar
        car_drop_menu = (
            customtkinter.CTkOptionMenu(
                master=self.edit_frame, 
                values=[ 
                    f"{index}. {car.brand}" 
                    for index, car in enumerate(cars) 
                ], 
                text_font=App.TEXT
            )
        )
        car_drop_menu.grid(
            row=1, 
            column=1, 
            padx=0, 
            pady=15
        )

        # Elección del feature a editar
        feature_drop_menu = (
            customtkinter.CTkOptionMenu(
                master=self.edit_frame, 
                values=['Marca', 'Modelo', 'Color', 'Año'], 
                text_font=App.TEXT
            )
        )
        feature_drop_menu.grid(
            row=2,
            column=1, 
            padx=0, 
            pady=15
        )
           
        # Input nuevo valor
        value_input = (
            customtkinter.CTkEntry(
                master=self.edit_frame, 
                text_font=App.TEXT, 
                placeholder_text="Valor"
            )
        )
        value_input.grid(row=3, column=1, padx=0, pady=15)  

        # Boton para editar
        self.edit_car_button = customtkinter.CTkButton(
            master=self.edit_frame, 
            text="Editar", 
            command=edit_car_action
        )
        self.edit_car_button.grid(row=5, column=1, pady=15, padx=0)

    ## Función Reporte ---------------------------------------------------------------------
    def report(self):
        # Frame
        self.report_frame = customtkinter.CTkFrame(master=self)                       
        self.report_frame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)       
        
        # Llamamos a la función get_vehicles
        cars = self.__inventory.get_vehicles()
        total_cars = len(cars)

        # Muestra Datos 
        inventory_output = Text(
            self.report_frame, 
            font=App.TEXT, 
            width=70, 
            height=16, 
            bg='#363636',
            fg='white', 
            spacing3=10
        )
        inventory_output.grid(row=5, column=1, columnspan=2, padx=0, pady=15)
        inventory_output.insert(
            0.0, 
            Inventory.convert_to_literal(
                self.__inventory.get_vehicles()
            )
        )
        inventory_output.config(state=DISABLED)

        customtkinter.CTkLabel(
            master=self.report_frame, 
            text=f'Total de autos: {total_cars}',
            text_font=("Roboto Medium", 12)
        ).grid(column=1, row=15, padx=0, pady=15)

    ## Función Cerrar ---------------------------------------------------------------------
    def on_closing(self, event=0):
        #El programa guardara los datos al cerrarse la ventana.
        car_list = Inventory.convert_to_save_literal(
            self.__inventory.get_vehicles()
        )
        self.__storage.write(car_list)
        self.destroy()

    ## Función Cambiar Modo ---------------------------------------------------------------------
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        
#------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()
