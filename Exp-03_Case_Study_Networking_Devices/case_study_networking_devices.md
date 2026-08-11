# Experiment 03: Case Study of Networking Devices

**Date:** 11-08-2026  
**Subject:** Computer Networks Laboratory  

---

## 🎯 Objectives
- Study the operational principles, architecture, and functions of key network intermediate devices.
- Understand the OSI layer at which each network device operates.
- Analyze collision domains, broadcast domains, and packet forwarding techniques.

---

## 🖥️ Overview of Networking Devices

| Device | Primary OSI Layer | Primary Function | Collision Domain | Broadcast Domain | Addressing Used |
| :--- | :---: | :--- | :---: | :---: | :---: |
| **Repeater** | Layer 1 (Physical) | Regenerates weak electrical/optical signals | 1 per segment | 1 per segment | None |
| **Hub** | Layer 1 (Physical) | Multi-port repeater; broadcasts electrical signals to all ports | 1 (Shared) | 1 (Shared) | None |
| **Bridge** | Layer 2 (Data Link) | Filters and forwards frames based on MAC addresses | 1 per port | 1 (Shared) | MAC Address |
| **Switch** | Layer 2 (Data Link) | High-speed multi-port bridge with hardware ASIC switching | 1 per port (Isolated) | 1 (per VLAN) | MAC Address |
| **Router** | Layer 3 (Network) | Forwards IP packets between different networks using routing tables | 1 per port | 1 per port (Breaks Broadcast) | IP Address |
| **Gateway** | Layer 4–7 (Transport–App) | Protocol translator between incompatible network architectures | Per interface | Per interface | IP / Protocol headers |
| **Access Point (AP)** | Layer 2 (Data Link) | Connects wireless (802.11) devices to a wired Ethernet LAN | Shared wireless medium | 1 per SSID/VLAN | MAC Address |
| **Modem** | Layer 1 / 2 | Modulates digital signals to analog and vice-versa for WAN transmission | Point-to-Point | Point-to-Point | Carrier Frequency |
| **NIC** | Layer 1 & 2 | Hardware interface connecting a host to the physical network | 1 | 1 | Hardware MAC Address |

---

## 🔍 Detailed Analysis of Devices

### 1. Network Interface Card (NIC)
- **Layer:** Layer 1 & Layer 2
- **Function:** Provides physical connectivity to a transmission medium (Ethernet or Wi-Fi) and encapsulates data into frames with a burned-in 48-bit physical MAC address (e.g., `00:1A:2B:3C:4D:5E`).

### 2. Hub
- **Layer:** Layer 1 (Physical)
- **Function:** Acts as a multiport signal repeater. Any signal received on one port is blindly repeated to all other connected ports.
- **Limitation:** Half-duplex operation, prone to collisions, high network congestion.

### 3. Switch
- **Layer:** Layer 2 (Data Link)
- **Function:** Operates in full duplex mode. Maintains a dynamic MAC Address Table (CAM Table) through source address learning.
- **Forwarding Methods:** Store-and-Forward, Cut-Through, and Fragment-Free.

### 4. Router
- **Layer:** Layer 3 (Network)
- **Function:** Interconnects heterogeneous network segments (LAN to WAN). Inspects destination IP addresses and routes packets using dynamic routing protocols (e.g., OSPF, RIP, BGP) or static routes.
- **Key Characteristic:** Stops Layer 2 broadcast frames from crossing interfaces, confining broadcasts within individual subnets.

### 5. Gateway
- **Layer:** Layers 4 to 7 (Transport through Application)
- **Function:** Acts as a protocol converter or translator between two entirely different network architectures or protocol stacks (e.g., connecting an IPv4 network to an IPv6 network or translating industrial Modbus to TCP/IP).

---

## 📌 Summary & Conclusion
Each networking device is engineered for a specific layer of the OSI model:
- **Layer 1 devices (Hubs, Repeaters)** simply handle physical bits and electrical signaling.
- **Layer 2 devices (Switches, Bridges)** segment collision domains using MAC addresses.
- **Layer 3 devices (Routers)** segment broadcast domains and direct traffic between independent IP networks.
