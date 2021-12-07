#From example: https://github.com/opencord/olt/blob/master/impl/src/main/resources/custom-topo.py
# run with: ""

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch

class ProjectTopo( Topo ):

    def build( self ):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        # Create Host.
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')

        # Add links
        self.addLink(s1,h1)
        self.addLink(s1,s2)

        self.addLink(s2,s4)
        self.addLink(s2,s5)

        self.addLink(s3,s5)
        self.addLink(s3,h7)

        self.addLink(s4,h3)

        self.addLink(s5,h4)

        self.addLink(s6,h5)
        self.addLink(s6,h6)

def runProjectTopo():

    topo = ProjectTopo()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
        switch=OVSSwitch,
        autoSetMacs=True )

    # Actually start the network
    net.start()

    # Drop the user in to a CLI so user can run commands.
    CLI( net )

    # After the user exits the CLI, shutdown the network.
    net.stop()

if __name__ == '__main__':
    # This runs if this file is executed directly
    setLogLevel( 'info' )
    runProjectTopo()

# Allows the file to be imported using `mn --custom <filename> --topo minimal`
topos = {
    'project': ProjectTopo
}
