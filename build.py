"""[Simple Data Explorer screen template
    that can be used as a module for different displays of data]
"""
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import figures
import data_controller as dc
import login
import DES
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

matplotlib.use('TkAgg')


def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')


def get_figure(des_name):
        if des_name == 'DES1':
            return figures.pie()
        if des_name == 'DES2':
            return figures.line_plot()
        if des_name == 'DES3':
            return figures.stack_plot()


def show(nextScreen, previousScreen, des_name):


    # ------ ANCHOR MENU SECTION ------ #
    menu_def = [['&File', ['&Open Upload', '&Open Merge', '&Logout', '&Exit']],
                ['&Navigation', [
                    '&Size of Angler fish(DES1)', '&Angler fish observed(DES2)', '&Min and max depth of angler fish(DES3)']],
                ['&Help', '&About...'],
                ]
    
    
    # ------ ANCHOR DRAW CANVAS SECTION ------ #
    def draw_figure(canvas, figure):
        if canvas.children:
            for child in canvas.winfo_children():
                child.destroy()
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        NavigationToolbar2Tk.toolitems = [t for t in NavigationToolbar2Tk.toolitems if t[0] not in (
        'Subplots', 'Back', 'Forward', 'Save')]

        # pack_toolbar=False will make it easier to use a layout manager later on.

        toolbar = NavigationToolbar2Tk(figure_canvas_agg, canvas, pack_toolbar=False)
        toolbar.update()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        toolbar.pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ------ ANCHOR GUI/LAYOUT SECTION ------ #
    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Canvas(key='-CANVAS-')],
        [sg.Multiline(default_text='Chat History:',
                      size=(55, 11), font=('current 12'), disabled=True),
        sg.Frame(layout=[
            
        [sg.Multiline(size=(80, 7), font=('current 12'))],
        [sg.Button('Send', size=(81, 0), font=('current 12'))],
        ], title='Chat input', font=('current 12') )],
        
        [sg.Button('Previous', font=('current 20')), sg.Button('Next', font=('current 20') )]]

    window = sg.Window(des_name,
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1),
                       finalize=True,
                       size=(1000, 720))
    
    fig = get_figure(des_name)
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    # ------ ANCHOR LOOP & PROCESS BUTTON & MENU CHOICES ------ #
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        print(event, values)
        # ------ Process button choices ------ #
        if event == 'Previous':
            if fig_canvas_agg:
                delete_figure_agg(fig_canvas_agg)
            window.close()
            previousScreen()
        if event == 'Next':
            if fig_canvas_agg:
                delete_figure_agg(fig_canvas_agg)
            window.close()
            nextScreen()

        # ------ Process menu choices ------ #
        if event == 'About...':
            sg.popup('About this program', 'Version 1.0',
                     'PySimpleGUI Version', sg.version,  grab_anywhere=True,)
        if event == 'Open Upload':
            file_name = sg.PopupGetFile('Please select file to upload (the file to add to or merge in)',
                                        file_types=(("Comma separated value", "*.csv")))
            dc.upload(file_name)
            if fig_canvas_agg:
                delete_figure_agg(fig_canvas_agg)
            fig = get_figure(des_name)
            fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
        if event == 'Open Merge':
            file_name = sg.PopupGetFile('Please select file to upload (the file to add to or merge in)',
                                        file_types=(("Comma separated value", "*.csv")))
            dc.merge(file_name)
            if fig_canvas_agg:
                delete_figure_agg(fig_canvas_agg)
            fig = get_figure(des_name)
            fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
            
        if event == 'Size of Angler fish(DES1)':
            window.close()
            DES.one()
            window.close()
        if event == 'Angler fish observed(DES2)':
            window.close()
            DES.two()
            window.close()
        if event == 'Min and max depth of angler fish(DES3)':
            window.close()
            DES.three()
            window.close()
        if event == 'Logout':
            window.close()
            login.login_main()
