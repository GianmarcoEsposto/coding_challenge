import numpy as np
# Lista rappresentativa della configurazione dell'ufficio per la definizione di "moe_current_office"
lst_current_office = [
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", "C", " ", "M", "C", " ", "M"]
]

np_lst_current_office = np.array(lst_current_office)


import numpy as np
# Lista rappresentativa della configurazione dell'ufficio per la definizione di "moe_current_office"
lst_current_office = [
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "M", " ", " ", "M", " ", " ", "M"],
    ["A", "M", " ", "A", "M", " ", "A", "M"],
    [" ", "M", "C", " ", "M", "C", " ", "M"]
]




# Lista rappresentativa degli indici che identificano le posizioni di Ordirale all'interno della mappa
lst_index = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63]
]

np_lst_index = np.array(lst_index)




def update(int1,int2,lst_office):
    np_lst_office = np.array(lst_office)
    updarr=np.array([[int1+1,int2+2],[int1+1,int2-2],[int1+2,int2+1],[int1+2,int2-1],[int1-1,int2+2],[int1-1,int2-2],[int1-2,int2+1],[int1-2,int2-1]])
    new_upd=updarr.copy()
    for i in range(8):
       if (updarr[i,0]<0 or updarr[i,1]<0 or updarr[i,0]>7 or updarr[i,1]>7):
           new_upd[i]=0
       elif 0 <= updarr[i, 0] < 8 and 0 <= updarr[i, 1] < 8 :
           if np_lst_office[updarr[i,0],updarr[i,1]] == ' ':
               pass
           else:
               new_upd[i]=0

    #new_upd = new_upd[~np.all(new_upd == 0, axis=1)]
    valid_rows = [row for row in new_upd if not np.all(row == 0)]
    return np.array(valid_rows)  
    #return new_upd

def upd(array,lst_office):
    out=[]
    for i in range(len(array)): 
       out.append(update(array[i][0],array[i][1],lst_office))
    out_np = np.vstack(out)  # Use np.vstack to vertically stack arrays
    new_out = out_np.reshape(-1, 2)
    return new_out




def move_current_office(int_starting_position, int_end_position):
    np_lst_current_office = np.array(lst_current_office)
    result=0
    r0 = np.where(np_lst_index == int_starting_position)[0]
    c0 = np.where(np_lst_index == int_starting_position)[1]
    r1 = np.where(np_lst_index == int_end_position)[0]
    c1 = np.where(np_lst_index == int_end_position)[1]
    starting_position = np_lst_current_office[r0,c0]
    end_position = np_lst_current_office[r1,c1]
    if int_starting_position != int_end_position :
        if starting_position != ' ' or end_position != ' ' or int_starting_position >63 or int_end_position >63 or int_starting_position <0 or int_end_position <0 :
            return np.nan
        elif starting_position == ' ' and end_position == ' ':
            arr=update(r0,c0,lst_current_office)
            if len(arr) ==0:
                return np.inf
            else:  
                arr0=np.zeros(len(arr))
                arr0=np.copy(np_lst_index[arr[:,0],arr[:,1]])
                if np.isin(int_end_position,arr0):
                    result=1
                    return result
                else:
                    all_iterations_completed=True
                    for i in range(1,10):
                        arr=update(r0,c0,lst_current_office)
                        for j in range(1,i):
                            arr=upd(arr,lst_current_office)
                            arr0=np.zeros(len(arr))
                        arr0=np.copy(np_lst_index[arr[:,0],arr[:,1]])
                        if np.isin(int_end_position,arr0):
                            result=i
                            all_iterations_completed=False
                            break
                    if all_iterations_completed==False:       
                        return result    
                    else:    
                        return np.inf
    else:
        return 0    

def move_current_office_generalised(int_starting_position, int_end_position,lst_office):
    np_lst_office = np.array(lst_office)
    result=0
    r0 = np.where(np_lst_index == int_starting_position)[0]
    c0 = np.where(np_lst_index == int_starting_position)[1]
    r1 = np.where(np_lst_index == int_end_position)[0]
    c1 = np.where(np_lst_index == int_end_position)[1]
    starting_position = np_lst_office[r0,c0]
    end_position = np_lst_office[r1,c1]
    if int_starting_position != int_end_position :
        if starting_position != ' ' or end_position != ' ' or int_starting_position >63 or int_end_position >63 or int_starting_position <0 or int_end_position <0 :
            return np.nan
        elif starting_position == ' ' and end_position == ' ':
            arr=update(r0,c0,lst_office)
            if len(arr) ==0:
                return np.inf
            else:    
                arr0=np.zeros(len(arr))
                arr0=np.copy(np_lst_index[arr[:,0],arr[:,1]])
                if np.isin(int_end_position,arr0):
                    result=1
                    return result
                else:
                    all_iterations_completed=True
                    for i in range(1,10):
                        arr=update(r0,c0,lst_office)
                        for j in range(1,i):
                            arr=upd(arr,lst_office)
                            arr0=np.zeros(len(arr))
                        arr0=np.copy(np_lst_index[arr[:,0],arr[:,1]])
                        if np.isin(int_end_position,arr0):
                            result=i
                            all_iterations_completed=False
                            break
                    if all_iterations_completed==False:       
                        return result    
                    else:    
                        return np.inf
                    
    else:
        return 0    



def path(int_starting_position, int_end_position,p):
    np_lst_current_office = np.array(lst_current_office)
    r0 = np.where(np_lst_index == int_starting_position)[0]
    c0 = np.where(np_lst_index == int_starting_position)[1]
    r1 = np.where(np_lst_index == int_end_position)[0]
    c1 = np.where(np_lst_index == int_end_position)[1]
    starting_position = np_lst_current_office[r0,c0]
    end_position = np_lst_current_office[r1,c1]    
    if starting_position == ' ' and end_position == ' ':
        #n = move_current_office(int_starting_position, int_end_position)
        if p>1:
            steps=[]
            for i in range(1,p+1):
                arr = update(r0,c0,lst_current_office) 
                arr_np=np.copy(np_lst_index[arr[:,0],arr[:,1]])
                for j in range(len(arr_np)):
                    arr_el=arr_np[j]
                    if move_current_office(arr_np[j],int_end_position) == p-i:
                        steps.append(arr_el)
                        r0=np.where(np_lst_index == arr_np[j])[0]
                        c0=np.where(np_lst_index == arr_np[j])[1]
                        break
                print(f'Step {i} is {arr_el} ')         
                    
        elif p==1:
            print(f'Step 1 is {int_end_position} ')
        else:
            pass

def path_generalised(int_starting_position, int_end_position,lst_office,p):
    np_lst_office = np.array(lst_office)
    r0 = np.where(np_lst_index == int_starting_position)[0]
    c0 = np.where(np_lst_index == int_starting_position)[1]
    r1 = np.where(np_lst_index == int_end_position)[0]
    c1 = np.where(np_lst_index == int_end_position)[1]
    starting_position = np_lst_office[r0,c0]
    end_position = np_lst_office[r1,c1]    
    if starting_position == ' ' and end_position == ' ':
        #n = move_current_office(int_starting_position, int_end_position)
        if p>1:
            steps=[]
            for i in range(1,p+1):
                arr = update(r0,c0,lst_office) 
                arr_np=np.copy(np_lst_index[arr[:,0],arr[:,1]])
                for j in range(len(arr_np)):
                    arr_el=arr_np[j]
                    if move_current_office_generalised(arr_np[j],int_end_position,lst_office) == p-i:
                        steps.append(arr_el)
                        r0=np.where(np_lst_index == arr_np[j])[0]
                        c0=np.where(np_lst_index == arr_np[j])[1]
                        break
                print(f'Step {i} is {arr_el} ')         
                    
        elif p==1:
            print(f'Step 1 is {int_end_position} ')
        else:
            pass

