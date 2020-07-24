
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import filedialog, messagebox, font
from sklearn.model_selection import train_test_split
import time
import threading 
import pandas as pd
import Preprocessing as pr
import knn  as knn
import our_id3 as our_id3
import id3 as id3
'''
        _                 _   
       | |               | |  
   __ _| |__   ___  _   _| |_ 
  / _` | '_ \ / _ \| | | | __|
 | (_| | |_) | (_) | |_| | |_ 
  \__,_|_.__/ \___/ \__,_|\__|
                             
    wellcome to the gui module

        **************
        *  BEWARE!!  *
        **************
      All ye who enter here:
     Most of the code in this module
       is twisted beyond belief!
        Tread carefully.
     If you think you understand it,
         You Don't,
       So Look Again.

~@!THIS PROGRAM HAS CODE THAT DOES NOT MEET STANDARDS!@~

For the sins I am about to commit, may Guido van Rossum forgive me.
'''

# TODO start vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
'''
  __          __   
 / /____  ___/ /__ 
/ __/ _ \/ _  / _ \
\__/\___/\_,_/\___/
                   
to do list:
- import all needed modules
- replace foo function with the right function
- make sure function from imported modules some of the **kwargs. 
    supported keys/values:
    - 'test'     / test file (pandas df)
    - 'train'    / train file (pandas df)
    - 'structure'/ structure file (txt)
    - 'k'        / int
    - 'tolorance'/ copy of k
    - 'number_of_bins' / int
    - 'bin_type' / 'equal_width'/'equal_frequency'/'entropy'  StRiNG
    - 'missing_values' / 'remove_nans' or 'replace_nans'  String (dah...)
    - choosen_function / function from the modules

- make sure functions return dictionaries 
- delete temporary foo function
- all done? working well? now delete this comment
'''
################### delete me ######################################
#     ___                              my name is foo              # 
#   / _/__    ___                                                  # 
#  / _/ _  \/ _  \       i am a place holder                       # 
# /_/ \___/ \___/          antil replaced by modules               # 
def foo (**kwargs):                                                # 
    print(kwargs)                                                  # 
    time.sleep(2)                                                  # 
    return { 'score':100 , 'TP':100 , 'TN':200 ,'FP':10 ,'FN':20 } #
####################################################################

#     __                                           _       _           
#    / _|                                         | |     | |          
#   | |_ _ __ ___  _ __ ___    _ __ ___   ___   __| |_   _| | ___  ___ 
#   |  _| '__/ _ \| '_ ` _ \  | '_ ` _ \ / _ \ / _` | | | | |/ _ \/ __|
#   | | | | | (_) | | | | | | | | | | | | (_) | (_| | |_| | |  __/\__ \
#   |_| |_|  \___/|_| |_| |_| |_| |_| |_|\___/ \__,_|\__,_|_|\___||___/
#                                                                      
# (from modules)                                                                  
OUR_ID3         = our_id3.our_id3_adapter
ID3             = id3.id3_adapret
OUR_NAIVE_BAYES = foo
NAIVE_BAYES     = foo
K_NN            = knn.run 
K_MEANS         = foo
PREPROCESS      = pr.Preprocessing_adapter
# TODO end ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def execute_update_kwargs( function , **kwargs):
    return {**kwargs,**function(**kwargs)} # old kwags are updated by the returen dict from  the function

#     __                  _   _                 
#    / _|                | | (_)                
#   | |_ _   _ _ __   ___| |_ _  ___  _ __  ___ 
#   |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#   | | | |_| | | | | (__| |_| | (_) | | | \__ \
#   |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
# (functions)                                              
# i just composed some of the functions with the preprocessor for future simpler calls...
functions = {
    'our_id3'        : lambda **kwargs: OUR_ID3(**execute_update_kwargs(PREPROCESS, **kwargs)),
    'id3'            : lambda **kwargs: ID3(**execute_update_kwargs(PREPROCESS, **kwargs)),
    'naive_bayes'    : lambda **kwargs: OUR_NAIVE_BAYES(**execute_update_kwargs(PREPROCESS, **kwargs)),
    'our_naive_bayes': lambda **kwargs: NAIVE_BAYES(**execute_update_kwargs(PREPROCESS, **kwargs)),
    # knn/ kmeans has its own preprossesing
    'knn'            : lambda **kwargs: K_NN(**kwargs),  
    'k_means'        : lambda **kwargs: K_MEANS(**kwargs)
}

#                                                
#                                                
#    _ __ ___  ___  ___  _   _ _ __ ___ ___  ___ 
#   | '__/ _ \/ __|/ _ \| | | | '__/ __/ _ \/ __|
#   | | |  __/\__ \ (_) | |_| | | | (_|  __/\__ \
#   |_|  \___||___/\___/ \__,_|_|  \___\___||___/
#                                                
#  (resources)                                              
def getResources():
    resources ={ 
        "main":{
            "background"     :{'image':ImageTk.PhotoImage(Image.open("res/main/back.png")),
                               'location':(0,0) },
            "prepro_frames"  : {'images':[PhotoImage(file='res/main/prepro.gif',format = 'gif -index %i' %(i)) for i in range(4)],
                               'location':(60,20) },
            "classif_frames" :{'images': [PhotoImage(file='res/main/classif.gif',format = 'gif -index %i' %(i)) for i in range(4)],
                               'location':(365,20) },
            "run_frames"     :{'images': [PhotoImage(file='res/main/run.gif',format = 'gif -index %i' %(i)) for i in range(4)],
                               'location':(670,20) },
            },
        "prepro":{
            "background"           : {'image':ImageTk.PhotoImage(Image.open("res/prepro/prepropanel.png")),
                                      'location':(160,320) },
            "equal_width_down"     : {'image':ImageTk.PhotoImage(Image.open("res/prepro/btn1down.png")),
                                      'location':(242,43) },
            "equal_width_up"       : {'image':ImageTk.PhotoImage(Image.open("res/prepro/btn1up.png")),
                                      'location':(242,43) },
            "equal_frequency_down" : {'image':ImageTk.PhotoImage(Image.open("res/prepro/btn2down.png")),
                                      'location':(384,43) },
            "equal_frequency_up"   : {'image':ImageTk.PhotoImage(Image.open("res/prepro/btn2up.png")),
                                      'location':(384,43) },
            "entropy_down"         : {'image':ImageTk.PhotoImage(Image.open("res/prepro/btn3down.png")),
                                      'location':(529,43) },
            "entropy_up"           : {'image':ImageTk.PhotoImage(Image.open("res/prepro/btn3up.png")),
                                      'location':(529,43) },
            "load_structure"       : {'image':ImageTk.PhotoImage(Image.open("res/prepro/loadstructure.png")),
                                      'location':(500,323) },
            "load_train"           : {'image':ImageTk.PhotoImage(Image.open("res/prepro/loadtrain.png")),
                                      'location':(200,320) },
            "load_test"            : {'image':ImageTk.PhotoImage(Image.open("res/prepro/loadtest.png")),
                                      'location':(347,321) },
            "remove_nans"          : {'image':ImageTk.PhotoImage(Image.open("res/prepro/removenans.png")),
                                      'location':(385,245) },
            "replace_nans"         : {'image':ImageTk.PhotoImage(Image.open("res/prepro/replacenans.png")),
                                      'location':(385,245) },
            "8020_on"              : {'image':ImageTk.PhotoImage(Image.open("res/prepro/8020u.png")),
                                      'location':(225,287) },
            "8020_off"             : {'image':ImageTk.PhotoImage(Image.open("res/prepro/8020d.png")),
                                      'location':(225,287) },
            }, 
        "classif":{
            "background"           :{'image':ImageTk.PhotoImage(Image.open("res/classif/classifpanel.png")),
                                     'location':(5,290) },
            "our_naive_bayes_up"   :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn1u.png")),
                                     'location':(106,48) },
            "our_naive_bayes_down" :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn1d.png")),
                                     'location':(106,48) },
            "our_id3_up"           :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn2u.png")),
                                     'location':(330,48) },
            "our_id3_down"         :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn2d.png")),
                                     'location':(330,48) },
            "naive_bayes_up"       :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn3u.png")),
                                     'location':(107,256) },
            "naive_bayes_down"     :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn3d.png")),
                                     'location':(107,256) },
            "id3_up"               :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn4u.png")),
                                     'location':(330,259) },
            "id3_down"             :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn4d.png")),
                                     'location':(330,259) },
            "knn_up"               :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn5u.png")),
                                     'location':(552,259) },
            "knn_down"             :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn5d.png")),
                                     'location':(552,259) },
            "k_means_up"           :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn6u.png")),
                                     'location':(771,259) },
            "k_means_down"         :{'image':ImageTk.PhotoImage(Image.open("res/classif/btn6d.png")),
                                     'location':(771,259) },
            }, 
        "run":{
            "background" :{'image':ImageTk.PhotoImage(Image.open("res/run/runPanel.png")),
                           'location':(35,300) },
            "start"      :{'image':ImageTk.PhotoImage(Image.open("res/run/startbtn.png")),
                           'location':(406,149) },
            "save"      :{'image':ImageTk.PhotoImage(Image.open("res/run/savebtn.png")),
                           'location':(83,159) },
            },
        "extra":{
            "slideball" :{'image':ImageTk.PhotoImage(Image.open("res/others/sliderball.png"))},
            "slidebr"   :{'image': ImageTk.PhotoImage(Image.open("res/others/sliderbr.png"))}
            }
        }
    return resources


'''
 Abandon all hope ye who enter beyond this point

      .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................    
'''
#                           _ _      _   
#                          | (_)    | |  
#     __ _ _ __ __ _     __| |_  ___| |_ 
#    / _` | '__/ _` |   / _` | |/ __| __|
#   | (_| | | | (_| |  | (_| | | (__| |_ 
#    \__,_|_|  \__, |   \__,_|_|\___|\__|
#               __/ |_____               
#              |___/______|     
# (arg dict)
arg_dict = { 'test':None,
             'train':None,
             'structure':None,
             'number_of_bins':None,
             'k':None,
             'tolorance':None,
             'bin_type':None,
             'missing_values': 'remove_nans',  # removing nans by default
             'choosen_function':None,
             'choosen_function_name':None,
             '8020':None
    }

#                           _       _ _      _   
#                          | |     | (_)    | |  
#    _ __   __ _ _ __   ___| |   __| |_  ___| |_ 
#   | '_ \ / _` | '_ \ / _ \ |  / _` | |/ __| __|
#   | |_) | (_| | | | |  __/ | | (_| | | (__| |_ 
#   | .__/ \__,_|_| |_|\___|_|  \__,_|_|\___|\__|
#   | |                                          
#   |_|                                          
# (panel dict)
panel_dict = {
        'prepro':None,
        'classif':None,
        'run':None,
    }

panel_location_and_size = {
    'prepro': {'location': (160, 320),
               'size': (670, 400)},
    'classif': {'location': (5, 290),
                'size': (1010, 470)},
    'run': {'location': (35, 300),
            'size': (965, 450)},
}

#    _           _   _                  
#   | |         | | | |                 
#   | |__  _   _| |_| |_ ___  _ __  ___ 
#   | '_ \| | | | __| __/ _ \| '_ \/ __|
#   | |_) | |_| | |_| || (_) | | | \__ \
#   |_.__/ \__,_|\__|\__\___/|_| |_|___/
# (buttons)                                      
button_actions = {
        "main":{
            'prepro'   : lambda  e: togglePanleVisability(panel_dict['prepro'],*panel_location_and_size['prepro']['location']),
            'classif'  : lambda  e: togglePanleVisability(panel_dict['classif'],*panel_location_and_size['classif']['location']),
            'run'      : lambda  e: togglePanleVisability(panel_dict['run'],*panel_location_and_size['run']['location']),
        },
        "prepro":{
            'load_train'     : lambda e: openDf('train'),
            'load_test'      : lambda e: openDf('test'),
            'load_structure' : lambda e: load_structure(),
            'missing_values' : lambda  : toggle_missing_values(),
            'equal_width'    : lambda  : toggle_bin_type('equal_width'),
            'equal_frequency': lambda  : toggle_bin_type('equal_frequency'),
            'entropy'        : lambda  : toggle_bin_type('entropy'),
            '8020'           : lambda  : toggle_8020(),
        },
        "classif":{
            'our_naive_bayes': lambda  : toggle_choosen_function(functions['our_naive_bayes'],'our_naive_bayes'),
            'naive_bayes'    : lambda  : toggle_choosen_function(functions['naive_bayes'],'naive_bayes'),
            'our_id3'        : lambda  : toggle_choosen_function(functions['our_id3'],'our_id3'),
            'id3'            : lambda  : toggle_choosen_function(functions['id3'],'id3'),
            'knn'            : lambda  : toggle_choosen_function(functions['knn'],'knn'),
            'k_means'        : lambda  : toggle_choosen_function(functions['k_means'],'k_means'),
        }, 
        "run":{
            'start' : '( function for the start button composed down in the run panel )',
            'save'  : lambda e : save_to_file(arg_dict,output_components)
        },
    }
def reformat_file_rout( string):
    total_path = string.split('/')
    return total_path[len(total_path) - 1]

def openDf( x ): # x can be 'test' or 'train'
    filename = filedialog.askopenfilename(filetypes=(("CSV Files", "*.csv"),))
    try:
        arg_dict[x] = pd.read_csv(filename)
    except FileNotFoundError as e:
        messagebox.showerror("Error", "file was not found!!")


def load_structure():
    arg_dict['structure'] = []
    filename = filedialog.askopenfilename(filetypes=(("TXT Files", "*.txt"),))
    try:
        tmp = open(filename, "r")
        for line in tmp:
            arg_dict['structure'].append(line)
        tmp.close()
    except FileNotFoundError as e:
        messagebox.showerror("Error", 'file not found')

def set_all_panels_in_main_visability_off():
    panel_dict['prepro'].place_forget()
    panel_dict['classif'].place_forget()
    panel_dict['run'].place_forget()

def togglePanleVisability(panel,x,y):
    if(panel.winfo_viewable()):
        panel.place_forget()
    else:
        set_all_panels_in_main_visability_off()
        panel.place(x=x,y=y)

def toggle_missing_values():
    if(arg_dict['missing_values'] == 'remove_nans'):
        arg_dict['missing_values'] = 'replace_nans'
    else:
        arg_dict['missing_values'] = 'remove_nans'

def toggle_bin_type(bin_type):
    if(arg_dict['bin_type'] == bin_type):
        arg_dict['bin_type'] = None
    else:
        arg_dict['bin_type'] = bin_type

def toggle_choosen_function(function,function_name):
    if(arg_dict['choosen_function'] == function):
        arg_dict['choosen_function'] = None
        arg_dict['choosen_function_name'] = None
    else:
        arg_dict['choosen_function'] = function
        arg_dict['choosen_function_name'] = function_name

def save_to_file(arg_dict,output_components):
    classifayer = arg_dict['choosen_function_name']
    setup = 'bins={0} ,k/tolorance={1}'.format(arg_dict['number_of_bins'], arg_dict['k'])
    nans = 'dealing with missing by:' + arg_dict['missing_values'] 
    score =  'score=({})'.format(output_components['score_box']['text']) # output_components defined at the run pannel
    matrix = 'maxtix=(({0},{1}),({2},{3}))'.format(output_components['TN_box']['text'],
                                            output_components['FP_box']['text'],
                                            output_components['FN_box']['text'],
                                            output_components['TP_box']['text'])
    if(None not in (classifayer,setup,nans,score,matrix )):
        line = classifayer +', '+setup+', '+nans+', '+score+', '+matrix+'\n'
        with open('Log_File.txt', 'a') as file:
            file.write(line)
        output_components['satus_box'].config(text = 'Saved')
    else:
        output_components['satus_box'].config(text = 'Nothing to save')

def pass_kwargs(**kwargs):
    return kwargs

def split_8020(**kwargs):

    df = kwargs['train']
    # train = df.sample(frac=0.8,random_state=200) #random state is a seed value
    # test = df.drop(train.index)
    train, test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
    
    train.dropna(inplace=True)
    test.dropna(inplace=True)

    return {**kwargs,**{'train':train, 'test': test }}

def toggle_8020():
    if(arg_dict['8020'] == pass_kwargs):
        arg_dict['8020'] = split_8020
    else:
        arg_dict['8020'] = pass_kwargs


def create_button(perent, location, image ,function ,enter_color="#2b2d42" ,leave_color="gray", bg_color="gray"):
    def on_enter(e):
        btn['activebackground'] = enter_color
    def on_leave(e):
        btn['background'] = leave_color
    btn = Button(perent, image=image, borderwidth=0, highlightthickness=0, bd=0, bg=bg_color)
    (x, y) = location
    btn.bind("<Button-1>", function)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.place(x=x, y=y)
    return btn

def create_lever_button(perent, down_img, up_img, location, function, set_other_down, enter_color="#2b2d42" ,leave_color="gray", bg_color="gray"):
    def onClick(e):
        if(e.widget.cget('image') == down_img):
            set_other_down()
            img = up_img
        else:
            img = down_img
        btn.configure(image=img)
        function()
    btn = Button(perent, image=up_img, borderwidth=0, highlightthickness=0, bd=0, bg=bg_color, relief=SUNKEN)
    up_img = btn.cget('image')  # for some reason image change itself after loading, this is why i load and save
    btn.configure(image=down_img) # and load
    down_img = btn.cget('image') # and save
    btn.config(activebackground=btn.cget('background'))
    (x, y) = location
    btn.bind("<Button-1>", onClick)
    btn.bind("<Enter>", lambda e:None)
    btn.bind("<Leave>", lambda e:None)
    btn.place(x=x, y=y)
    return btn


#                       _ _           
#                      | | |          
#    ___  ___ _ __ ___ | | | ___ _ __ 
#   / __|/ __| '__/ _ \| | |/ _ \ '__|
#   \__ \ (__| | | (_) | | |  __/ |   
#   |___/\___|_|  \___/|_|_|\___|_|   
#                                     
#                                     
# I copied it from stackoverflow and wraped it inside function and made is update arg_dict
def make_scaler(perent,location,from_ ,to_, args_dict_keys):
    class CustomScale(ttk.Scale):
        def __init__(self, master=None, **kw):
            self.variable = kw.pop('variable', IntVar(master))
            ttk.Scale.__init__(self, master, orient='vertical', variable=self.variable, **kw)
            self._style_name = '{}.custom.Vertical.TScale'.format(self) # unique style name to handle the text
            self['style'] = self._style_name
            self.variable.trace_add('write', self._update)
            self.set(from_)
            self._update()
        
        def _update(self, *args):
            style.configure(self._style_name, text="{}".format(self.variable.get()))
            for key in args_dict_keys:
                arg_dict[key]= self.variable.get()
    scale = CustomScale(perent, from_=from_, to=to_)
    (x,y) = location
    scale.place(x=x,y=y)
    return scale

# need to call this function onces so scroller will look nice
def set_scroller_style(root,resources):
    style = ttk.Style(root)
    # create scale elements
    style.element_create('custom.Vertical.Scale.trough', 'image', resources['extra']['slidebr']['image'])
    style.element_create('custom.Vertical.Scale.slider', 'image',resources['extra']['slideball']['image'] )
    # create custom layout
    style.layout('custom.Vertical.TScale',
                    [('custom.Vertical.Scale.trough', {'sticky': 'ns'}),
                    ('custom.Vertical.Scale.slider',{'side': 'top', 'sticky': '',
                    'children': [('custom.Vertical.Scale.label', {'sticky': ''})]
                    })])
    style.configure('custom.Vertical.TScale',background='#de1700', foreground='black' )
    style.map("custom.Vertical.TScale",
        foreground = [('active','#de1700')],
        background=[ ('active', '#de1700')]
        )
    return style


#                    _                  _           _               
#                   (_)                (_)         | |              
#    _ __ ___   __ _ _ _ __   __      ___ _ __   __| | _____      __
#   | '_ ` _ \ / _` | | '_ \  \ \ /\ / / | '_ \ / _` |/ _ \ \ /\ / /
#   | | | | | | (_| | | | | |  \ V  V /| | | | | (_| | (_) \ V  V / 
#   |_| |_| |_|\__,_|_|_| |_|   \_/\_/ |_|_| |_|\__,_|\___/ \_/\_/  
#                                                                   
#  (main window)
def create_main_window(root,resources):
    main_window = Canvas(root, width=1024, height=768)
    main_window.create_image(0,0,anchor=NW ,image=resources['main']['background']['image'])
    main_window.pack()

    button = create_button(main_window, resources['main']['prepro_frames']['location'],
                           resources['main']['prepro_frames']['images'][0], button_actions['main']['prepro'])

    button1 = create_button(main_window, resources['main']['classif_frames']['location'],
                           resources['main']['classif_frames']['images'][0], button_actions['main']['classif'])

    button2 = create_button(main_window, resources['main']['run_frames']['location'],
                           resources['main']['run_frames']['images'][0], button_actions['main']['run'])

    def makeGifMove(ind): # copied from stack and added some modification
        frame = resources['main']['prepro_frames']['images'][ind]
        frame1 = resources['main']['classif_frames']['images'][ind]
        frame2 = resources['main']['run_frames']['images'][ind]
        ind = (1 + ind) % 4 
        button.configure(image=frame)
        button1.configure(image=frame1)
        button2.configure(image=frame2)
        root.after(100, makeGifMove, ind) # I don't know why. Just move on.
    root.after(0, makeGifMove, 0) # I don't know why. Just move on.

    return main_window


#    _____                                                                     _ 
#   |  __ \                                                                   | |
#   | |__) | __ ___ _ __  _ __ ___   ___ ___  ___ ___   _ __   __ _ _ __   ___| |
#   |  ___/ '__/ _ \ '_ \| '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` | '_ \ / _ \ |
#   | |   | | |  __/ |_) | | | (_) | (_|  __/\__ \__ \ | |_) | (_| | | | |  __/ |
#   |_|   |_|  \___| .__/|_|  \___/ \___\___||___/___/ | .__/ \__,_|_| |_|\___|_|
#                  | |                                 | |                       
#                  |_|                                 |_|                       
# (Preprocess panel)
def create_prepro_panel(parent, resources):
    (width,height) = panel_location_and_size['prepro']['size']
    prepro_panel = Canvas(parent, width=width, height=height,
                          borderwidth=0, highlightthickness=0, bd=0, bg="black")
    prepro_panel.create_image(0,0,anchor=NW ,image=resources['prepro']['background']['image'])

    # load train
    create_button(prepro_panel, resources['prepro']['load_train']['location'],
                  resources['prepro']['load_train']['image'], button_actions['prepro']['load_train'])

    # load test
    create_button(prepro_panel, resources['prepro']['load_test']['location'],
                  resources['prepro']['load_test']['image'], button_actions['prepro']['load_test'])

    # load structure
    create_button(prepro_panel, resources['prepro']['load_structure']['location'],
                  resources['prepro']['load_structure']['image'], button_actions['prepro']['load_structure'])

    # deal with not a numbers toggle button
    create_lever_button(prepro_panel,
                         resources['prepro']['remove_nans']['image'],
                         resources['prepro']['replace_nans']['image'],
                         resources['prepro']['remove_nans']['location'],
                         button_actions['prepro']['missing_values'],
                         lambda: None)

    # 80 / 20 button
    arg_dict['8020'] = pass_kwargs
    create_lever_button(prepro_panel,
                         resources['prepro']['8020_off']['image'],
                         resources['prepro']['8020_on']['image'],
                         resources['prepro']['8020_off']['location'],
                         button_actions['prepro']['8020'],
                         lambda: None)

    conected_lever_buttons = []
    def turn_buttons_down():
        conected_lever_buttons[0].configure(image=resources['prepro']['equal_width_down']['image'])
        conected_lever_buttons[1].configure(image=resources['prepro']['equal_frequency_down']['image'])
        conected_lever_buttons[2].configure(image=resources['prepro']['entropy_down']['image'])
    # equal width
    conected_lever_buttons.append(
        create_lever_button(prepro_panel,
                         resources['prepro']['equal_width_down']['image'],
                         resources['prepro']['equal_width_up']['image'],
                         resources['prepro']['equal_width_down']['location'],
                         button_actions['prepro']['equal_width'],
                         turn_buttons_down))
    # equal frequency
    conected_lever_buttons.append(
        create_lever_button(prepro_panel,
                         resources['prepro']['equal_frequency_down']['image'],
                         resources['prepro']['equal_frequency_up']['image'],
                         resources['prepro']['equal_frequency_down']['location'],
                         button_actions['prepro']['equal_frequency'],
                         turn_buttons_down))
    # entropy
    conected_lever_buttons.append(
        create_lever_button(prepro_panel,
                         resources['prepro']['entropy_down']['image'],
                         resources['prepro']['entropy_up']['image'],
                         resources['prepro']['entropy_down']['location'],
                         button_actions['prepro']['entropy'],
                         turn_buttons_down))
    # bins scroller
    make_scaler(prepro_panel, (43,60), 2, 10,('number_of_bins',) )

    prepro_panel.place_forget()
    return prepro_panel



#         _               _  __ _           _   _                                      _ 
#        | |             (_)/ _(_)         | | (_)                                    | |
#     ___| | __ _ ___ ___ _| |_ _  ___ __ _| |_ _  ___  _ __    _ __   __ _ _ __   ___| |
#    / __| |/ _` / __/ __| |  _| |/ __/ _` | __| |/ _ \| '_ \  | '_ \ / _` | '_ \ / _ \ |
#   | (__| | (_| \__ \__ \ | | | | (_| (_| | |_| | (_) | | | | | |_) | (_| | | | |  __/ |
#    \___|_|\__,_|___/___/_|_| |_|\___\__,_|\__|_|\___/|_| |_| | .__/ \__,_|_| |_|\___|_|
#                                                              | |                       
#                                                              |_|                       
# (classification panel)
def create_classif_panel(parent, resources):
    (width,height) = panel_location_and_size['classif']['size']
    classif_panel= Canvas(parent, width=width, height=height,
                          borderwidth=0, highlightthickness=0, bd=0, bg="black")
    classif_panel.create_image(0,0,anchor=NW ,image=resources['classif']['background']['image'])

    conected_lever_buttons = []
    def turn_buttons_down():
        conected_lever_buttons[0].configure(image=resources['classif']['our_naive_bayes_down']['image'])
        conected_lever_buttons[1].configure(image=resources['classif']['our_id3_down']['image'])
        conected_lever_buttons[2].configure(image=resources['classif']['naive_bayes_down']['image'])
        conected_lever_buttons[3].configure(image=resources['classif']['id3_down']['image'])
        conected_lever_buttons[4].configure(image=resources['classif']['knn_down']['image'])
        conected_lever_buttons[5].configure(image=resources['classif']['k_means_down']['image'])
    # our naive bayes 
    conected_lever_buttons.append(
        create_lever_button(classif_panel,
                         resources['classif']['our_naive_bayes_down']['image'],
                         resources['classif']['our_naive_bayes_up']['image'],
                         resources['classif']['our_naive_bayes_up']['location'],
                         button_actions['classif']['our_naive_bayes'],
                         turn_buttons_down))
    # our id3
    conected_lever_buttons.append(
        create_lever_button(classif_panel,
                         resources['classif']['our_id3_down']['image'],
                         resources['classif']['our_id3_up']['image'],
                         resources['classif']['our_id3_down']['location'],
                         button_actions['classif']['our_id3'],
                         turn_buttons_down))
    # naive bayes
    conected_lever_buttons.append(
        create_lever_button(classif_panel,
                         resources['classif']['naive_bayes_down']['image'],
                         resources['classif']['naive_bayes_up']['image'],
                         resources['classif']['naive_bayes_down']['location'],
                         button_actions['classif']['naive_bayes'],
                         turn_buttons_down))
    # id3
    conected_lever_buttons.append(
        create_lever_button(classif_panel,
                         resources['classif']['id3_down']['image'],
                         resources['classif']['id3_up']['image'],
                         resources['classif']['id3_down']['location'],
                         button_actions['classif']['id3'],
                         turn_buttons_down))
    # knn
    conected_lever_buttons.append(
        create_lever_button(classif_panel,
                         resources['classif']['knn_down']['image'],
                         resources['classif']['knn_up']['image'],
                         resources['classif']['knn_down']['location'],
                         button_actions['classif']['knn'],
                         turn_buttons_down))
    # k means
    conected_lever_buttons.append(
        create_lever_button(classif_panel,
                         resources['classif']['k_means_down']['image'],
                         resources['classif']['k_means_up']['image'],
                         resources['classif']['k_means_down']['location'],
                         button_actions['classif']['k_means'],
                         turn_buttons_down))
    # k/tolorance scroller
    make_scaler(classif_panel, (24,100), 0, 100,('k','tolorance') )
    return classif_panel



#                                              _ 
#                                             | |
#    _ __ _   _ _ __    _ __   __ _ _ __   ___| |
#   | '__| | | | '_ \  | '_ \ / _` | '_ \ / _ \ |
#   | |  | |_| | | | | | |_) | (_| | | | |  __/ |
#   |_|   \__,_|_| |_| | .__/ \__,_|_| |_|\___|_|
#                      | |                       
#                      |_|                       
# (run panel)

# Otuput components:
# (didnt found better solotion for, this is why i make it global)
output_components = {
    'status_box':None,
    'score_box':None,
    'TP_box':None,
    'TN_box':None,
    'FP_box':None,
    'FN_box':None,
}

def create_run_panel(parent, resources):
    (width,height) = panel_location_and_size['run']['size']
    run_panel= Canvas(parent, width=width, height=height,
                          borderwidth=0, highlightthickness=0, bd=0, bg="black")
    run_panel.create_image(0,0,anchor=NW ,image=resources['run']['background']['image'])

    # status box
    output_components['satus_box'] = Label(run_panel,text= "Not Loaded")
    output_components['satus_box'].config(font=('Helvetica',20,'bold'))
    output_components['satus_box'].config( bg="black")
    output_components['satus_box'].config( fg="red")
    output_components['satus_box'].place(x=350,y=65)
    def setStatus(string):
        output_components['satus_box'].config(text = string)

    # score box
    output_components['score_box']= Label(run_panel,text= "00.00")
    output_components['score_box'].config(font=('Helvetica',20,'bold'))
    output_components['score_box'].config( bg="black")
    output_components['score_box'].config( fg="#aacc00")
    output_components['score_box'].place(x=440,y=365)
    def setScore( score):
        if( score < 10):
            string = '0{:.2f}'.format(score)
        else:
            string = '{:.2f}'.format(score)
        output_components['score_box'].config(text = string)

    # True positive 
    output_components['TP_box'] = Label(run_panel,text= "TP")
    output_components['TP_box'].config(font=('Helvetica',20,'bold'))
    output_components['TP_box'].config( bg="#dd1c1a")
    output_components['TP_box'].config( fg="#000000")
    output_components['TP_box'].place(x=834,y=255)

    # True negative box
    output_components['TN_box'] = Label(run_panel,text= "TN")
    output_components['TN_box'].config(font=('Helvetica',20,'bold'))
    output_components['TN_box'].config( bg="#f0c808")
    output_components['TN_box'].config( fg="#000000")
    output_components['TN_box'].place(x=717,y=189)

    # False positive box
    output_components['FP_box'] = Label(run_panel,text= "FP")
    output_components['FP_box'].config(font=('Helvetica',20,'bold'))
    output_components['FP_box'].config( bg="#086788")
    output_components['FP_box'].config( fg="#000000")
    output_components['FP_box'].place(x=834,y=189)

    # False negative box
    output_components['FN_box'] = Label(run_panel,text= "FN")
    output_components['FN_box'].config(font=('Helvetica',20,'bold'))
    output_components['FN_box'].config( bg="#06aed5")
    output_components['FN_box'].config( fg="#000000")
    output_components['FN_box'].place(x=717,y=255)


    def F_D_L_S(): # Fault Detection Location System
        if(not isinstance(arg_dict['train'], pd.DataFrame)):
            setStatus('Load train')
        elif(not isinstance(arg_dict['test'], pd.DataFrame)
            and arg_dict['8020'] == pass_kwargs):
            setStatus('Load test')
        elif(arg_dict['structure'] == None ):
            setStatus('Load structure')
        elif(arg_dict['number_of_bins'] < 0):
            setStatus('Bins error')
        elif(arg_dict['k'] != arg_dict['tolorance'] or arg_dict['k'] < 0):
            setStatus('Tolorance / k error')
        elif(arg_dict['bin_type'] is None):
            setStatus('Choose bin type')
        elif(arg_dict['missing_values'] is None):
            setStatus('Missing values error')
        elif(arg_dict['choosen_function'] is None):
            setStatus('Choose classifier')
        else:
            setStatus('fdls go')

    def update_output(**kwargs):
        setStatus('Working...')
        function = kwargs['choosen_function']
        result = function(**kwargs['8020'](**kwargs))
        setScore(result['score'])
        output_components['TP_box'].config(text = result['TP'])
        output_components['TN_box'].config(text = result['TN'])
        output_components['FP_box'].config(text = result['FP'])
        output_components['FN_box'].config(text = result['FN'])
        setStatus('Done')

    def start(e):
        F_D_L_S()
        if(output_components['satus_box']['text'] == 'fdls go'):
            # creating kwargs - making clone of test,train,structure
            kwargs = {**arg_dict, **{'train': arg_dict['train'].copy(deep=True)
                                    , 'structure': [x for x in list(arg_dict['structure'])]}
                      }
            if(arg_dict['8020'] == pass_kwargs):
                kwargs = {**kwargs , **{'test':arg_dict['test'].copy(deep=True)}}
            threading.Thread(target=update_output, kwargs=kwargs).start()

    # start button
    create_button(run_panel, resources['run']['start']['location'],
                    resources['run']['start']['image'],start ,'black','black','black')

    # save button
    create_button(run_panel, resources['run']['save']['location'],
                    resources['run']['save']['image'],button_actions['run']['save'] ,'#c0176c','#c0176c','#c0176c')
    return run_panel

#                _   _   _                     _ _   _                    _   _               
#               | | | | (_)                   | | | | |                  | | | |              
#    _ __  _   _| |_| |_ _ _ __   __ _    __ _| | | | |_ _   _  __ _  ___| |_| |__   ___ _ __ 
#   | '_ \| | | | __| __| | '_ \ / _` |  / _` | | | | __| | | |/ _` |/ _ \ __| '_ \ / _ \ '__|
#   | |_) | |_| | |_| |_| | | | | (_| | | (_| | | | | |_| |_| | (_| |  __/ |_| | | |  __/ |   
#   | .__/ \__,_|\__|\__|_|_| |_|\__, |  \__,_|_|_|  \__|\__,_|\__, |\___|\__|_| |_|\___|_|   
#   | |                           __/ |                         __/ |                         
#   |_|                          |___/                         |___/                          
# (putting all tugether)
root = Tk()
root.title("oogabooga")
root.resizable(False, False)
resources = getResources()
style = set_scroller_style(root,resources) # for the scrollers to work
main_window = create_main_window(root,resources)
panel_dict['prepro'] = create_prepro_panel(main_window, resources)
panel_dict['classif'] = create_classif_panel(main_window, resources)
panel_dict['run'] = create_run_panel(main_window, resources)
root.mainloop()

#    finito
# ＼ ( ᐛ ) /
# 
