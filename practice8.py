import time
import sys
from datetime import datetime

def main():
    UserInputs("users_database.txt")

def UserInputs(file):
    print("Wellcome to noteHuk...\n press number to add/remove/update/see\n Add -- [press 1],\n Watch -- [press 2],\n Update -- [press 3] and\n Delete -- [press 4]\n Show last note -- [press 5]\n Show first one -- [press 6],\n show new all notes -- (press 7)\n read delete history -- (press 8)\n")
    input_userExp = 0
    while True:
        input_userExp = int(input("Press 1/2/3/4/... ? "))
        if input_userExp <= 8 and input_userExp > 0:
            break
        # IF NOT ERR
    __HANDLE_INPUT_PROMPT(input_userExp, file) 

def __HANDLE_INPUT_PROMPT(input_n, working_file):
        if input_n == 1:
             __ADD(working_file)
        elif input_n == 2:
             print("\n------ Your all notes ------\n")
             __READ(working_file,0, "all")
             open_note(working_file)
        elif input_n == 3:
             
             check_arr = __CHECK_HAS_NOTE(working_file)
             if check_arr[2] == 0:
                  print(f"\n{check_arr[0]}")
                  print("----")
                  while True:
                    print(f"create new note (press {check_arr[1]}) or quit (press 0)?")
                    input_code = get_int()
                    if input_code == 1:
                       __HANDLE_INPUT_PROMPT(input_code, working_file)
                       return
                    elif input_code == 0:
                       sys.exit()
             __USER_FILE_DATA = []
             with open(working_file, "r") as read_data_file:
               for read in read_data_file:
                    __USER_FILE_DATA.append(read.split(" |-13-@3*3code(013.1-qpd__)| "))
               update_code = int(input(f"You have {len(__USER_FILE_DATA)} notes, update to press note id? "))
               mode__ = int(input("update title (press 0) or update note (press 1) or if you change to title and note so (press 2) ? "))
               if len(__USER_FILE_DATA) > 0:
                    if mode__ >= 0 and mode__ < 4:
                         __list_arr = input_notes_part(mode__)
                         __UPDATE_FILE(working_file, update_code, __list_arr, mode__)
               else: print("Id is not found !")
        elif input_n == 4:
             delete_code = int(input("Enter the delete id? "))
             __DELETE_FILE_CONTENT(working_file, delete_code)
        elif input_n == 5:
             __READ(working_file,0, "last")
        elif input_n == 6:
             __READ(working_file,0, "first")
        elif input_n == 7:
             __READ(working_file,0, "new")
        elif input_n == 8:
             delete_history()
        else:
             print("Wrong input type !")
def delete_history():
     history = __GET_HISTORY()
     if len(history) < 1:
          print("Empty delete history!")
          return
     print("---- Your deleted notes ----\n")
     __READ("delete_history.txt", 0, "all")
def open_spacific_note(id):
     __READ("users_database.txt", id, "single")

def input_notes_part(__mode):
     if __mode == 0:
          return [str(input("Enter update title: "))]
     elif __mode == 1:
          return [str(input("Enter update note: "))]
     elif __mode == 3:
          x = input_notes_part(0)
          y = input_notes_part(1)
          return [x[0],y[0]]
             
def __WRITE_FILE(filename, write):
     if filename:
          with open(filename, "a+") as write_file:
               write_file.write(write)
def __CHECK_HAS_NOTE(file):
     read__ = __READ_FILE_CONTENT_TO_LIST(file)   
     if len(read__) < 1:
          print(read__)
          return ["Empty notes !", 1, 0]   
     else:
          return ["", 0, 1]     
               
def __READ_FILE(filename):
     read_database = []
     with open(filename, "r") as read_file:
          for r in read_file:
            read_database.append(r.rstrip())
     return read_database

def __UPDATE_FILE(filename, update_id, update__list, mode__):
     __read_file__ = __READ_FILE_CONTENT_TO_LIST(filename)
     # __READ_FILE_WITH_SPLIT_CODE = __READ_FILE()
     __READY_FOR_UP = []
     __is_found = False
     for i in range(0, len(__read_file__)):
          if update_id == int(__read_file__[i][0]):
               __is_found = True
     if __is_found:
          for r in __read_file__:
               if update_id == int(r[0]):
                    if mode__ == 0:
                         r[1] = update__list[0]
                         edited__ = r[4].split(" , ")
                         edited__[0] = '1'
                         edited__[1] = str(time.time())
                         edited__[2] = '1' 
                         r[4] = " , ".join(edited__)
                    elif mode__ == 1:
                         r[2] = update__list[0]
                         edited__ = r[4].split(" , ")
                         edited__[0] = '1'
                         edited__[1] = str(time.time())
                         edited__[3] = '1' 
                         r[4] = " , ".join(edited__)
                    elif mode__ == 2:
                         r[1] = update__list[0]
                         r[2] = update__list[1]
                         edited__ = r[4].split(" , ")
                         edited__[0] = '1'
                         edited__[1] = str(time.time())
                         edited__[2] = '1' 
                         edited__[3] = '1' 
                         r[4] = " , ".join(edited__)
                    __READY_FOR_UP.append(r)
               else:
                    __READY_FOR_UP.append(r)
                    

          with open(filename, "w") as write_emp:
               write_emp.write("")
          with open(filename, "a+") as write_file:
               for i in range(0, len(__READY_FOR_UP)):
                    write_file.write(" |-13-@3*3code(013.1-qpd__)| ".join(__READY_FOR_UP[i]))
     else:
          print("Not found note!")
def open_note(file):
     print("\n")
     open_id = int(input("Open note to enter note id? "))
     read_notes = __READ_FILE_CONTENT_TO_LIST(file)
     is_found = False
     for i in range(0, len(read_notes)):
          if int(read_notes[i][0]) == open_id:
               is_found = True
     if is_found:
          open_spacific_note(open_id)
     else:
          print("Not found this note !")

def __DELETE_FILE_CONTENT(filename, deleteId):
     __DATA_STACK__ = []
     __IS_DELETED = False
     with open(filename, "r") as __delete_content:
        __count_readed = 0
        for read in __delete_content:
             __count_readed = int(read.split(" |-13-@3*3code(013.1-qpd__)| ")[0])
             if __count_readed == deleteId:
                  __IS_DELETED = True
                  __SET_HISTORY(read)
             else:
                  __DATA_STACK__.append(read)        
        # delete note from file           
     with open(filename, 'w') as __write_content:
          __write_content.write("")

     with open(filename, 'a') as __append_data:
          for i in range(0, len(__DATA_STACK__)):
               __append_data.write(__DATA_STACK__[i])
     if __IS_DELETED:
          print(f"\nComplated delete note [id: {deleteId}].\n")
     else:
          print(f"\nNot Found id {deleteId}")
          print("---")
          print(f"Unsuccess to delete, meybe already deleted or file problem, note [id: {deleteId}]")

def get_int(prompt=""):
     return int(input(prompt))
     
# def __READ_FORMAT(code):
class __show_time:
    def day(self):
        day = datetime.now().strftime("%A")
        return day
    def time(self):
         return time.time()
    def calc_time(self, old_time):
         old_time = int(old_time)
         now_time = time.time()
         total_second = int(now_time - old_time)
         return [total_second, str(total_second) + 's' if total_second < 60 else str(int(total_second / 60))+'m' if total_second < 3600 and total_second >= 60 else str(int(total_second / 3600))+'h' if total_second >= 3600 and total_second < 86400 else str(int(total_second / (24 * 3600)))+'d' if total_second >= 24 * 3600 else 'default time']
    def year(self):
         return time.localtime().tm_year
    def month(self):
         return time.localtime().tm_mon
    def show_second(self, old_time):
         old_time = int(old_time)
         now_time = time.time()
         seconds = int(now_time - old_time)
         return seconds

def __ADD(file):
     note_title = str(input("Enter note title: "))
     note__ = str(input("Enter the note: "))

     file_data = __READ_FILE(file)
     if len(note_title) > 0 or len(note__) > 0:
        time_config = __show_time()
        __WRITE_FILE(file, f"{len(file_data)+1} |-13-@3*3code(013.1-qpd__)| {note_title if note_title else '---'} |-13-@3*3code(013.1-qpd__)| {note__ if note__ else ''} |-13-@3*3code(013.1-qpd__)| {time_config.time()} , {time_config.day()} , {time_config.month()} , {time_config.year()} |-13-@3*3code(013.1-qpd__)| 0 , {time_config.time()} , 0 , 0 \n")
     
def __READ(file,id,filter="all"):
    filter_list = ["all", "new", "old", "last", "first", "single"]
    __time = __show_time()
    if filter in filter_list and filter == "all" and id == 0:
        __read_file = __READ_FILE(file)
        __list_read = __READ_FILE_CONTENT_TO_LIST(file)
        if len(__list_read) < 1:
          print("Empty note!")
          print("Create new note (press 1)? ")
          input_code = get_int()
          if input_code == 1:
               __HANDLE_INPUT_PROMPT(input_code, file)  
               print("Complate add note !")
               sys.exit()
        __count = 0
        for line in __read_file:
             edited_checker_list = line.split(" |-13-@3*3code(013.1-qpd__)| ")[4].split(" , ")
             split_line = line.split(" |-13-@3*3code(013.1-qpd__)| ")
             print(f"created at -- {__time.calc_time(float((line.split(' |-13-@3*3code(013.1-qpd__)| '))[3].split(' , ')[0]))[1]} ago {f'(edited: {__time.calc_time(float(edited_checker_list[1]))[1]})' if int(edited_checker_list[0]) == 1 else ''}")
             print_line = ""
             for i in range(0, len(split_line)-2):
                  print_line += split_line[i]
                  if i < 2:
                    print_line += ' | '
                  
             print(print_line)
             if __count+1 != len(__read_file):
                  print("\n ------- \n")
             __count += 1
             
    elif filter in filter_list and filter == "last":
         __read_file = __READ_FILE(file)
         print(f"Created at -- {__time.calc_time(float((__read_file[len(__read_file)-1].split(' |-13-@3*3code(013.1-qpd__)| '))[3].split(' , ')[0]))}")
         print(" | ".join((__read_file[len(__read_file)-1]).split(" |-13-@3*3code(013.1-qpd__)| ")))
        #  show last one
    elif filter in filter_list and filter == "first":
         __read_file = __READ_FILE(file)
         print(f"Created at -- {__time.calc_time(float((__read_file[0].split(' |-13-@3*3code(013.1-qpd__)| '))[3].split(' , ')[0]))}")
         print(" | ".join((__read_file[0]).split(" |-13-@3*3code(013.1-qpd__)| ")))
    elif filter in filter_list and filter == "new":
         read_list = __READ_FILE_CONTENT_TO_LIST(file)
         has_list = False
         for i in range(0, len(read_list)):
              old_time = float(read_list[i][3].split(" , ")[0])
              if __time.show_second(old_time) <= 3600:
                    print(read_list[i])
                    has_list = True
         if not has_list:
              print("Not found new notes !")
    elif filter in filter_list and filter == "single" and id > 0:
          read_list = __READ_FILE_CONTENT_TO_LIST(file)
          read_list_index = -1
          is_found = False
          for i in range(0, len(read_list)):
               if int(read_list[i][0]) == id:
                    is_found = True
                    read_list_index = i
          if is_found:
               note = read_list[read_list_index]
               date__ = note[3].split(" , ")
               edit_details = note[4].split(" , ")
               print(f"\n[{id}]--created--[ {date__[1][0:3]}, {__time.calc_time(float(date__[0]))[1]} ago ] {f'-- (edited at {__time.calc_time(float(edit_details[1]))[0]})' if int(edit_details[0]) == 1 else ''}")
               print(" -------------- ")
               print(f"• {note[1]}")
               print(" -------------- ")
               print(f"• {note[2]}\n")
               print(f"press 0 to see details? ")
               code__ = int(input("Enter code: "))
               if code__ == 0:
                    print(f"id: {note[0]}")
                    print(f"created at {date__[1][0:3]}, {__time.calc_time(float(date__[0]))[1]} ago ]")
                    print(f"is edited: {int(edit_details[0]) == 1} and edit {'title' if int(edit_details[2]) == 1 and int(edit_details[0]) == 1 else ''}{', note' if int(edit_details[3]) == 1 and int(edit_details[0]) == 1 else ''} ")
                    print(f"Year: {date__[3]}, Month: {date__[2]}, day: {date__[1][0:3]}")
                    print(f"Activity: {__time.calc_time(float(date__[0]))}")

def __READ_FILE_CONTENT_TO_LIST(filename):
     __USER_FILE_DATA = []
     with open(filename, "r") as read_data_file:
          for read in read_data_file:
               __USER_FILE_DATA.append(read.split(" |-13-@3*3code(013.1-qpd__)| "))
     return __USER_FILE_DATA

     
def __SET_HISTORY(write,file="delete_history.txt"):
     with open(file, "a+") as write_his: 
          write_his.write(write)
def __GET_HISTORY(file="delete_history.txt"):
     __data_list = []
     with open(file, "r") as read_his:
          for read in read_his:
               __data_list.append(read)
     return __data_list
if __name__ == "__main__":
    main()