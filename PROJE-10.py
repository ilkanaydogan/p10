#PROJECT - 10
import customtkinter
import tkinter as tk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox
import random

#////////////////////////////////////////////////////////////////////////////////////////////#

r4 = customtkinter.CTk()
r4.title("RECIPE APP")

r3 = customtkinter.CTk()
r3.title("RECIPE APP")

r2 = customtkinter.CTk()
r2.title("LOGIN")

r1 = customtkinter.CTk()
r1.title("REGISTER")

#////////////////////////////////////////////////////////////////////////////////////////////#

conn = sqlite3.connect("data10.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')

#////////////////////////////////////////////////////////////////////////////////////////////#

def register_to_login_page():
    r1.destroy()
    frame2 = customtkinter.CTkFrame(master=r2,
                                    width=350,
                                    height=350)
    frame2.pack(padx=20,pady=20)

    global username_entry_login
    global password_entry_login

    username_entry_login = customtkinter.CTkEntry(master=frame2,
                                                placeholder_text="Username",
                                                width=150,
                                                height=40)
    username_entry_login.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    password_entry_login = customtkinter.CTkEntry(master=frame2,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
    password_entry_login.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

    verification_button = customtkinter.CTkButton(master=frame2,
                                          text="Verify and Continue!",
                                          command=loginaccount)
    verification_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
    r2.mainloop()

def signup():
    username = username_entry_register.get()
    password = password_entry_register.get()
    if ((username != "") and (password != "")):
        cursor.execute("SELECT username FROM users WHERE username=?", [username])
        if(cursor.fetchone() is not None):
            messagebox.showerror("Error","Username already exists!")
        else:
            encodedpassword = password.encode("utf-8")
            hashedpassword = bcrypt.hashpw(encodedpassword, bcrypt.gensalt())
            print(hashedpassword)
            cursor.execute("INSERT into users VALUES(?, ?)", [username, hashedpassword])
            conn.commit()
            messagebox.showinfo("Sucsess!","Account has been created")
            register_to_login_page_button = customtkinter.CTkButton(master=r1,
                                                                    text="Go to Login Page",
                                                                    command=login,)
            register_to_login_page_button.place(relx=0.5, rely=0.6, anchor = tk.CENTER)
    else:
        messagebox.showerror("Error","Enter all data.")

def loginaccount():
    username = username_entry_login.get()
    password = password_entry_login.get()
    if ((username != "") and (password != "")):
        cursor.execute("SELECT password FROM users WHERE username=?", [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                messagebox.showinfo("Success", f"Logged in successfully, Welcome {username}")
                r2.destroy()
                #////////////////////////////////////////////////////////////////////////////////////////////#
                
                def support_button_function():

                    r3.destroy()

                    def complain_button_function():
                        complain_reason = complain_combobox.get()

                        if not complain_reason:
                            messagebox.showerror("Error", "Please select a complaint!")
                        else:
                            messagebox.showinfo("Success", "Complaint submitted successfully!")

                    def show_complain_details():

                        complain_reason = complain_combobox.get()

                        if not complain_reason:
                            messagebox.showerror("Error", "Please select a complaint!")
                        else:
                            # Sipariş detaylarını ve şikayet nedenini messagebox'ta göster
                            messagebox.showinfo("Complaint Details", f" Complaint Reason: {complain_reason}")

                    main_frame = customtkinter.CTkFrame(master=r4,
                                    width=400,
                                    height=200)
                    main_frame.pack(padx=20,pady=20)

                    support_label = customtkinter.CTkLabel(master=main_frame,
                                                        text="Please Select Your Complain:")
                    support_label.place(relx=0.05,rely=0.1)

                    complain_combobox_options = customtkinter.StringVar(value="")

                    complain_combobox = customtkinter.CTkComboBox(master=main_frame,
                                                                  values=["comp1","comp2","comp3"],
                                                                  variable=complain_combobox_options)
                    complain_combobox.place(relx=0.55,rely=0.1)

                    complain_button = customtkinter.CTkButton(master=main_frame,
                                                            text="Complain",
                                                            width=342,
                                                            command=complain_button_function)
                    complain_button.place(relx=0.05,rely=0.35)

                    complain_detail_button = customtkinter.CTkButton(master=main_frame,
                                                                    text="Complain Details",
                                                                    width=342,
                                                                    command=show_complain_details)
                    complain_detail_button.place(relx=0.05,rely=0.6)

                    r4.mainloop()

                def order_button_function():

                    global customer_name,selected_product

                    customer_name = customer_entry.get()
                    selected_product = product_combobox.get()

                    if not customer_name:
                        messagebox.showerror("Error", "Please enter customer name!")
                    elif not selected_product:
                        messagebox.showerror("Error", "Please select a product!")
                    else:
                        messagebox.showinfo("Success", "Order placed successfully!")
                
                def show_order_details():
                    customer_name = customer_entry.get()
                    selected_product = product_combobox.get()

                    if not customer_name or not selected_product:
                        messagebox.showerror("Error", "Please place an order before viewing order details!")
                    else:
                        # Rastgele bir teslimat süresi oluştur
                        delivery_time = random.randint(1, 30)
                        
                        # Sipariş detaylarını messagebox'ta göster
                        messagebox.showinfo("Order Details", f"Customer: {customer_name}\nProduct: {selected_product}\nEstimated Delivery Time: {delivery_time} days")

                main_frame = customtkinter.CTkFrame(master=r3,
                                    width=400,
                                    height=250)
                main_frame.pack(padx=20,pady=20)

                customer_label = customtkinter.CTkLabel(master=main_frame,
                                                        text="Enter your Customer Name:")
                customer_label.place(relx=0.1,rely=0.1)
                
                customer_entry = customtkinter.CTkEntry(master=main_frame)
                customer_entry.place(relx=0.55,rely=0.1)

                product_label = customtkinter.CTkLabel(master=main_frame,
                                                    text="Select Product:")
                product_label.place(relx=0.275,rely=0.3)

                product_combobox_options = customtkinter.StringVar(value="")

                product_combobox = customtkinter.CTkComboBox(master=main_frame,
                                                            values=["PC","iPad","Bla Bla"],
                                                            variable=product_combobox_options)
                product_combobox.place(relx=0.55,rely=0.3)

                order_button = customtkinter.CTkButton(master=main_frame,
                                                    text="ORDER",
                                                    width=320,
                                                    command=order_button_function)
                order_button.place(relx=0.1,rely=0.5)

                support_button = customtkinter.CTkButton(master=main_frame,
                                                        text="SUPPORT",
                                                        command=support_button_function)
                support_button.place(relx=0.1,rely=0.75)

                order_details_button = customtkinter.CTkButton(master=main_frame,
                                                        text="ORDER DETAILS",
                                                        command=show_order_details)
                order_details_button.place(relx=0.55,rely=0.75)
                
                #////////////////////////////////////////////////////////////////////////////////////////////#
                r3.mainloop()
                #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "Invalid Username")
    else:
        messagebox.showerror("Error", "Enter all data")

def login():
    r1.destroy()
    frame2 = customtkinter.CTkFrame(master=r2,
                                    width=350,
                                    height=350)
    frame2.pack(padx=20,pady=20)

    global username_entry_login
    global password_entry_login

    username_entry_login = customtkinter.CTkEntry(master=frame2,
                                                placeholder_text="Username",
                                                width=150,
                                                height=40)
    username_entry_login.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    password_entry_login = customtkinter.CTkEntry(master=frame2,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
    password_entry_login.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

    verification_button = customtkinter.CTkButton(master=frame2,
                                          text="Verify and Continue!",
                                          command=loginaccount)
    verification_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
    r2.mainloop()

def entry_to_recipe_app():
        
        r2.destroy()
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

        # Create a frame for the recipe app
        recipe_app_frame = customtkinter.CTkFrame(master=r2)
        recipe_app_frame.pack(pady=20, padx=20, fill="both", expand=True, side="left")

        # Create a listbox to display the recipes
        recipe_app_listbox = tk.Listbox(master=recipe_app_frame, height=30, width=100, bg=r3.cget('bg'), fg='white', font="bold")
        recipe_app_listbox.grid(row=1, column=0, rowspan=5, padx=10)

        # Create a label and entry for the recipe name
        recipe_app_name_label = customtkinter.CTkLabel(master=recipe_app_frame, text="Recipe Name:")
        recipe_app_name_label.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        recipe_name_entry = customtkinter.CTkEntry(master=recipe_app_frame, placeholder_text="Enter Recipe Name")
        recipe_name_entry.grid(row=1, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

        # Create a label and entry for the ingredient name
        recipe_app_link_label = customtkinter.CTkLabel(master=recipe_app_frame, text="Ingredient Name:")
        recipe_app_link_label.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        ingredient_name_entry = customtkinter.CTkEntry(master=recipe_app_frame, placeholder_text="Enter Ingredient Name")
        ingredient_name_entry.grid(row=2, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

        # Create a label and entry for the ingredient piece
        recipe_app_director_label = customtkinter.CTkLabel(master=recipe_app_frame, text="Ingredient Piece:")
        recipe_app_director_label.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        ingredient_piece_entry = customtkinter.CTkEntry(master=recipe_app_frame, placeholder_text="Enter Ingredient Piece")
        ingredient_piece_entry.grid(row=3, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

        # Create a function to add the recipe to the listbox
        def add_recipe():
            recipe_name = recipe_name_entry.get()
            ingredient_name = ingredient_name_entry.get()
            ingredient_piece = ingredient_piece_entry.get()

            recipe_list = f"{recipe_name} - {ingredient_name} - {ingredient_piece}"
            recipe_app_listbox.insert("end", recipe_list)

        def delete_item():
            selected_index = recipe_app_listbox.curselection()
            if selected_index:
                recipe_app_listbox.delete(selected_index)


        # Create a button to add the recipe
        add_recipe_button = customtkinter.CTkButton(master=recipe_app_frame, text="Add Recipe", command=add_recipe)
        add_recipe_button.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        delete_recipe_button = customtkinter.CTkButton(master=recipe_app_frame, text="Delete Recipe", command=delete_item)
        delete_recipe_button.grid(row=4, column=2, pady=10, padx=10, sticky="w")

        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

        r3.mainloop()

#////////////////////////////////////////////////////////////////////////////////////////////#

frame1 = customtkinter.CTkFrame(master=r1,
                                width=350,
                                height=350)
frame1.pack(padx=20,pady=20)

username_entry_register = customtkinter.CTkEntry(master=frame1,
                                     placeholder_text="Username",
                                     width=150,
                                     height=40)
username_entry_register.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

password_entry_register = customtkinter.CTkEntry(master=frame1,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
password_entry_register.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

register_button = customtkinter.CTkButton(master=frame1,
                                          text="Create Your account!",
                                          command=signup)
register_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

register_to_login_label = customtkinter.CTkLabel(master=frame1, 
                                                 text="Already have an account?")
register_to_login_label.place(relx=0.5, rely=0.7, anchor = tk.CENTER)

register_to_login_button = customtkinter.CTkButton(master=frame1,
                                          text="Login!",
                                          command=register_to_login_page)
register_to_login_button.place(relx=0.5, rely=0.8, anchor = tk.CENTER)

#////////////////////////////////////////////////////////////////////////////////////////////#

r1.mainloop()