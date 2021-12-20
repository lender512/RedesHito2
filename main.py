# mn --custom main.py --topo project
# Basesed on:  https://github.com/opencord/olt

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, UserSwitch

class ProjectTopo( Topo ):

    def build( self ):

        # Create Switch.
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
        self.addLink(s1,h2)

        self.addLink(s2,s4)
        self.addLink(s2,s5)

        self.addLink(s3,s6)
        self.addLink(s3,h7)

        self.addLink(s4,h3)

        self.addLink(s5,h4)

        self.addLink(s6,h5)
        self.addLink(s6,h6)

def runProjectTopo():

    # Create an instance of our topology
    topo = ProjectTopo()

    # Create a network based on the topology using OVS and controlled by
    # a remote controller.
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
        switch=UserSwitch,
        autoSetMacs=True )

    net.start()
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    runProjectTopo()

# Allows the file to be imported using `mn --custom main.py --topo project`
topos = {
    'project': ProjectTopo
}