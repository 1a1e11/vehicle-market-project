from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pickle
from User import *
from Vehicles import *
from Accessories import *
FILENAME3 = 'users.dat'
FILENAME = 'cars.dat'
users = []
FILENAME1 = 'mcycles.dat'
FILENAME2 = 'accessories.dat'


def registration_form():
    login_window.destroy()
    registration_window = Tk()
    registration_window.iconbitmap('vehicle.ico')
    registration_window.title('Регистрация')
    registration_window.geometry('500x450+500+200')
    registration_window.resizable(False, False)
    registration_login_label = ttk.Label(registration_window, text='Новый логин:')
    registration_login_label.place(x=100, y=1)
    registration_login_entry = ttk.Entry(registration_window)
    registration_login_entry.place(x=100, y=25)
    registration_password_label = ttk.Label(text='Новый пароль:')
    registration_password_label.place(x=100, y=53)
    registration_password_entry = ttk.Entry(registration_window)
    registration_password_entry.place(x=100, y=75)

    def registration_conf():
        if (registration_password_entry.get() != "" and registration_login_entry.get() != "" and
                (registration_login_entry.get() != 'admin' or registration_password_entry.get() != 'admin')):
            password = registration_password_entry.get()
            login = registration_login_entry.get()
            users.append(User(login, password))
            with open(FILENAME3, 'wb') as f3:
                pickle.dump(users, f3)
            showinfo("Успешно!", "Аккаунт создан")
            registration_window.destroy()
    registration_btn = ttk.Button(text='Создать', command=registration_conf)
    registration_btn.place(x=125, y=100)


def signin_form():
    global users
    with (open(FILENAME3, 'rb') as f3):
        users = pickle.load(f3)
        if login_entry.get() == 'admin' and password_entry.get() == 'admin':
            showinfo("Успешно!", "Вы вошли в аккаунт")
            login_window.destroy()

            def sort_accessories_lb():
                try:
                    list_of_accessories.sort()
                    accessories_var.set(list_of_accessories)
                    with open(FILENAME2, 'wb') as f2:
                        pickle.dump(list_of_accessories, f2)
                except:
                    pass

            def adding_accessories_lb():
                try:
                    add_accessories_win = Tk()
                    add_accessories_win.title('Добавление в список аксессуаров')
                    add_accessories_win.iconbitmap('vehicle.ico')
                    add_accessories_win.geometry('550x450')
                    add_accessories_win.resizable(False, False)
                    frame_add_access = ttk.Frame(borderwidth=1, relief=SOLID, padding=10, master=add_accessories_win)
                    frame_add_access.pack()
                    accessory_type_label = ttk.Label(text='Тип аксессуара', master=frame_add_access)
                    accessory_type_label.pack()
                    accessory_type_entry = ttk.Entry(master=frame_add_access)
                    accessory_type_entry.pack()
                    accessory_price_label = ttk.Label(text='Цена аксессуара', master=frame_add_access)
                    accessory_price_label.pack()
                    accessory_price_entry = ttk.Entry(master=frame_add_access)
                    accessory_price_entry.pack()

                    def confirm_add_accessories():
                        # global FILENAME2
                        try:
                            if accessory_price_entry.get() == '' or accessory_type_entry.get() == '':
                                showerror("Ошибка", "Поля не должны оставаться пустыми")
                            elif accessory_price_entry.get().isnumeric():
                                accessory_type = accessory_type_entry.get()
                                accessory_price = accessory_price_entry.get()
                                list_of_accessories.append(str(Accessories(accessory_type, accessory_price)))
                                with open(FILENAME2, 'wb') as f2:
                                    pickle.dump(list_of_accessories, f2)
                                accessories_var.set(list_of_accessories)
                                add_accessories_win.destroy()
                                showinfo("Добавление аксессуара", "Успешно!")
                        except:
                            pass
                    confirm_add_accessories_btn = ttk.Button(text='Подтвердить', command=confirm_add_accessories,
                                                             master=frame_add_access)
                    confirm_add_accessories_btn.pack()
                except:
                    pass

            def deleting_accessory():
                try:
                    selection_acc = accessories_lb.curselection()
                    accessories_lb.delete(selection_acc[0])
                    list_of_accessories.pop(selection_acc[0])
                    with open(FILENAME2, 'wb') as f2:
                        pickle.dump(list_of_accessories, f2)
                    showinfo("Удаление аксессуара", "Успешно!")
                except:
                    pass

            def editting_accessories_lb():
                try:
                    if not accessories_lb.curselection():
                        pass
                    else:
                        edit_accessories = Tk()
                        edit_accessories.title("Изменение списка аксессуаров")
                        edit_accessories.iconbitmap('vehicle.ico')
                        edit_accessories.geometry('550x450')
                        edit_accessories.resizable(False, False)
                        frame_for_edit_accessories = ttk.Frame(borderwidth=1, relief=SOLID, padding=10,
                                                               master=edit_accessories)
                        frame_for_edit_accessories.pack()
                        new_accessory_type_label = ttk.Label(master=frame_for_edit_accessories,
                                                             text='Введите тип аксессуара')
                        new_accessory_type_label.pack()
                        new_accessory_type_entry = ttk.Entry(master=frame_for_edit_accessories)
                        new_accessory_type_entry.pack()
                        new_accessory_price_label = ttk.Label(text='Введите цену аксессуара',
                                                              master=frame_for_edit_accessories)
                        new_accessory_price_label.pack()
                        new_accessory_price_entry = ttk.Entry(master=frame_for_edit_accessories)
                        new_accessory_price_entry.pack()

                    def confirm_edit_accessories():
                        try:
                            if new_accessory_price_entry.get() == '' or new_accessory_type_entry.get() == '':
                                showerror("Ошибка", "Поля не должны оставаться пустыми")
                            elif new_accessory_price_entry.get().isnumeric():
                                old_acc_edit = accessories_lb.curselection()
                                accessories_lb.delete(old_acc_edit[0])
                                list_of_accessories.pop(old_acc_edit[0])
                                new_acc_type_edit = new_accessory_type_entry.get()
                                new_acc_price_edit = new_accessory_price_entry.get()
                                list_of_accessories.append(str(Accessories(new_acc_type_edit, new_acc_price_edit)))
                                accessories_var.set(list_of_accessories)
                                with open(FILENAME2, 'wb') as f2:
                                    pickle.dump(list_of_accessories, f2)
                                edit_accessories.destroy()
                                showinfo("Изменение списка аксессуаров", "Успешно!")
                        except:
                            pass
                    confirm_edit_accessories_btn = ttk.Button(text='Подтвердить', master=frame_for_edit_accessories,
                                                              command=confirm_edit_accessories)
                    confirm_edit_accessories_btn.pack()
                except:
                    pass

            def sort_mcycles_lb():
                try:
                    list_of_mcycles.sort()
                    mcycles_var.set(list_of_mcycles)
                    with open(FILENAME1, 'wb') as f1:
                        pickle.dump(list_of_mcycles, f1)
                except:
                    pass

            def editing_mcycles_lb():
                try:
                    if not mcycles_lb.curselection():
                        pass
                    else:
                        edit_mcycles = Tk()
                        edit_mcycles.title('Изменение списка мотоциклов')
                        edit_mcycles.iconbitmap('vehicle.ico')
                        edit_mcycles.geometry('550x450')
                        edit_mcycles.resizable(False, False)
                        frame_for_edit_mcycles = ttk.Frame(borderwidth=1, relief=SOLID, padding=10, master=edit_mcycles)
                        frame_for_edit_mcycles.pack()
                        label_new_mcycle_mark = ttk.Label(text='Введите марку мотоцикла', master=frame_for_edit_mcycles)
                        label_new_mcycle_mark.pack()
                        entry_new_mcycle_mark = ttk.Entry(master=frame_for_edit_mcycles)
                        entry_new_mcycle_mark.pack()
                        label_new_mcycle_model = ttk.Label(text='Введите модель мотоцикла', master=frame_for_edit_mcycles)
                        label_new_mcycle_model.pack()
                        entry_new_mcycle_model = ttk.Entry(master=frame_for_edit_mcycles)
                        entry_new_mcycle_model.pack()
                        label_new_mcycle_year = ttk.Label(text='Введите год производства мотоцикла',
                                                          master=frame_for_edit_mcycles)
                        label_new_mcycle_year.pack()
                        entry_new_mcycle_year = ttk.Entry(master=frame_for_edit_mcycles)
                        entry_new_mcycle_year.pack()
                        label_new_mcycle_price = ttk.Label(text='Введите цену мотоцикла', master=frame_for_edit_mcycles)
                        label_new_mcycle_price.pack()
                        entry_new_mcycle_price = ttk.Entry(master=frame_for_edit_mcycles)
                        entry_new_mcycle_price.pack()
                        label_new_mcycle_distance = ttk.Label(master=frame_for_edit_mcycles,
                                                              text="Введите пробег мотоцикла")
                        label_new_mcycle_distance.pack()
                        entry_new_mcycle_distance = ttk.Entry(master=frame_for_edit_mcycles)
                        entry_new_mcycle_distance.pack()

                    def confirm_edit_mcycles():
                        try:
                            if entry_new_mcycle_distance.get() == '' or entry_new_mcycle_price.get() == '' \
                                    or entry_new_mcycle_year.get() == '' or entry_new_mcycle_model.get() == '' \
                                    or entry_new_mcycle_mark.get() == '':
                                showerror("Ошибка", "Поля не должны оставаться пустыми")
                            elif entry_new_mcycle_distance.get().isnumeric() and\
                                    entry_new_mcycle_year.get().isnumeric() and\
                                    entry_new_mcycle_price.get().isnumeric():
                                old = mcycles_lb.curselection()
                                mcycles_lb.delete(old[0])
                                list_of_mcycles.pop(old[0])
                                new_mcycle_mark = entry_new_mcycle_mark.get()
                                new_mcycle_model = entry_new_mcycle_model.get()
                                new_mcycle_year = entry_new_mcycle_year.get()
                                new_mcycle_price = entry_new_mcycle_price.get()
                                new_mcycle_distance = entry_new_mcycle_distance.get()
                                list_of_mcycles.append(str(Motorcycles(new_mcycle_mark, new_mcycle_model,
                                                                       new_mcycle_year, new_mcycle_price,
                                                                       new_mcycle_distance)))
                                mcycles_var.set(list_of_mcycles)
                                with open(FILENAME1, 'wb') as f1:
                                    pickle.dump(list_of_mcycles, f1)
                                edit_mcycles.destroy()
                                showinfo("Изменение мотоцикла", "Успешно!")
                        except:
                            pass

                    confirm_edit_mcycles_btn = ttk.Button(text='Подтвердить', master=frame_for_edit_mcycles,
                                                          command=confirm_edit_mcycles)
                    confirm_edit_mcycles_btn.pack()

                except:
                    pass

            def deleting_from_mcycles_lb():
                try:
                    selection_mc = mcycles_lb.curselection()
                    mcycles_lb.delete(selection_mc[0])
                    list_of_mcycles.pop(selection_mc[0])
                    with open(FILENAME1, 'wb') as f1:
                        pickle.dump(list_of_mcycles, f1)
                    showinfo("Удаление мотоцикла", "Успешно!")
                except:
                    pass

            def add_to_mcycles_lb():
                try:
                    add_window_mcycles = Tk()
                    add_window_mcycles.title("Добавление в список мотоциклов")
                    add_window_mcycles.iconbitmap('vehicle.ico')
                    add_window_mcycles.geometry('550x450')
                    add_window_mcycles.resizable(False, False)
                    frame_for_mcycles_adding = ttk.Frame(borderwidth=1, relief=SOLID, padding=10,
                                                         master=add_window_mcycles)
                    frame_for_mcycles_adding.pack()
                    mcycle_mark_label = ttk.Label(text='Введите марку мотоцикла', master=frame_for_mcycles_adding)
                    mcycle_mark_label.pack()
                    mcycle_mark_entry_to_list = ttk.Entry(master=frame_for_mcycles_adding)
                    mcycle_mark_entry_to_list.pack()
                    mcycle_model_label = ttk.Label(text='Введите модель мотоцикла', master=frame_for_mcycles_adding)
                    mcycle_model_label.pack()
                    mcycle_model_entry_to_list = ttk.Entry(master=frame_for_mcycles_adding)
                    mcycle_model_entry_to_list.pack()
                    mcycle_year_label = ttk.Label(text='Введите год производства мотоцикла',
                                                  master=frame_for_mcycles_adding)
                    mcycle_year_label.pack()
                    mcycle_year_entry_to_list = ttk.Entry(master=frame_for_mcycles_adding)
                    mcycle_year_entry_to_list.pack()
                    mcycle_price_label = ttk.Label(text='Введите цену мотоцикла', master=frame_for_mcycles_adding)
                    mcycle_price_label.pack()
                    mcycle_price_entry_to_list = ttk.Entry(master=frame_for_mcycles_adding)
                    mcycle_price_entry_to_list.pack()
                    mcycle_distance_label = ttk.Label(text='Введите пробег мотоцикла', master=frame_for_mcycles_adding)
                    mcycle_distance_label.pack()
                    mcycle_distance_entry_to_list = ttk.Entry(master=frame_for_mcycles_adding)
                    mcycle_distance_entry_to_list.pack()
                except:
                    pass

                def conf_add_mcycle():
                    try:
                        if mcycle_mark_entry_to_list.get() == "" or mcycle_distance_entry_to_list.get() == '' \
                                or mcycle_price_entry_to_list.get() == '' or mcycle_model_entry_to_list.get() == '' \
                                or mcycle_year_entry_to_list.get() == '':
                            showerror("Ошибка", "Поля не должны оставаться пустыми")

                        elif mcycle_distance_entry_to_list.get().isnumeric()\
                                and mcycle_price_entry_to_list.get().isnumeric()\
                                and mcycle_year_entry_to_list.get().isnumeric():
                            mcycle_mark = mcycle_mark_entry_to_list.get()
                            mcycle_model = mcycle_model_entry_to_list.get()
                            mcycle_year = mcycle_year_entry_to_list.get()
                            mcycle_price = mcycle_price_entry_to_list.get()
                            mcycle_distance = mcycle_distance_entry_to_list.get()

                            list_of_mcycles.append(str(Motorcycles(mcycle_mark, mcycle_model, mcycle_year,
                                                                   mcycle_price,
                                                                   mcycle_distance)))
                            mcycles_var.set(list_of_mcycles)
                            with open(FILENAME1, 'wb') as f1:
                                pickle.dump(list_of_mcycles, f1)
                            add_window_mcycles.destroy()
                            showinfo('Добавление машины', "Успешно!")
                    except:
                        pass

                confirm_adding_for_mcycles_btn = ttk.Button(text='Подтвердить', master=frame_for_mcycles_adding,
                                                            command=conf_add_mcycle)
                confirm_adding_for_mcycles_btn.pack()

            def sort_cars_lb():
                try:
                    list_of_cars.sort()
                    lc_var.set(list_of_cars)
                    with open(FILENAME, 'wb') as f:
                        pickle.dump(list_of_cars, f)
                except:
                    pass

            def add_to_lc_lb():
                try:
                    add_window = Tk()
                    add_window.title("Добавление в список машин")
                    add_window.iconbitmap('vehicle.ico')
                    add_window.geometry('550x450')
                    add_window.resizable(False, False)
                    frame_for_adding_car = ttk.Frame(borderwidth=1, relief=SOLID, padding=10, master=add_window)
                    frame_for_adding_car.pack()
                    mark_label = ttk.Label(text='Введите марку машины', master=frame_for_adding_car)
                    mark_label.pack()
                    mark_entry_to_list = ttk.Entry(master=frame_for_adding_car)
                    mark_entry_to_list.pack()
                    model_label = ttk.Label(text='Введите модель машины', master=frame_for_adding_car)
                    model_label.pack()
                    model_entry_to_list = ttk.Entry(master=frame_for_adding_car)
                    model_entry_to_list.pack()
                    year_label = ttk.Label(text='Введите год производства машины', master=frame_for_adding_car)
                    year_label.pack()
                    year_entry_to_list = ttk.Entry(master=frame_for_adding_car)
                    year_entry_to_list.pack()
                    ctype_label = ttk.Label(text='Введите тип машины', master=frame_for_adding_car)
                    ctype_label.pack()
                    ctype_entry_to_list = ttk.Entry(master=frame_for_adding_car)
                    ctype_entry_to_list.pack()
                    price_label = ttk.Label(text='Введите цену машины', master=frame_for_adding_car)
                    price_label.pack()
                    price_entry_to_list = ttk.Entry(master=frame_for_adding_car)
                    price_entry_to_list.pack()
                    seats_label = ttk.Label(text='Введите количество сидений машины', master=frame_for_adding_car)
                    seats_label.pack()
                    seats_entry_to_list = ttk.Entry(master=frame_for_adding_car)
                    seats_entry_to_list.pack()
                    distance_label = ttk.Label(text='Введите пробег машины', master=frame_for_adding_car)
                    distance_label.pack()
                    distance_entry_to_list = ttk.Entry(master=frame_for_adding_car)
                    distance_entry_to_list.pack()
                except:
                    pass

                def confirm_adding():
                    try:
                        if mark_entry_to_list.get() == "" or model_entry_to_list.get() =='' \
                                or year_entry_to_list.get() == '' or ctype_entry_to_list.get() == '' \
                                or price_entry_to_list.get() == '' or seats_entry_to_list.get() == '' \
                                or distance_entry_to_list.get() == '':
                            showerror("Ошибка", "Поля не должны оставаться пустыми")

                        elif year_entry_to_list.get().isnumeric() and price_entry_to_list.get().isnumeric() and\
                                seats_entry_to_list.get().isnumeric() and distance_entry_to_list.get().isnumeric():
                            mark = mark_entry_to_list.get()
                            model = model_entry_to_list.get()
                            year = year_entry_to_list.get()
                            car_type = ctype_entry_to_list.get()
                            price = price_entry_to_list.get()
                            seats = seats_entry_to_list.get()
                            distance = distance_entry_to_list.get()

                            list_of_cars.append(str(Cars(mark, model, year, car_type, price, seats, distance)))
                            lc_var.set(list_of_cars)
                            with open(FILENAME, 'wb') as f:
                                pickle.dump(list_of_cars, f)
                            add_window.destroy()
                            showinfo('Добавление машины', "Успешно!")
                    except:
                        pass

                confirm_adding_btn = ttk.Button(text='Подтвердить', master=frame_for_adding_car, command=confirm_adding)
                confirm_adding_btn.pack()

            def delete_from_cars_lb():
                try:
                    selection = lc_lb.curselection()
                    lc_lb.delete(selection[0])
                    list_of_cars.pop(selection[0])
                    with open(FILENAME, 'wb') as f:
                        pickle.dump(list_of_cars, f)
                    showinfo('Удаление машины', "Успешно!")
                except:
                    pass

            def edit_cars_lb_fun():
                try:
                    if not lc_lb.curselection():
                        pass
                    else:
                        edit_cars_lb = Tk()
                        edit_cars_lb.title('Изменение списка машин')
                        edit_cars_lb.iconbitmap('vehicle.ico')
                        edit_cars_lb.geometry('550x450')
                        edit_cars_lb.resizable(False, False)
                        frame_for_edit_cars = ttk.Frame(borderwidth=1, relief=SOLID, padding=10, master=edit_cars_lb)
                        frame_for_edit_cars.pack()
                        label_new_mark = ttk.Label(master=frame_for_edit_cars, text="Введите марку машины")
                        label_new_mark.pack()
                        new_mark_entry_to_list = ttk.Entry(master=frame_for_edit_cars)
                        new_mark_entry_to_list.pack()
                        label_new_model = ttk.Label(master=frame_for_edit_cars, text='Введите модель машины')
                        label_new_model.pack()
                        new_model_entry_to_list = ttk.Entry(master=frame_for_edit_cars)
                        new_model_entry_to_list.pack()
                        label_new_year = ttk.Label(master=frame_for_edit_cars, text="Введите год машины")
                        label_new_year.pack()
                        new_year_entry_to_list = ttk.Entry(master=frame_for_edit_cars)
                        new_year_entry_to_list.pack()
                        label_new_ctype = ttk.Label(master=frame_for_edit_cars, text="Введите тип машины")
                        label_new_ctype.pack()
                        new_ctype_entry_to_list = ttk.Entry(master=frame_for_edit_cars)
                        new_ctype_entry_to_list.pack()
                        label_new_price = ttk.Label(master=frame_for_edit_cars, text="Введите цену машины")
                        label_new_price.pack()
                        new_price_entry_to_list = ttk.Entry(master=frame_for_edit_cars)
                        new_price_entry_to_list.pack()
                        label_new_seats = ttk.Label(master=frame_for_edit_cars, text="Введите количество сидений машины")
                        label_new_seats.pack()
                        new_seats_entry_to_list = ttk.Entry(master=frame_for_edit_cars)
                        new_seats_entry_to_list.pack()
                        label_new_distance = ttk.Label(master=frame_for_edit_cars, text="Введите пробег машины")
                        label_new_distance.pack()
                        new_distance_entry_to_list = ttk.Entry(master=frame_for_edit_cars)
                        new_distance_entry_to_list.pack()

                    def confirm_editting_fun():
                        try:
                            if new_mark_entry_to_list.get() == '' or new_distance_entry_to_list.get() == '' \
                                    or new_seats_entry_to_list.get() == '' or new_price_entry_to_list.get() == '' \
                                    or new_ctype_entry_to_list.get() == '' or new_model_entry_to_list.get() == '':
                                showerror("Ошибка", "Поля не должны оставаться пустыми")

                            elif new_year_entry_to_list.get().isnumeric() and new_price_entry_to_list.get().isnumeric() and \
                                    new_seats_entry_to_list.get().isnumeric() and \
                                    new_distance_entry_to_list.get().isnumeric():

                                old = lc_lb.curselection()
                                lc_lb.delete(old[0])
                                list_of_cars.pop(old[0])
                                new_mark = new_mark_entry_to_list.get()
                                new_model = new_model_entry_to_list.get()
                                new_year = new_year_entry_to_list.get()
                                new_ctype = new_ctype_entry_to_list.get()
                                new_price = new_price_entry_to_list.get()
                                new_seats = new_seats_entry_to_list.get()
                                new_distance = new_distance_entry_to_list.get()
                                list_of_cars.append(
                                        str(Cars(new_mark, new_model, new_year, new_ctype, new_price, new_seats,
                                                 new_distance)))
                                lc_var.set(list_of_cars)
                                with open(FILENAME, 'wb') as f:
                                    pickle.dump(list_of_cars, f)
                                edit_cars_lb.destroy()
                                showinfo("Изменение машины", "Успешно!")

                        except:
                            pass

                    confirm_editting_btn = ttk.Button(master=frame_for_edit_cars, text="Подтвердить",
                                                      command=confirm_editting_fun)
                    confirm_editting_btn.pack()
                except:
                    pass

            kia = str(Cars('Kia', 'Rio', 2006, "Хетчбэк", 11600, 5, 265000))
            # honda = Motorcycles('Мотоцикл', 'Honda', 'H’ness CB350 DLX Pro', 2023, 7999, 0)
            toyota = str(Cars('Toyota', 'Prius', 2009, 'Лифтбэк', 15500, 5, 260000))

            zerkalo = str(Accessories("Зеркало заднего вида", 300))

            vehicle_market_adm = Tk()
            vehicle_market_adm.title('Vehicle Market Admin Panel')
            vehicle_market_adm.geometry('1500x800+1+1')
            vehicle_market_adm.resizable(False, False)
            vehicle_market_adm.iconbitmap('vehicle.ico')
            vehicle_market_adm['bg'] = 'red'
            admin_panel_label = ttk.Label(text='Админ-панель', font=("Comic Sans MS", 45), master=vehicle_market_adm,
                                          foreground='white', background='red')
            admin_panel_label.place(x=1050, y=1)

            list_of_cars = [toyota, kia]
            with open(FILENAME, 'rb') as f:
                list_of_cars = pickle.load(f)
            lc_var = StringVar(value=list_of_cars)
            frame_for_lb = ttk.Frame(borderwidth=0, relief=FLAT, padding=30)
            frame_for_lb.place(height=800, width=1000)
            label_cars = ttk.Label(text='Машины:', master=vehicle_market_adm, font=("Comic Sans MS", 15))
            label_cars.place(x=30, y=0)
            lc_lb = Listbox(listvariable=lc_var, master=frame_for_lb)
            lc_lb.place(height=100, width=850, x=1, y=1)
            add_car_button = ttk.Button(text='Добавить', master=frame_for_lb, command=add_to_lc_lb)
            add_car_button.place(height=30, width=100, x=1, y=101)
            delete_button = ttk.Button(text='Удалить', master=frame_for_lb, command=delete_from_cars_lb)
            delete_button.place(height=30, width=100, x=100, y=101)
            edit_cars_button = ttk.Button(text='Изменить', master=frame_for_lb, command=edit_cars_lb_fun)
            edit_cars_button.place(height=30, width=100, x=199, y=101)
            sort_cars_button = ttk.Button(text='Сортировка', master=frame_for_lb, command=sort_cars_lb)
            sort_cars_button.place(height=30, width=100, x=300, y=101)
            y_scrollbar_cars_adm = ttk.Scrollbar(master=lc_lb, orient='vertical')
            y_scrollbar_cars_adm.pack(side=RIGHT, fill=BOTH)
            y_scrollbar_cars_adm.config(command=lc_lb.yview)
            lc_lb.config(yscrollcommand=y_scrollbar_cars_adm.set)

            list_of_mcycles = [Motorcycles('Honda', 'H’ness CB350 DLX Pro', 2023, 7999, 0)]
            with open(FILENAME1, 'rb') as f1:
                list_of_mcycles = pickle.load(f1)
            mcycles_var = StringVar(value=list_of_mcycles)
            mcycles_label = ttk.Label(text='Мотоциклы:', master=vehicle_market_adm, font=("Comic Sans MS", 15))
            mcycles_label.place(x=30, y=179)
            mcycles_lb = Listbox(listvariable=mcycles_var, master=frame_for_lb)
            mcycles_lb.place(height=100, width=800, x=1, y=180)
            y_scrollbar_mcycles_admin = ttk.Scrollbar(master=mcycles_lb, orient='vertical')
            y_scrollbar_mcycles_admin.pack(side=RIGHT, fill=BOTH)
            mcycles_lb.config(yscrollcommand=y_scrollbar_mcycles_admin.set)
            y_scrollbar_mcycles_admin.config(command=mcycles_lb.yview)
            add_mcycles_btn = ttk.Button(text='Добавить', master=frame_for_lb, command=add_to_mcycles_lb)
            add_mcycles_btn.place(height=30, width=100, x=1, y=280)
            delete_mcycles_btn = ttk.Button(text='Удалить', master=frame_for_lb, command=deleting_from_mcycles_lb)
            delete_mcycles_btn.place(height=30, width=100, x=100, y=280)
            edit_mcycles_btn = ttk.Button(text='Изменить', master=frame_for_lb, command=editing_mcycles_lb)
            edit_mcycles_btn.place(height=30, width=100, x=200, y=280)
            sort_mcycles_btn = ttk.Button(text='Сортировка', master=frame_for_lb, command=sort_mcycles_lb)
            sort_mcycles_btn.place(height=30, width=100, x=300, y=280)

            list_of_accessories = [zerkalo]
            with open(FILENAME2, 'rb') as f2:
                list_of_accessories = pickle.load(f2)
            accessories_var = StringVar(value=list_of_accessories)
            accessories_label = ttk.Label(text='Аксессуары:', master=frame_for_lb, font=("Comic Sans MS", 15))
            accessories_label.place(x=1, y=325)
            accessories_lb = Listbox(master=frame_for_lb, listvariable=accessories_var)
            accessories_lb.place(x=1, y=355, height=100, width=500)
            add_accessories_btn = ttk.Button(text='Добавить', master=frame_for_lb, command=adding_accessories_lb)
            add_accessories_btn.place(y=455, x=1, height=30, width=100)
            delete_accessories_btn = ttk.Button(text='Удалить', master=frame_for_lb, command=deleting_accessory)
            delete_accessories_btn.place(y=455, x=100, height=30, width=100)
            edit_accessories_btn = ttk.Button(text='Изменить', master=frame_for_lb, command=editting_accessories_lb)
            edit_accessories_btn.place(y=455, x=200, height=30, width=100)
            sort_accessories_btn = ttk.Button(text='Сортировка', master=frame_for_lb, command=sort_accessories_lb)
            sort_accessories_btn.place(y=455, x=300, height=30, width=100)
            y_scrollbar_accessories_adm = ttk.Scrollbar(master=accessories_lb, orient='vertical')
            y_scrollbar_accessories_adm.pack(side=RIGHT, fill=BOTH)
            y_scrollbar_accessories_adm.config(command=accessories_lb.yview)
            accessories_lb.config(yscrollcommand=y_scrollbar_accessories_adm.set)
        for user in users:
            try:
                if login_entry.get() == user.login and password_entry.get() == user.password:
                    user_name = user.login
                    showinfo("Успех", "Вы вошли в аккаунт")
                    login_window.destroy()
                    vehicle_market_user = Tk()
                    vehicle_market_user.title('Vehicle Market')
                    vehicle_market_user.iconbitmap('vehicle.ico')
                    vehicle_market_user.resizable(False, False)
                    vehicle_market_user.geometry('1500x800+1+1')
                    frame_for_vm_user = ttk.Frame(master=vehicle_market_user, borderwidth=0, relief=FLAT, padding=30)
                    frame_for_vm_user.place(height=800, width=1000)
                    label_cars_user = ttk.Label(text='Машины:', master=vehicle_market_user, font=("Comic Sans MS", 15))
                    label_cars_user.place(x=30, y=3)
                    with open(FILENAME, 'rb') as f:
                        list_of_cars = pickle.load(f)
                    with open(FILENAME1, 'rb') as f1:
                        list_of_mcycles = pickle.load(f1)
                    with open(FILENAME2, 'rb') as f2:
                        list_of_accessories = pickle.load(f2)

                    def buy_car():
                        car_to_buy = cars_user_lb.curselection()
                        cars_user_lb.delete(car_to_buy[0])
                        list_of_cars.pop(car_to_buy[0])
                        with open(FILENAME, 'wb') as f:
                            pickle.dump(list_of_cars, f)
                        showinfo("Успешно", "Поздравляем с приобретением!")

                    def buy_mcycle():
                        mcycle_to_buy = mcycles_user_lb.curselection()
                        mcycles_user_lb.delete(mcycle_to_buy[0])
                        list_of_mcycles.pop(mcycle_to_buy[0])
                        with open(FILENAME1, 'wb') as f1:
                            pickle.dump(list_of_mcycles, f1)
                        showinfo("Успешно", "Поздравляем с приобретением!")

                    def buy_accessory():
                        accessory_to_buy = accessories_user_lb.curselection()
                        accessories_user_lb.delete(accessory_to_buy[0])
                        list_of_accessories.pop(accessory_to_buy[0])
                        with open(FILENAME2, 'wb') as f2:
                            pickle.dump(list_of_accessories, f2)
                        showinfo("Успешно", "Поздравляем с приобретением!")

                    def window_closed():
                        print(f"Пользователь {user_name} закрыл программу")
                        vehicle_market_user.destroy()
                    car_var_user = StringVar(value=list_of_cars)
                    mcycles_var_user = StringVar(value=list_of_mcycles)
                    accessories_var_user = StringVar(value=list_of_accessories)

                    cars_user_lb = Listbox(master=frame_for_vm_user, listvariable=car_var_user)
                    cars_user_lb.place(height=100, width=850, x=1, y=5)
                    y_scrollbar_cars_user = ttk.Scrollbar(cars_user_lb, orient='vertical')
                    y_scrollbar_cars_user.pack(side=RIGHT, fill=BOTH)
                    cars_user_lb.config(yscrollcommand=y_scrollbar_cars_user.set)
                    y_scrollbar_cars_user.config(command=cars_user_lb.yview)
                    buy_car_user_btn = ttk.Button(text='Купить', master=frame_for_vm_user, command=buy_car)
                    buy_car_user_btn.place(height=30, width=100, x=1, y=105)

                    label_motorcycles_user = ttk.Label(master=vehicle_market_user, text='Мотоциклы:',
                                                       font=("Comic Sans MS", 15))
                    label_motorcycles_user.place(x=30, y=180)
                    mcycles_user_lb = Listbox(master=frame_for_vm_user, listvariable=mcycles_var_user)
                    mcycles_user_lb.place(height=100, width=800, x=1, y=181)
                    y_scrollbar_mcycles_user = ttk.Scrollbar(mcycles_user_lb, orient='vertical')
                    y_scrollbar_mcycles_user.pack(side=RIGHT, fill=BOTH)
                    mcycles_user_lb.config(yscrollcommand=y_scrollbar_mcycles_user.set)
                    y_scrollbar_mcycles_user.config(command=mcycles_user_lb.yview)
                    buy_mcycle_user_btn = ttk.Button(master=frame_for_vm_user, text='Купить', command=buy_mcycle)
                    buy_mcycle_user_btn.place(height=30, width=100, x=1, y=281)

                    label_accessories_user = ttk.Label(text='Аксессуары:', master=frame_for_vm_user,
                                                       font=("Comic Sans MS", 15))
                    label_accessories_user.place(x=1, y=325)
                    accessories_user_lb = Listbox(master=frame_for_vm_user, listvariable=accessories_var_user)
                    accessories_user_lb.place(x=1, y=355, height=100, width=500)
                    y_scrollbar_accessories_user = ttk.Scrollbar(accessories_user_lb, orient='vertical')
                    y_scrollbar_accessories_user.pack(side=RIGHT, fill=BOTH)
                    accessories_user_lb.config(yscrollcommand=y_scrollbar_accessories_user.set)
                    y_scrollbar_accessories_user.config(command=accessories_user_lb.yview)
                    buy_accessory_user_btn = ttk.Button(master=frame_for_vm_user, text='Купить', command=buy_accessory)
                    buy_accessory_user_btn.place(x=1, y=455, height=30, width=100)

                    frame_for_user_data = ttk.Frame(master=vehicle_market_user, relief=FLAT, padding=10, height=800,
                                                    width=500)
                    frame_for_user_data.place(x=1300, y=1)
                    user_name_label = ttk.Label(master=frame_for_user_data, background='cyan', text=f'Аккаунт: {user_name}',
                                                font=("Comic Sans MS", 15))
                    user_name_label.place(x=1, y=1)
                    vehicle_market_user.protocol("WM_DELETE_WINDOW", window_closed)
                elif login_entry.get() == '' or password_entry.get() == '':
                    showerror("Ошибка", "Введите логин или пароль")
            except:
                pass


login_window = Tk()
login_window.iconbitmap('vehicle.ico')
login_window.title('Вход')
login_window.geometry('500x450+500+200')
login_window.resizable(False, False)
login_label = ttk.Label(login_window, text='Логин:')
login_label.place(x=100, y=1)
login_entry = ttk.Entry(login_window)
login_entry.place(x=100, y=25)
password_label = ttk.Label(login_window, text='Пароль:')
password_label.place(x=100, y=53)
password_entry = ttk.Entry(login_window, show='*')
password_entry.place(x=100, y=75)


def show_signin_password():
    if signin_password_var.get() == 1:
        password_entry['show'] = ""
        check_btn_for_signin_password.config(text='Скрыть пароль')
    else:
        password_entry['show'] = "*"
        check_btn_for_signin_password.config(text='Показать пароль')


signin_password_var = IntVar()
check_btn_for_signin_password = Checkbutton(master=login_window, text='Показать пароль', variable=signin_password_var,
                                            command=show_signin_password)
check_btn_for_signin_password.place(x=250, y=75)
signin_btn = ttk.Button(login_window, text="Вход", command=signin_form)
signin_btn.place(x=125, y=100)


registration_btn = ttk.Button(text='Создать аккаунт', master=login_window, command=registration_form)
registration_btn.place(x=115, y=125)

login_window.mainloop()
