import pandapower
import pandapower.networks
import pandapower.topology
import pandapower.plotting
import pandapower.converter
import pandapower.estimation
import pandapower as pp
#create empty net
net = pp.create_empty_network()
#create buses
b1 = pp.create_bus(net, vn_kv=20., name="Bus 1")
b2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")
b3 = pp.create_bus(net, vn_kv=0.4, name="Bus 3")
#create bus elements
pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid Connection")
pp.create_load(net, bus=b3, p_mw=0.1, q_mvar=0.05, name="Load");
#create branch elements
pp.create_line(net, from_bus=b1, to_bus=b2, length_km=0.2, name="Line 1", std_type="NAYY 4x150 SE") 
pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, name="Line 2", std_type="NAYY 4x150 SE");
pp.runpp(net)
# show the power flow and losses in the lines
# run power flow
pp.runpp(net)

# show bus results
print("\n--- Bus Results ---")
print(net.res_bus)

# show line results
print("\n--- Line Results ---")
print(net.res_line.iloc[:, 0:6])

# save results to CSV
net.res_bus.to_csv("results/bus_results.csv", index=False)
net.res_line.to_csv("results/line_results.csv", index=False)

print("\nResults saved to 'results' folder.")

