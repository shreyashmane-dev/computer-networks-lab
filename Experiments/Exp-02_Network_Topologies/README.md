# Exp 02: Network Topologies (Bus, Star, Ring & Mesh)

## 🎯 Objectives
- Build and compare physical and logical network topologies in Cisco Packet Tracer.
- Analyze collision domains, broadcast domains, and fault tolerance across Bus, Star, Ring, and Mesh topologies.
- Evaluate traffic performance using simulation mode.

---

## 📐 Network Topology
Star and Mesh topologies constructed using Cisco Switches and Routers.

![Topology Screenshot](topology.png)

---

## 📊 Topology Comparison Summary

| Topology Type | Devices Required | Redundancy | Cable Cost | Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Bus** | Coaxial / Switch | Low | Low | Simple |
| **Star** | Central Switch | Medium | Moderate | Easy |
| **Ring** | Dual ring switch | Medium | Moderate | Medium |
| **Mesh** | Full Mesh links | **High** | High | Complex |

---

## 🔍 Verification & Observation
In simulation mode, PDU packets were sent across redundant links in Full Mesh topology to test auto-rerouting when a primary link fails.
