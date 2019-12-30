# RapidRF  
RapidRF is a drop in script or companion to Rpitx. It uses RTL-SDR and
sendiq to record playback and save RF signals via a SDR and frequency
modulation of GPIO pin 4 of most raspberry pi devices. 

It allows the rapid profiling of RF devices for the purposes of replay
or loop immediately as well as the ability to save and load. It can also
generate a bash script for convenience.

### Requirements
 
Raspberry Pi device  
Kali preferred but raspbian as root may work  
Must be run as root user  
RTL-SDR  
Wire for antenna  
sendiq and rtl_sdr as part of [rpitx](https://github.com/F5OEO/rpitx)

This is meant to be a companion script/drop in script so it assumes that
you have already followed the setup of the rpitx project. 
### Install / drop in.
You only need to drop this script into the same folder which should look
something like "rpitx". After that you need to create a folder named
"SAVED" this is where the .iq the files are stored for later use.  

#### Notes  
Generated bash scripts will be dumped into the main folder and are
automatically made executable. Please note that these bash scripts are
not necessary for replay within the RapidRF script and are meant to be a
easy way of replaying a signal outside of the RapidRF script. Such as
home automation and other nefarious uses.

Note that the signals frequency is added to the bash script as well as
appended to the file name so that the bash script works as expected and
so that you can keep track of what frequency you need to be using for
later loading of files within the RapidRF script.   

You can choose to simply replay or replay on loop and you can change the
input and output frequencies to your liking for fine-tuning. Input and
output frequencies can be independent of each other.  
 
So why did I make this script. Rpitx is a great project. However I
required a different feature set. The ability to rapidly profile and
device save and load and replay is highly useful when you have only
moments with a RF device or when you have lots of RF devices to profile
one right after the other. In a home automation scenario you would have
6 buttons for 3 RF outlet switches and this project is intended to make
quick work of that with a simple interface that can run over SSH.  
 
To get the cleanest recording I would suggest knowing exactly what
frequency you need to be listening on and knowing your particular SDRs
behavior and frequency offset. Don't hold the RF device too close or too
far away for the appropriate gain that you have specified. Foremost low
power RF devices I would suggest in between 1 and 6 feet. Use an
appropriate sized wire for your antenna. You shouldn't need anything
over 6in. A low pass filter is highly recommended however if your RF
receiver isn't too picky and the other electronics in the area aren't
too susceptible to RF interference then you can probably get away
without it. However I would only recommend doing that for short bursts
and of course following FCC guidelines. Although realistically your
broadcast it's going to be limited by about 100ft and without a filter
your signal is likely to be a little dirty.  

#### Troubleshooting

All errors are pipe to dev/null :D  

#### License.  
Software should be free.  
This script is really just a wrapper for other programs. I am not
legally liable for misuse or damaged caused by this script. I do not
condone the use of the script for any reason and you should always read
the script before you use it especially when someone from the Internet
is asking you to run it as root.



