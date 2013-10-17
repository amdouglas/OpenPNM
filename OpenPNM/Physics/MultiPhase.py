
"""
module MultiPhase
===============================================================================

"""

import OpenPNM
import scipy as sp

def Conduit_Filled_State_Calculator(network):
    r"""
    nothing yet
    """
    if 'Pc_invaded' in network.pore_properties:
        network.pore_properties['swp'] = network.pore_properties['Pc_invaded']>p_val
        network.pore_properties['snwp'] = -network.pore_properties['swp']
    elif 'IP_Pseq' in network.pore_properties:
        network.pore_properties['snwp'] = network.pore_properties['IP_Pseq']>p_val
        network.pore_properties['snwp'] = -network.pore_properties['swp']
    pores = network.get_connected_pores(network.throat_properties['numbering'],flatten=0)
    network.throat_properties['swp_conduits'] = -(-network.pore_properties['swp'][pores[:,0]]*-network.pore_properties['swp'][pores[:,1]])
    network.throat_properties['snwp_conduits'] = -(-network.pore_properties['snwp'][pores[:,0]]*-network.pore_properties['snwp'][pores[:,1]])

#    if -sp.in1d(neighborPs,self.Pinvaded).all():
#        self._net.throat_properties['UninvadedConduits'] = 1
#            val_name = 'Pc_invaded'
#
#        elif self.Alg=='IP':
#            Alg_var = self.Psequence
#            val_name = 'IP_Pseq'
#
#        for P_val in Alg_var:
#            self._logger.info("Applying Pressure/Sequence = "+str(P_val))
#            Concentration = self._do_one_inner_iteration(P_val)
#            #Store result of Concentration in each step
#            if P_val!=0:
#                Concentration = np.multiply(Concentration,self._net.pore_properties[val_name]>P_val)
#
#            self._net.set_pore_property(name="Concentration_at_"+str(P_val),ndarray=Concentration)
#    return

def Apply_Phase_State_to_Conduit_Conductivity(network):
    r"""
    nothing yet
    """
    C_wet = network.throat_properties['Cdiff']
    C_wet[network.throat_properties['snwp']] = 1e-30
    return(C_wet)

def Late_Pore_Filling(network,swpi=0.0,eta=1.0,Pc=0.0):
    r"""
    Applies a late pore filling model to determine the fractional saturation of a pore

    Parameters
    ----------
    network : OpenPNM Network Object

    swpi : float, array_like
        The fraction of each pore still filled by wetting phase upon initial invasion

    eta : float, array_like
        The late pore filling exponent

    Pc : float, scalar
        The capillary pressure applied to the nonwetting phase

    Notes
    -----

    """

    Pc_star = network.pore_conditions['Pc_invaded']
    swp = swpi*(Pc_star/Pc)**eta*(network.pore_conditions['Pc_invaded']<=Pc)
    swp = swp + (network.pore_conditions['Pc_invaded']>Pc)
    network.pore_conditions['satn_wp'] = swp









