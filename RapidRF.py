
import os
from time import sleep


input_freq = "434"
input_gain = "35"
output_freq = "434"


def kill_it():
    os.system("sudo killall rtl_sdr 2>/dev/null")
    os.system("sudo killall sendiq 2>/dev/null")
    os.system("sudo killall rtl_fm 2>/dev/null")


def welcome_screen():
    os.system("clear")
    print("Welcome to RapidRF")
    print("=" * 20)
    print("1.[R]ecord New")
    print("2.[L]oad And Replay")
    print(20 * "_")
    welcome_choice = str(input("Choose : "))

    os.system("clear")

    if welcome_choice in ("1", "r", "R"):
        radio_info()
        main_rec_screen()

    elif welcome_choice in ("2", "l", "L"):
        replay_only_radio_info()
        load_play()

    else:
        print("try 1 or 2 or r or l")
        sleep(2)
        os.system("clear")
        welcome_screen()


def radio_info():
    global input_freq, input_gain, output_freq
    os.system("clear")
    print("Frequency and Gain Settings")
    print("=" * 20)
    print("Choose INPUT Frequency (in MHZ)")
    print("This is the frequency your ltr-sdr will Listen on")
    print("Default is 434MHZ")
    print(20 * "_")
    input_freq_temp = str(input("INPUT Frequency = "))
    if input_freq_temp == "":
        pass
    else:
        input_freq = input_freq_temp

    os.system("clear")
    print("Frequency and Gain Settings")
    print("=" * 20)
    print("Choose INPUT Gain (1-45)")
    print("This is the Gain Level your ltr-sdr will use")
    print("Default is 35")
    print(20 * "_")
    input_gain_temp = str(input("INPUT Gain = "))
    if input_gain_temp == "":
        pass
    else:
        input_gain = input_gain_temp

    os.system("clear")
    print("Frequency and Gain Settings")
    print("=" * 20)
    print("Choose OUTPUT Frequency (in MHZ)")
    print("This is the frequency your Pi will Broadcast on")
    print("Default is 434MHZ")
    print(20 * "_")
    output_freq_temp = str(input("INPUT Frequency = "))
    if output_freq_temp == "":
        pass
    else:
        output_freq = output_freq_temp

    os.system("clear")


def replay_only_radio_info():
    global output_freq
    os.system("clear")
    print("Frequency and Gain Settings")
    print("=" * 20)
    print("Choose OUTPUT Frequency (in MHZ)")
    print("This is the frequency your Pi will Broadcast on")
    print("Default is 434MHZ")
    print(20 * "_")
    output_freq_temp = str(input("INPUT Frequency = "))
    if output_freq_temp == "":
        pass
    else:
        output_freq = output_freq_temp


def load_play():
    os.system("clear")
    print("Load and Replay")
    print("=" * 20)
    print("1.Load and [R]eplay")
    print("2.Load Play on [L]oop")
    print("3.[C]hange Freq")
    print("4.[B]ack to Welcome screen")
    print("5.[Q]uit")
    print(20 * "_")
    main_load_play_choice = str(input("Choose : "))

    if main_load_play_choice in ("1", "r", "R"):
        load_it_play_it(loop=False)

    elif main_load_play_choice in ("2", "l", "L"):
        load_it_play_it(loop=True)

    elif main_load_play_choice in ("3", "c", "C"):
        replay_only_radio_info()
        load_play()

    elif main_load_play_choice in ("4", "b", "B"):
        welcome_screen()

    elif main_load_play_choice in ("5", "q", "Q"):
        print("bye-bye")
        quit()


def load_it_play_it(loop):
    os.system("clear")

    f_list = []

    path = "./SAVED"
    print("Saved files")
    print("=" * 20)
    for i, file in enumerate(os.scandir(path)):
        print(i, file.name)
        f_list.append(file)
    print("_" * 20)
    file_num_to_replay = int(input("Input File Number : "))
    os.system("clear")
    if loop:
        lo = "-l"
        print("Replaying on Loop...")
    else:
        lo = ""
        print("Replaying...")
    print("=" * 20)
    print("""
   ##      ##      #
  #  #    #  #    #
>>>>>>>>>>>>>>>>>>>>  
 #    #  #    #  #
#      ##      ##
""")
    print("=" * 20)
    com_str_replay = "sudo ./sendiq -s 250000 {0} -f {1}e6 -t u8 -i {2} >/dev/null 2>/dev/null &".format(
        lo,output_freq, f_list[file_num_to_replay].path)
    os.system(com_str_replay)
    input("Press [Enter] to stop : ")
    kill_it()
    load_play()


def main_rec_screen():
    os.system("clear")
    print("Record and Replay")
    print("=" * 20)
    print("1.[R]ec NOW    [Enter]")
    print("2.Re[P]lay")
    print("3.RePlay on [L]oop")
    print("4.[S]ave")
    print("5.Save AND [M]ake Bash script")
    print("6.[C]hange Freq")
    print("7.[B]ack to Welcome screen")
    print("8.[Q]uit")
    print(20 * "_")
    main_rec_choice = str(input("Choose : "))

    if main_rec_choice in ("1", "r", "R", ""):
        rec()
    elif main_rec_choice in ("2", "p", "P"):
        replay(loop=False)
    elif main_rec_choice in ("3", "l", "L"):
        replay(loop=True)
    elif main_rec_choice in ("4", "s", "S"):
        save_it(bash_it=False)
    elif main_rec_choice in ("5", "m", "M"):
        save_it(bash_it=True)
    elif main_rec_choice in ("6", "c", "C"):
        radio_info()
        main_rec_screen()
    elif main_rec_choice in ("7", "b", "B"):
        welcome_screen()
    elif main_rec_choice in ("8", "q", "Q"):
        print("bye-bye")
        quit()
    else:
        os.system("clear")
        print("Try again...")
        main_rec_screen()


def rec():
    os.system("clear")
    print("Recording...")
    print("=" * 20)
    print("""
   ##      ##      #
  #  #    #  #    #
<<<<<<<<<<<<<<<<<<<<
 #    #  #    #  #
#      ##      ##
""")
    print("=" * 20)
    com_str = "rtl_sdr -s 250000 -g {0} -f {1}e6 record.iq >/dev/null 2>/dev/null &".format(input_gain, input_freq)
    os.system(com_str)
    input("Press [Enter] to stop : ")
    kill_it()
    main_rec_screen()


def replay(loop):
    os.system("clear")
    if loop:
        loo = "-l"
        print("Replaying on Loop...")
    else:
        loo = ""
        print("Replaying...")
    print("=" * 20)
    print("""
   ##      ##      #
  #  #    #  #    #
>>>>>>>>>>>>>>>>>>>>  
 #    #  #    #  #
#      ##      ##
""")
    print("=" * 20)
    com_str_replay = "sudo ./sendiq -s 250000 {0} -f {1}e6 -t u8 -i record.iq >/dev/null 2>/dev/null &".format(
        loo,output_freq)
    os.system(com_str_replay)
    input("Press [Enter] to stop : ")
    kill_it()
    main_rec_screen()


def save_it(bash_it):
    os.system("clear")
    save_name = input("Input Filename (without .iq) : ")
    print("Saving...")
    save_com = "cp record.iq SAVED/{1}_{0}.iq".format(output_freq, save_name)
    os.system(save_com)
    if bash_it:
        com_str_sh = "sudo echo 'sudo ./sendiq -s 250000 -f {0}e6 -t u8 -i SAVED/{1}_{0}.iq' >> {1}.sh && chmod +x {1}.sh" \
            .format(output_freq, save_name)
        os.system(com_str_sh)
    print("Saved!!!!")
    sleep(0.5)
    main_rec_screen()




welcome_screen()
