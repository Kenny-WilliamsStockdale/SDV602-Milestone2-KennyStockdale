"""
    page that takes inputs to upload to data source
"""
import PySimpleGUI as sg
import datasourcenav
import login

# ------------------------------- UPLOAD PAGE START -------------------------------

def Upload_new_data_page():
    """
        Function that allows user input to upload to data source
    """    
    layout = [
            [sg.Frame(layout=[
                [sg.Text('Title_No:', size=(14, 1)), sg.InputText(
                    '', size=(15, 1))],
                [sg.Text('Status:', size=(14, 1)), sg.InputText(
                    '', size=(15, 1))],
                [sg.Text('Type:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))],
                [sg.Text('Land_district:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))],
                [sg.Text('Issue_date:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))],
                [sg.Text('Guarantee_Status:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))],
                [sg.Text('Number_Owners:', size=(14, 1)),
                 sg.InputText('', size=(15, 1))]
            ], title=""), sg.Frame(layout=[

                [sg.Text('Estate_description')],
                [sg.Multiline('', size=(35, 5))]], title="")],
            [sg.Button('Back'), sg.Button('Upload new data')]
            
        ]
            
    
    window = sg.Window('Upload new data page', layout,
                       finalize=True, size=(500, 250))

    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Back':
        window.close()
        datasourcenav.Data_source_page()
    if event == 'Upload new data':
        window.close()
        Upload_new_data_successful()
# ------------------------------- UPLOAD PAGE END -------------------------------

# ------------------------------- UPLOAD CONFIRMATION PAGE START -------------------------------

def Upload_new_data_successful():
    """
        function returns successful upload of data
    """    
    layout = [
        [sg.Text('Success! New data has been added.')],
        [sg.Button('Ok')]]
    window = sg.Window('New data confirmation', layout,
                       finalize=True, size=(350, 80), element_justification='c')
    event, values = window.read()
    print(event, values)

    if event == None or event == 'Exit Application':
        window.close()
    if event == 'Ok':
        window.close()
        Upload_new_data_page()
# ------------------------------- UPLOAD CONFIRMATION PAGE END -------------------------------
# Invoking start script/function for user to begin the proccess of using the application.  
if __name__ == "__main__":
    # def function here
    login.login_main()
    pass