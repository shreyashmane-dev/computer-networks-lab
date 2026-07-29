# Lab-01: Multi Area OSPF

## 🎯 Objectives
- Build and configure the network topology in Cisco Packet Tracer.
- Verify node connectivity and analyze network protocol behavior.

---

## 💾 Topology File & Direct Download
- **Packet Tracer File**: `ospf_topology.pkt`
- [📥 **Download ospf_topology.pkt**](https://github.com/shreyashmane-dev/computer-networks-lab/raw/main/Cisco_Labs/Lab-01_Multi_Area_OSPF/ospf_topology.pkt)
- Open this file in **Cisco Packet Tracer v8.x+** to inspect the configuration and simulate traffic.

---

## 📐 Network Topology & Configuration

> *Upload a `topology.png` screenshot to this lab folder to visually display the diagram here.*

### Device Addressing Table Template

| Device Name | Interface | IP Address | Subnet Mask | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **Router1** | GigabitEthernet0/0/0 | `192.168.1.1` | `255.255.255.0` | N/A |
| **PC1** | FastEthernet0 | `192.168.1.10` | `255.255.255.0` | `192.168.1.1` |

---

## 🔍 Verification Steps
1. Open `ospf_topology.pkt` in Cisco Packet Tracer.
2. Enter Desktop > Command Prompt on end devices.
3. Test connectivity using `ping <destination-ip>`.
