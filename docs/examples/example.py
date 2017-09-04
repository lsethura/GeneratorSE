# 1 ---------

from math import pi
import numpy as np
import generatorse.PMSG_arms


# 1 ---------
# 2 ---------

# simple test of PMSG for a 5 MW turbine

  opt_problem = Drive_PMSG_arms('CONMINdriver','Costs')  		# Optimiser and Objective function
	
	# Initial design variables for a DD PMSG designed for a 5MW turbine
	
	opt_problem.P_rated=5.0e6             										# Rated power  
	opt_problem.T_rated=4.143289e6														# Rated torque (Nm)
	opt_problem.N=12.1                    										# Rated speed (rpm)
	opt_problem.Eta_target = 93																# Target design efficiency %
	
	opt_problem.PMSG_r_s= 3.26																# Air gap radius (meter)               
	opt_problem.PMSG_l_s= 1.6																	# core length (meter)
	opt_problem.PMSG_h_s = 0.07																# Stator slot height (meter)
	opt_problem.PMSG_tau_p = 0.08															# Pole pitch (meter)
	opt_problem.PMSG_h_m = 0.009															# Magnet height (meter)
	opt_problem.PMSG_h_ys = 0.0615														# Stator yoke height (meter)
	opt_problem.PMSG_h_yr = 0.057															# Rotor yoke height (meter)
	opt_problem.PMSG_n_s = 5																	# Stator arms
	opt_problem.PMSG_b_st = 0.480															# Stator circumferential arm dimension (meter)
	opt_problem.PMSG_n_r =5																		# Rotor arms
	opt_problem.PMSG_b_r = 0.520															# Rotor circumferential arm dimension (meter)
	opt_problem.PMSG_d_r = 0.7																# Rotor axial arm dimension (meter)
	opt_problem.PMSG_d_s= 0.3																	# Stator axial arm dimension (meter)
	opt_problem.PMSG_t_wr =0.06																# Rotor arm thickness (meter)
	opt_problem.PMSG_t_ws =0.06																# Stator arm thickness (meter)
	opt_problem.PMSG_R_o =0.43      													# Main shaft radius (meter)
	
	# Specific costs
	opt_problem.C_Cu   =4.786                  								# Unit cost of Copper $/kg
	opt_problem.C_Fe	= 0.556                    							# Unit cost of Iron/magnetic steel $/kg
	opt_problem.C_Fes =0.50139                   							# specific cost of structural steel
	
	#Material properties
	opt_problem.rho_Fe = 7700                 								# magnetic Steel density
	opt_problem.rho_Copper =8900              								# Kg/m3 copper density
	opt_problem.rho_PM =7450                  								# Kg/m3 magnet density
	opt_problem.rho_Fes =7850                  								# Kg/m3 structural steel density

# 2 ----------
# 3 ----------

opt_problem.run()

# 3 ----------
# 4 ----------

raw_data = {'Parameters': ['Rating','Stator Arms', 'Stator Axial arm dimension','Stator Circumferential arm dimension',' Stator arm Thickness' ,'Rotor arms','Rotor Axial arm dimension','Rotor Circumferential arm dimension' ,'Rotor arm Thickness',' Stator Radial deflection', 'Stator Axial deflection','Stator circum deflection',' Rotor Radial deflection', 'Rotor Axial deflection','Rotor circum deflection', 'Air gap diameter','Overall Outer diameter', 'Stator length', 'l/d ratio','Slot_aspect_ratio','Pole pitch', 'Stator slot height','Stator slotwidth','Stator tooth width', 'Stator yoke height', 'Rotor yoke height', 'Magnet height', 'Magnet width', 'Peak air gap flux density fundamental','Peak stator yoke flux density','Peak rotor yoke flux density','Flux density above magnet','Maximum Stator flux density','Maximum tooth flux density','Pole pairs', 'Generator output frequency', 'Generator output phase voltage', 'Generator Output phase current', 'Stator resistance','Synchronous inductance', 'Stator slots','Stator turns','Conductor cross-section','Stator Current density ','Specific current loading','Generator Efficiency ','Iron mass','Magnet mass','Copper mass','Mass of Arms', 'Total Mass', 'Stator Mass','Rotor Mass','Total Material Cost'],
			'Values': [opt_problem.PMSG.P_gennom/1000000,opt_problem.PMSG.n_s,opt_problem.PMSG.d_s*1000,opt_problem.PMSG.b_st*1000,opt_problem.PMSG.t_ws*1000,opt_problem.PMSG.n_r,opt_problem.PMSG.d_r*1000,opt_problem.PMSG.b_r*1000,opt_problem.PMSG.t_wr*1000,opt_problem.PMSG.Stator_delta_radial*1000,opt_problem.PMSG.Stator_delta_axial*1000,opt_problem.PMSG.Stator_circum*1000,opt_problem.PMSG.Rotor_delta_radial*1000,opt_problem.PMSG.Rotor_delta_axial*1000,opt_problem.PMSG.Rotor_circum*1000,2*opt_problem.PMSG.r_s,opt_problem.PMSG.R_out*2,opt_problem.PMSG.l_s,opt_problem.PMSG.K_rad,opt_problem.PMSG.Slot_aspect_ratio,opt_problem.PMSG.tau_p*1000,opt_problem.PMSG.h_s*1000,opt_problem.PMSG.b_s*1000,opt_problem.PMSG.b_t*1000,opt_problem.PMSG.t_s*1000,opt_problem.PMSG.t*1000,opt_problem.PMSG.h_m*1000,opt_problem.PMSG.b_m*1000,opt_problem.PMSG.B_g,opt_problem.PMSG.B_symax,opt_problem.PMSG.B_rymax,opt_problem.PMSG.B_pm1,opt_problem.PMSG.B_smax,opt_problem.PMSG.B_tmax,opt_problem.PMSG.p,opt_problem.PMSG.f,opt_problem.PMSG.E_p,opt_problem.PMSG.I_s,opt_problem.PMSG.R_s,opt_problem.PMSG.L_s,opt_problem.PMSG.S,opt_problem.PMSG.N_s,opt_problem.PMSG.A_Cuscalc,opt_problem.PMSG.J_s,opt_problem.PMSG.A_1/1000,opt_problem.PMSG.gen_eff,opt_problem.PMSG.Iron/1000,opt_problem.PMSG.mass_PM/1000,opt_problem.PMSG.M_Cus/1000,opt_problem.PMSG.Inactive/1000,opt_problem.PMSG.M_actual/1000,opt_problem.PMSG.Stator/1000,opt_problem.PMSG.Rotor/1000,opt_problem.PMSG.Costs/1000],
				'Limit': ['','','',opt_problem.PMSG.b_all_s*1000,'','','',opt_problem.PMSG.b_all_r*1000,'',opt_problem.PMSG.u_all_s*1000,opt_problem.PMSG.y_all*1000,opt_problem.PMSG.z_all_s*1000,opt_problem.PMSG.u_all_r*1000,opt_problem.PMSG.y_all*1000,opt_problem.PMSG.z_all_r*1000,'','','','(0.2-0.27)','(4-10)','','','','','','','','','','<2','<2','<2',opt_problem.PMSG.B_g,'','','','','>500','','','','','5','3-6','60','>93%','','','','','','','',''],
				'Units':['MW','unit','mm','mm','mm','mm','mm','','mm','mm','mm','mm','mm','mm','mm','m','m','m','','','mm','mm','mm','mm','mm','mm','mm','mm','T','T','T','T','T','T','-','Hz','V','A','ohm/phase','p.u','A/mm^2','slots','turns','mm^2','kA/m','%','tons','tons','tons','tons','tons','ton','ton','k$']}
	df=pd.DataFrame(raw_data, columns=['Parameters','Values','Limit','Units'])
print df

# 4 ---------
# 5 ---------

# test of gear driven doubly fed Induction generator

# Initial design values for a DFIG designed for a 5MW turbine
  opt_problem = Drive_DFIG('CONMINdriver','Costs')         # Optimiser and Objective function
	opt_problem.Eta_target=93																 # Target overall drivetrain efficiency             
	opt_problem.DFIG_P_rated=5e6														 # Rated power
	opt_problem.DFIG_N_rated=1200														 # Rated speed
	opt_problem.Gearbox_efficiency=0.955										 # Gearbox efficiency
	opt_problem.DFIG_r_s= 0.65                               # Air gap radius (meter)                       
	opt_problem.DFIG_l_s= 0.6 															 # Core length (meter)
	opt_problem.DFIG_h_s = 0.1 															 # Stator Slot height (meter)
	opt_problem.DFIG_h_r = 0.065 														 # Rotor Slot height (meter)
	opt_problem.DFIG_I_0 = 32 															 # No-load magnetization current (Ampere)
	opt_problem.DFIG_B_symax = 1.3 													 # Peak Stator yoke flux density (Tesla)
	opt_problem.DFIG_S_Nmax = -0.3  												 # Maximum slip
	
	# Specific costs
	opt_problem.C_Cu   =4.786                  							 # Unit cost of Copper $/kg
	opt_problem.C_Fe	= 0.556                    						 # Unit cost of Iron $/kg
	opt_problem.C_Fes =0.50139                   						 # specific cost of structure
	
	#Material properties
	opt_problem.rho_Fe = 7700                 							 #Steel density
	opt_problem.rho_Copper =8900                  					 # Kg/m3 copper density

	opt_problem.run()

# NREL 5 MW Drivetrain variables
nace.drivetrain_design = 'geared' # geared 3-stage Gearbox with induction generator machine
nace.machine_rating = 5000.0 # kW
nace.gear_ratio = 96.76 # 97:1 as listed in the 5 MW reference document
nace.gear_configuration = 'eep' # epicyclic-epicyclic-parallel
#nace.bevel = 0 # no bevel stage
nace.crane = True # onboard crane present
nace.shaft_angle = 5.0 #deg
nace.shaft_ratio = 0.10
nace.Np = [3,3,1]
nace.ratio_type = 'optimal'
nace.shaft_type = 'normal'
nace.uptower_transformer=False
nace.shrink_disc_mass = 333.3*nace.machine_rating/1000.0 # estimated
nace.carrier_mass = 8000.0 # estimated
nace.mb1Type = 'CARB'
nace.mb2Type = 'SRB'
nace.flange_length = 0.5 #m
nace.overhang = 5.0
nace.gearbox_cm = 0.1
nace.hss_length = 1.5
nace.check_fatigue = 0 #0 if no fatigue check, 1 if parameterized fatigue check, 2 if known loads inputs
nace.blade_number=3
nace.cut_in=3. #cut-in m/s
nace.cut_out=25. #cut-out m/s
nace.Vrated=11.4 #rated windspeed m/s
nace.weibull_k = 2.2 # windepeed distribution shape parameter
nace.weibull_A = 9. # windspeed distribution scale parameter
nace.T_life=20. #design life in years
nace.IEC_Class_Letter = 'A'
nace.L_rb = 1.912 # length from hub center to main bearing, leave zero if unknown

# NREL 5 MW Tower Variables
nace.tower_top_diameter = 3.78 # m

# 5 ---------
# 6 ---------

nace.run()

# 6 ---------
# 7 ---------

print "Estimate of Nacelle Component Sizes for the NREL 5 MW Reference Turbine"
print 'Low speed shaft: {0:8.1f} kg'.format(nace.lowSpeedShaft.mass)
print 'Main bearings: {0:8.1f} kg'.format(nace.mainBearing.mass + nace.secondBearing.mass)
print 'Gearbox: {0:8.1f} kg'.format(nace.gearbox.mass)
print 'High speed shaft & brakes: {0:8.1f} kg'.format(nace.highSpeedSide.mass)
print 'Generator: {0:8.1f} kg'.format(nace.generator.mass)
print 'Variable speed electronics: {0:8.1f} kg'.format(nace.above_yaw_massAdder.vs_electronics_mass)
print 'Overall mainframe:{0:8.1f} kg'.format(nace.above_yaw_massAdder.mainframe_mass)
print '     Bedplate: {0:8.1f} kg'.format(nace.bedplate.mass)
print 'Electrical connections: {0:8.1f} kg'.format(nace.above_yaw_massAdder.electrical_mass)
print 'HVAC system: {0:8.1f} kg'.format(nace.above_yaw_massAdder.hvac_mass )
print 'Nacelle cover: {0:8.1f} kg'.format(nace.above_yaw_massAdder.cover_mass)
print 'Yaw system: {0:8.1f} kg'.format(nace.yawSystem.mass)
print 'Overall nacelle: {0:8.1f} kg'.format(nace.nacelle_mass, nace.nacelle_cm[0], nace.nacelle_cm[1], nace.nacelle_cm[2], nace.nacelle_I[0], nace.nacelle_I[1], nace.nacelle_I[2]  )
print '    cm {0:6.2f} {1:6.2f} {2:6.2f} [m, m, m]'.format(nace.nacelle_cm[0], nace.nacelle_cm[1], nace.nacelle_cm[2])
print '    I {0:6.1f} {1:6.1f} {2:6.1f} [kg*m^2, kg*m^2, kg*m^2]'.format(nace.nacelle_I[0], nace.nacelle_I[1], nace.nacelle_I[2])
# 7 ---------