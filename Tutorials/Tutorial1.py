import OpenPNM
#Controller object provides oversite to all simulations
ctrl = OpenPNM.Base.Controller()

#initializing the network topology
pn = OpenPNM.Network.Cubic(name='net',shape=[20,5,10])

Ps = pn.pores()
Ts = pn.throats()

#initialize and build a Geometry object
geom = OpenPNM.Geometry.GenericGeometry(network=pn,pores=Ps,throats=Ts)  # instantiate geometry object

#adding desired methods to geometry
import OpenPNM.Geometry.models as gm

#May need to create an object for the reservoir
geom.add_model(propname='pore.seed',model=gm.pore_misc.random) #begin adding the desired methods to 'geom'
geom.add_model(propname='pore.diameter',
               model=gm.pore_diameter.sphere,
               psd_name='weibull_min',
               psd_shape=2.77,
               psd_loc=6.9e-7,
               psd_scale=9.8e-6,
               psd_offset=10e-6)
geom.add_model(propname='throat.diameter',model=gm.throat_misc.neighbor,pore_prop='pore.diameter',mode='min')
geom.add_model(propname='pore.volume',model=gm.pore_volume.sphere)
geom.add_model(propname='pore.area',model=gm.pore_area.spherical)
geom.add_model(propname='throat.length',model=gm.throat_length.straight)
geom.add_model(propname='throat.volume',model=gm.throat_volume.cylinder)
geom.add_model(propname='throat.area',model=gm.throat_area.cylinder)

#Create phases
air = OpenPNM.Phases.GenericPhase(network=pn,name='air')
water = OpenPNM.Phases.GenericPhase(network=pn,name='water')

#Add desired methods to phases
from OpenPNM.Phases import models as fm

air.add_model(propname='pore.diffusivity',model=fm.diffusivity.fuller,MA=0.03199,MB=0.0291,vA=16.3,vB=19.7)
air.add_model(propname='pore.viscosity',model=fm.viscosity.reynolds,uo=0.001,b=0.1)
air.add_model(propname='pore.molar_density',model=fm.molar_density.ideal_gas,R=8.314)
water['pore.diffusivity'] = 1e-12
water['pore.viscosity'] = 0.001
water['pore.molar_density'] = 44445.0
water['pore.contact_angle'] = 110.0
water['pore.surface_tension'] = 0.072

#Creating Pore Scale Physics Objects (how phase and geometric properties interact)
phys_water = OpenPNM.Physics.GenericPhysics(network=pn,phase=water,geometry=geom)
phys_air = OpenPNM.Physics.GenericPhysics(network=pn,phase=air,geometry=geom)

#Add desired methods to Physics Objects
from OpenPNM.Physics import models as pm

phys_water.add_model(propname='throat.capillary_pressure',
                     model=pm.capillary_pressure.purcell,
                     r_toroid=1.e-5)
phys_water.add_model(propname='throat.hydraulic_conductance',
                     model=pm.hydraulic_conductance.hagen_poiseuille)
phys_air.add_model(propname='throat.diffusive_conductance',
                   model=pm.diffusive_conductance.bulk_diffusion)
phys_air.add_model(propname='throat.hydraulic_conductance',
                   model=pm.hydraulic_conductance.hagen_poiseuille)

#Run some simulations
alg = OpenPNM.Algorithms.FickianDiffusion(network=pn,phase=air)
# Assign Dirichlet boundary conditions to top and bottom surface pores
BC1_pores = pn.pores('right')
alg.set_boundary_conditions(bctype='Dirichlet', bcvalue=0.6, pores=BC1_pores)
BC2_pores = pn.pores('left')
alg.set_boundary_conditions(bctype='Dirichlet', bcvalue=0.4, pores=BC2_pores)
# Use desired diffusive_conductance in the diffusion calculation (conductance for the dry network or water-filled network)
alg.run()
alg.return_results()
# Calculate the macroscopic effective diffusivity through this Network
Deff = alg.calc_eff_diffusivity()

#Visualise the results
ctrl.export(pn)





