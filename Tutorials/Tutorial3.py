#Diffusion Simulations with Various Boundary Conditions
#Fickian diffusion algorithm example

#Generating network, geometry, phases and physics


#adding the boundaries creates a layer of boundary pores around the network
import OpenPNM
pn = OpenPNM.Network.Cubic(name='net',shape=[10,10,10])
pn.add_boundaries()

#Controller object provides oversite to all simulations
ctrl = OpenPNM.Base.Controller()

#Geometry object should span over the whole network
Ps = pn.pores()
Ts = pn.throats()

#defining geometry
geo = OpenPNM.Geometry.Stick_and_Ball(network=pn,name='basic',pores=Ps,throats=Ts)

#Changing the pore and throat sizes
geo['throat.diameter'] = geo['throat.diameter']*1e-5
geo['pore.diameter'] = geo['pore.diameter']*1e-5
geo['throat.length'] = geo['throat.length']*1e-5

#Now much regenerate the geometry
geo.regenerate()

#Create the phase object and set a custom value
air = OpenPNM.Phases.Air(network=pn)
air['pore.Dac'] = 1e-7 #adding a custom property

#Now apply the physics object - this can be over several geometries so need to specify again which pores and throats to apply to


phys = OpenPNM.Physics.Standard(network=pn,phase=air,geometry=geo)

#Now tell the physics object to use bulk diffusion of diffusive conductance model

phys.add_model(model=OpenPNM.Physics.models.diffusive_conductance.bulk_diffusion,
           propname='throat.gdiff_ac',
           pore_diffusivity='pore.Dac')

#Generate an Algorithm Object
alg = OpenPNM.Algorithms.FickianDiffusion(network=pn,phase=air)

#Apply Dirichlet Conditions to Two Faces - get top pores
BC1_pores = pn.pores(labels=['top_boundary'])
alg.set_boundary_conditions(bctype='Dirichlet', bcvalue=0.6, pores=BC1_pores)


#Get bottom pores and apply conditions
BC2_pores = pn.pores(labels=['bottom_boundary'])
alg.set_boundary_conditions(bctype='Dirichlet', bcvalue=0.4, pores=BC2_pores)


alg.run(conductance='throat.diffusive_conductance')
alg.return_results()

ctrl.export(pn)



