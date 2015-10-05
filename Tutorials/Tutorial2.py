import OpenPNM

#Generating the netork, adding geometry and creating phases
pn = OpenPNM.Network.Cubic(name='net',shape =[10,10,10], spacing = 0.0001)
pn.add_boundaries()

#calling object, pn and running method pores
Ps = pn.pores()
Ts = pn.throats()
geom = OpenPNM.Geometry.Toray090(network=pn,name='basic',pores=Ps,throats=Ts)
air = OpenPNM.Phases.Air(network=pn)
water = OpenPNM.Phases.Water(network=pn)

#Defining the Pore-scale Physics - pressure at which phase can invade etc.
phys = OpenPNM.Physics.GenericPhysics(network=pn,phase=water,geometry = geom)

#Add the desired methods to this object
phys.add_model(propname='throat.capillary_pressure',model=OpenPNM.Physics.models.capillary_pressure.washburn)

water['pore.contact_angle'] = 140.0

#Run the drainage simulation - create an algorithm object
OP_1 = OpenPNM.Algorithms.OrdinaryPercolation(network=pn,invading_phase=water)

#define parameters for the run() command (inlet is bottom boundary)
Ps = pn.pores(labels=['bottom_boundary'])
OP_1.run(inlets=Ps)

OP_1.plot_drainage_curve()

