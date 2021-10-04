import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import figures
import datacontroller as dc
import login

matplotlib.use('TkAgg')

"""[Simple Data Explorer screen template
    that can be used as a module for different displays of data]
"""


def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')


def getfigure(des_name):
        import figures
        if des_name == 'DES1':
            return figures.fish()
        if des_name == 'DES2':
            return figures.line_plot()
        if des_name == 'DES3':``
            return figures.scatter_plots()


def show(nextScreen, previousScreen, des_name):

    sg.set_options(element_padding=(5, 5))

    # ------ ANCHOR MENU SECTION ------ #
    menu_def = [['&File', ['&Open Upload', '&Open Merge', '&Logout', '&Exit']],
                ['&Navigation', [
                    '&Size of Angler fish(DES1)', '&Types of ownership(DES2)', '&Number of property owners(DES3)']],
                ['&Help', '&About...'],
                ]

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg


    # ------ ANCHOR GUI/LAYOUT SECTION ------ #
    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Canvas(key='-CANVAS-')],
        [sg.Multiline(default_text='Data Information Summary:',
                      size=(55, 11), font=('current 12')),
         sg.Multiline(default_text='Chat System:',
                      font=('current 12'), size=(55, 11))],
        [sg.Button('Previous', font=('current 20')), sg.Button('Next', font=('current 20'))]]

    window = sg.Window(des_name,
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1),
                       finalize=True,
                       element_justification='center',
                       size=(1000, 700))
    
    fig = getfigure(des_name)
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
            fig = getfigure(des_name)
            fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
        if event == 'Open Merge':
            file_name = sg.PopupGetFile('Please select file to upload (the file to add to or merge in)',
                                        file_types=(("Comma separated value", "*.csv")))
            dc.merge(file_name)
            if fig_canvas_agg:
                delete_figure_agg(fig_canvas_agg)
            fig = getfigure(des_name)
            fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
            
        if event == 'Size of Angler fish(DES1)':
            window.close()
            show()
            window.close()
        if event == 'Types of ownership(DES2)':
            window.close()
            show()
            window.close()
        if event == 'Number of property owners(DES3)':
            window.close()
            show()
            window.close()
        if event == 'Logout':
            window.close()
            login.login_main()


# template empty until parsed in data

# class DataExplorerScreen()
