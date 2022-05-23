#!/usr/bin/python
import os
import time
import xml.etree.ElementTree as et
import pandas as pd # Pandas 3
import glob
from mininet.topo import Topo # pandas 2 
from mininet.net import Mininet #mininet.net.Mininet.ping	
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.node import Host
from mininet.link import TCLink, Link
from mininet.node import RemoteController, OVSSwitch

directory = '/home/sdn/Documents/day_by_day_jjm/Day-1/'
# Add hosts and switches 
def clean_s(df):
            df.columns = df.columns.str.replace(' ', '')
            df.columns = df.columns.str.lstrip()
            df.columns = df.columns.str.rstrip()
            df.columns = df.columns.str.strip()
            df.reset_index(inplace=True) 
            df.columns = ['n', 'S', 'D','A']
            return df
        

hosts = ['h1' , "h2" , "h3" , "h4" , "h5" , "h6" , "h7" , "h8" , "h9" , "h10" , "h11" , "h12" , "h13" , "h14" , "h15" , "h16" , "h17" , "h18" , "h19" , "h20" , "h21" , "h22", "h23" ]
switches = ['s1' , "s2" , "s3" , "s4" , "s5" , "s6" , "s7" , "s8" , "s9" , "s10" ,"s11" , "s12" , "s13" , "s14" , "s15" , "s16" , "s17" , "s18" , "s19" , "s20" ,"s21" , "s22" , "s23" ]
#################################################################################################################################

class Project(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)       
        # Add Hosts 
        for ip,host in enumerate(hosts): 
            self.addHost(host, ip='10.0.0.{}/24'.format(ip+1) , mac='00:00:00:00:00:{}'.format(ip+1))
            #host.setMAC("00:00:00:00:00:{}".format(ip+1))
            
        # Add Switches 
        for switch in switches: 
            self.addSwitch(switch)
        # Add Links between Switches and Hosts

        for host,switch in zip(hosts,switches): 
            
            self.addLink( host, switch , cls=TCLink)

        # Add link between switches and Switches Totem

      
        self.addLink(switches[0], switches[2], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[0], switches[6], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[0], switches[15], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        
        self.addLink(switches[1], switches[3], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[1], switches[6], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[1], switches[11], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[1], switches[12], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[1], switches[17], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})
        self.addLink(switches[1], switches[22], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})
        
        self.addLink(switches[2], switches[9], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[2], switches[10], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})
        self.addLink(switches[2], switches[13], cls=TCLink, params1 = {'bw':0.155}, params2 = {'bw':0.155})
        self.addLink(switches[2], switches[20], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        
        self.addLink(switches[3], switches[15], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})

        self.addLink(switches[4], switches[7], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})
        self.addLink(switches[4], switches[15], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})

        self.addLink(switches[5], switches[6], cls=TCLink, params1 = {'bw':0.155}, params2 = {'bw':0.155})
        self.addLink(switches[5], switches[18], cls=TCLink, params1 = {'bw':0.155}, params2 = {'bw':0.155})

        self.addLink(switches[6], switches[16], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[6], switches[18], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})
        self.addLink(switches[6], switches[20], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})

        self.addLink(switches[7], switches[8], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})

        self.addLink(switches[8], switches[14], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})
        self.addLink(switches[8], switches[15], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})

        self.addLink(switches[9], switches[10], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})
        self.addLink(switches[9], switches[11], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[9], switches[15], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[9], switches[16], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})

        self.addLink(switches[11], switches[21], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})

        self.addLink(switches[12], switches[13], cls=TCLink, params1 = {'bw':0.155}, params2 = {'bw':0.155})
        self.addLink(switches[12], switches[16], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[12], switches[18], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})

        self.addLink(switches[14], switches[19], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})

        self.addLink(switches[16], switches[19], cls=TCLink, params1 = {'bw':10}, params2 = {'bw':10})
        self.addLink(switches[16], switches[22], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})

        self.addLink(switches[17], switches[20], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})

        self.addLink(switches[19], switches[21], cls=TCLink, params1 = {'bw':2.5}, params2 = {'bw':2.5})
      
        
def run():
    
        topo = Project()
        net = Mininet(
            topo=topo,
            controller=RemoteController('c0', ip='127.0.0.1', port=6633, protocols="OpenFlow13"),
            switch=OVSSwitch,
            autoSetMacs=False)
        net.start()
        time.sleep(20)
        
        #checkConnection(net) For Some reason it does not ping 
        GenerateTrffic(net)
        
        net.stop()
        
def checkConnection(net):
           
    print("Testing bandwidth between all hosts and h2")
    net.pingAll()                         
     
def GenerateTrffic(net):
    
    path_to_target = './traffic-matrices/'
    path_to_file_list = glob.glob(path_to_target + '*xml' )
    path_to_file_list.sort()
    
    # From XML files # Code from LUIC 
    
    while True:
        
        for filename in path_to_file_list:
            print("File : ", filename)
            my_tree = et.parse(filename)
            my_root = my_tree.getroot()

            # print("\nLes ppts sont : ")
            for j in range (len(my_root[1])):
                hostSrc = 'h' + str(my_root[1][j].attrib['id'])
                for i in range(len(my_root[1][j])):
                    frequencekbps = float(my_root[1][j][i].text)
                    frequencebit = frequencekbps*1000
                    frequenceStr = str(frequencekbps) + 'k'
                    frequenceMBps = frequencekbps/1000
                    hostDst = str(my_root[1][j][i].attrib['id'])

                    nbrByte = frequencekbps * 15 * 60 * 1000
                    longInterA = str(nbrByte)
                    tempsTransmission = 60*60
                    print("On transmet src ", hostSrc)
                    print("On transmet dst ", hostDst)
                    print("On transmet ", frequencekbps)

                    print("L'iperf ","iperf  -c 10.0.0." + hostDst + " -p " + hostSrc[1:] + '00' + hostDst + " -u -b " + str(format(float(frequencekbps),'.3f')) + " -w 256 -t " + str(tempsTransmission) + " &")
                    net.get(hostSrc).cmd("iperf  -c 10.0.0." + hostDst + " -p " + hostSrc[1:] + '00' + hostDst + " -u -b " + str(format(float(frequencekbps),'.3f')) + " -w 256 -t " + str(tempsTransmission) + " &")
            time.sleep(60 * 60)
            break
        break
        print("On change")

    
if __name__ == '__main__':
    setLogLevel('info')
    run() # Build Topology
    