""" interactive screen showing graphical data to user.

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
"""

import PySimpleGUI as sg
import datasourcenav
import login
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

# ------------------------------- DATA EXPLORER SCREEN ONE START -------------------------------

def DataExplorerScreen1():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
    """    
    # ---- MATPLOTLIB CODE HERE -----
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(len(labels))
    fig, ax = plt.subplots()
    width = 0.35
    rects1 = ax.bar(t - width/2, men_means, width, label='Men')
    rects2 = ax.bar(t + width/2, women_means, width, label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(t)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    # ---- END OF MATPLOTLIB CODE ----

    # ---- Beginning of Matplotlib helper code ----

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ---- Beginning of GUI CODE ----

    # define the window layout
    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
              [sg.Multiline(default_text='Data Information Summary:', size=(
                  35, 5)), sg.Multiline(default_text='Chat System:', size=(35, 5))],
              [sg.Button('Previous'), sg.Button('Next')],
              [sg.Button('Back'), sg.Button('Logout')]]

    # create the form and show it without the plot
    window = sg.Window('Property issue dates', layout, finalize=True,
                       element_justification='center', size=(800, 700))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Previous':
        window.close()
        DataExplorerScreen3()
    if event == 'Next':
        window.close()
        DataExplorerScreen2()
    if event == 'Back':
        window.close()
        datasourcenav.Data_source_page()
    if event == 'Logout':
        window.close()
        login.login_main()
# ------------------------------- DATA EXPLORER SCREEN ONE END -------------------------------

# ------------------------------- DATA EXPLORER SCREEN TWO START -------------------------------

def DataExplorerScreen2():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
    """
    # ---- MATPLOTLIB CODE HERE -----
    fig, ax = plt.subplots(figsize=(7, 5), subplot_kw=dict(aspect="equal"))

    recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

    data = [float(x.split()[0]) for x in recipe]
    ingredients = [x.split()[-1] for x in recipe]


    def func(pct, allvals):
        absolute = int(round(pct/100.*np.sum(allvals)))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)


    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"))

    ax.legend(wedges, ingredients,
            title="Ingredients",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Matplotlib bakery: A pie")


    # ---- END OF MATPLOTLIB CODE ----

    # ---- Beginning of Matplotlib helper code ----

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ---- Beginning of GUI CODE ----

    # define the window layout
    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
              [sg.Multiline(default_text='Data Information Summary:', size=(
                  35, 5)), sg.Multiline(default_text='Chat System:', size=(35, 5))],
              [sg.Button('Previous'), sg.Button('Next')],
              [sg.Button('Back'), sg.Button('Logout')]]

    # create the form and show it without the plot
    window = sg.Window('Current property status', layout, finalize=True,
                       element_justification='center', size=(800, 700))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Previous':
        window.close()
        DataExplorerScreen1()
    if event == 'Next':
        window.close()
        DataExplorerScreen3()
    if event == 'Back':
        window.close()
        datasourcenav.Data_source_page()
    if event == 'Logout':
        window.close()
        login.login_main()
# ------------------------------- DATA EXPLORER SCREEN TWO END -------------------------------

# ------------------------------- DATA EXPLORER SCREEN THREE START -------------------------------

def DataExplorerScreen3():
    """interactive screen showing graphical data to user. Includes navigation and chatsystem

    Returns:
        Data Explorer Screens layout shared between multiple interfaces -PySimpleGUI 
    """
    # ---- MATPLOTLIB CODE HERE -----
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='About as simple as it gets, folks')
    ax.grid()


    # ---- END OF MATPLOTLIB CODE ----

    # ---- Beginning of Matplotlib helper code ----

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # ---- Beginning of GUI CODE ----

    # define the window layout
    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('ZOOM +'), sg.Button('ZOOM -')],
              [sg.Multiline(default_text='Data Information Summary:', size=(
                  35, 5)), sg.Multiline(default_text='Chat System:', size=(35, 5))],
              [sg.Button('Previous'), sg.Button('Next')],
              [sg.Button('Back'), sg.Button('Logout')]]

    # create the form and show it without the plot
    window = sg.Window('Number of property owners', layout,
                       finalize=True, element_justification='center', size=(800, 700))

    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Previous':
        window.close()
        DataExplorerScreen2()
    if event == 'Next':
        window.close()
        DataExplorerScreen1()
    if event == 'Back':
        window.close()
        datasourcenav.Data_source_page()
    if event == 'Logout':
        window.close()
        login.login_main()
# ------------------------------- DATA EXPLORER SCREEN THREE END -------------------------------
# Invoking start script/function for user to begin the proccess of using the application.  
if __name__ == "__main__":
    # def function here
    login.login_main()
    pass