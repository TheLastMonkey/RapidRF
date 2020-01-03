import os
from time import sleep
import RRF_config

input_freq = RRF_config.input_freq
input_gain = RRF_config.input_gain
output_freq = RRF_config.output_freq
dis_splash = RRF_config.dis_splash

dis_lines = "=" * 50
dis_under_line = "_" * 50


def kill_it():
    os.system("sudo killall rtl_sdr sendiq rtl_fm 2>/dev/null")

def main():
    os.system("clear")
    bouncer()
    if dis_splash:
        print(dis_lines)
        RRF_config.splash()
        print(dis_lines)
        sleep(1)
        os.system("clear")
    radio_info()
    main_screen()


def radio_info():
    global input_freq, input_gain
    os.system("clear")
    display()
    print("Frequency and Gain Settings")
    print(dis_lines)
    print("Choose INPUT Frequency (in MHZ)")
    print("This is the frequency your ltr-sdr will Listen on")
    print("Default is {}MHZ".format(RRF_config.input_freq))
    print(dis_under_line)
    input_freq_temp = str(input("INPUT Frequency = "))
    if input_freq_temp == "":
        pass
    else:
        input_freq = input_freq_temp

    os.system("clear")
    display()
    print("Frequency and Gain Settings")
    print(dis_lines)
    print("Choose INPUT Gain (1-45)")
    print("This is the Gain Level your ltr-sdr will use")
    print("Default is {}".format(RRF_config.input_gain))
    print(dis_under_line)
    input_gain_temp = str(input("INPUT Gain = "))
    if input_gain_temp == "":
        pass
    else:
        input_gain = input_gain_temp

    os.system("clear")
    replay_only_radio_info()


def replay_only_radio_info():
    global output_freq
    os.system("clear")
    display()
    print("Frequency and Gain Settings")
    print(dis_lines)
    print("Choose OUTPUT Frequency (in MHZ)")
    print("This is the frequency your Pi will Broadcast on")
    print("Default is {}MHZ".format(RRF_config.output_freq))
    print(dis_under_line)
    output_freq_temp = str(input("INPUT Frequency = "))
    if output_freq_temp == "":
        pass
    else:
        output_freq = output_freq_temp
    os.system("clear")


def load_play():
    kill_it()
    os.system("clear")
    display()
    print("Load and Replay")
    print(dis_lines)
    print("1.Load and [R]eplay")
    print("2.Load Play on [L]oop")
    print("3.[C]hange Freq")
    print("4.[B]ack")
    print("5.[Q]uit")
    print(dis_under_line)
    main_load_play_choice = str(input("Choose : "))

    if main_load_play_choice in ("1", "r", "R"):
        load_it_play_it(loop=False)
    elif main_load_play_choice in ("2", "l", "L"):
        load_it_play_it(loop=True)
    elif main_load_play_choice in ("3", "c", "C"):
        replay_only_radio_info()
        load_play()
    elif main_load_play_choice in ("4", "b", "B", ""):
        main_screen()
    elif main_load_play_choice in ("5", "q", "Q"):
        os.system("clear")
        print("bye-bye")
        quit()


def load_it_play_it(loop):
    kill_it()
    os.system("clear")
    display()
    f_list = []

    path = "./SAVED"
    print("Saved files")
    print(dis_lines)
    for i, file in enumerate(os.scandir(path)):
        print(i, file.name)
        f_list.append(file)
    print(dis_under_line)
    file_num_to_replay = input("Input File Number OR [Enter] to go back: ")
    if file_num_to_replay == "":
        load_play()
    else:
        file_num_to_replay = int(file_num_to_replay)
        play_file(file_num_to_replay, loop, f_list)


def play_file(file_num_to_replay, loop, f_list):
    global output_freq
    os.system("clear")
    display()
    if loop:
        lo = "-l"
        print("Replaying on Loop...")
    else:
        lo = ""
        print("Replaying...")
    print(dis_lines)
    print("""   ##      ##      ##      ##      ##      #     
  #  #    #  #    #  #    #  #    #  #    #      
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     
 #    #  #    #  #    #  #    #  #    #  #       
#      ##      ##      ##      ##      ##        """)
    print(dis_lines)

    try:
        com_str_replay = "sudo ./sendiq -s 250000 {0} -f {1}e6 -t u8 -i {2} >/dev/null 2>/dev/null &".format(
            lo, output_freq, f_list[file_num_to_replay].path)
        os.system(com_str_replay)

    except IndexError:

        print("ERROR!!!")
        print("{0} NOT in file list try again".format(file_num_to_replay))
        sleep(2)
        load_it_play_it(loop)

    respon = input("Press [Enter] to STOP OR set OUT Freq : ")
    kill_it()
    if respon == "":
        load_play()
    else:
        output_freq = respon
        play_file(file_num_to_replay, loop, f_list)


def main_screen():
    kill_it()
    os.system("clear")
    display()
    print("RapidRF")
    print(dis_lines)
    print("1.[R]ec NOW    [Enter]")
    print("2.Re[P]lay")
    print("3.RePlay on [L]oop")
    print("4.[S]ave")
    print("5.Load [A]nd Replay")
    print("6.Save AND [M]ake Bash script")
    print("7.[C]hange Freq")
    print("8.[Q]uit")
    print(dis_under_line)
    main_rec_choice = str(input("Choose : "))

    if main_rec_choice in ("1", "r", "R", ""):
        rec()
    elif main_rec_choice in ("2", "p", "P"):
        replay(loop=False)
    elif main_rec_choice in ("3", "l", "L"):
        replay(loop=True)
    elif main_rec_choice in ("4", "s", "S"):
        save_it(bash_it=False)
    elif main_rec_choice in ("5", "a", "A"):
        load_play()
    elif main_rec_choice in ("6", "m", "M"):
        save_it(bash_it=True)
    elif main_rec_choice in ("7", "c", "C"):
        radio_info()
        main_screen()
    elif main_rec_choice in ("8", "q", "Q"):
        os.system("clear")
        print("bye-bye")
        quit()
    else:
        os.system("clear")
        main_screen()


def rec():
    global input_freq, input_gain
    os.system("clear")
    display()
    print("Recording...")
    print(dis_lines)
    print("""   ##      ##      ##      ##      ##      #     
  #  #    #  #    #  #    #  #    #  #    #      
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<     
 #    #  #    #  #    #  #    #  #    #  #       
#      ##      ##      ##      ##      ##        """)
    print(dis_lines)
    com_str = "rtl_sdr -s 250000 -g {0} -f {1}e6 record.iq >/dev/null 2>/dev/null &".format(input_gain, input_freq)
    os.system(com_str)
    respon = input("Press [Enter] to STOP OR set IN Freq & try again : ")
    kill_it()
    if respon == "":
        main_screen()
    else:
        input_freq = respon
        rec()


def replay(loop):
    global output_freq
    os.system("clear")
    display()
    if loop:
        loo = "-l"
        print("Replaying on Loop...")
    else:
        loo = ""
        print("Replaying...")
    print(dis_lines)
    print("""   ##      ##      ##      ##      ##      #     
  #  #    #  #    #  #    #  #    #  #    #      
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     
 #    #  #    #  #    #  #    #  #    #  #       
#      ##      ##      ##      ##      ##        """)
    print(dis_lines)
    com_str_replay = "sudo ./sendiq -s 250000 {0} -f {1}e6 -t u8 -i record.iq >/dev/null 2>/dev/null &".format(
        loo, output_freq)
    os.system(com_str_replay)
    respon = input("Press [Enter] to STOP OR set OUT Freq : ")
    kill_it()
    if respon == "":
        main_screen()
    else:
        output_freq = respon
        replay(loop)


def save_it(bash_it):
    os.system("clear")
    display()
    save_name = input("Input Filename (without .iq) : ")
    if save_name == "":
        main_screen()
    else:
        print("Saving...")
        save_com = "cp record.iq SAVED/{1}_{0}.iq".format(output_freq, save_name)
        os.system(save_com)
        if bash_it:
            com_str_sh = "sudo echo 'sudo ./sendiq -s 250000 -f {0}e6 -t u8 -i SAVED/{1}_{0}.iq' >> {1}.sh && chmod +x {1}.sh" \
                .format(output_freq, save_name)
            os.system(com_str_sh)
        print("Saved!!!!")
        sleep(0.5)
        main_screen()


def display():
    print("IN freq: {0}      Gain: {2}      OUT freq: {1}".format(input_freq, output_freq, input_gain))
    print(dis_lines)


def bouncer():
    user_id = os.getuid()
    if user_id == 0:
        pass
    else:
        print("""A rotund man approaches you and takes you by the shoulder and wrist and escorts you out of the Python bar. 
He smiles.
Come back when you're a super user.""")
        quit()

main()
kill_it()
