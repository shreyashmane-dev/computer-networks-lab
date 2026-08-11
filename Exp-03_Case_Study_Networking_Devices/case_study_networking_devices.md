# Experiment No.: 3

**Aim:** Case Study on Networking Devices and Transmission Media

---

### **PART A: NETWORKING DEVICES**

1. **Hub (Multiport Repeater)**
   * **OSI Layer:** Layer 1 (Physical Layer).
   * **Working Principle & Purpose:** Receives a signal from one port, regenerates the corrupted bits to remove noise, and broadcasts the signal out of all other outgoing ports to every station on the network without filtering capability.
   * **Ports:** Multiport device (4, 8, 16, or 24 ports).

2. **Switch (Two-Layer Switch)**
   * **OSI Layer:** Layer 2 (Data Link Layer & Physical Layer).
   * **Working Principle & Purpose:** Inspects destination MAC addresses in incoming frames and uses a dynamically learned MAC address table to forward frames directly to the specific destination port, eliminating collisions.
   * **Ports:** Multiport device (8, 16, 24, or 48 ports).

3. **Router (Three-Layer Switch)**
   * **OSI Layer:** Layer 3 (Network Layer, Data Link Layer, & Physical Layer).
   * **Working Principle & Purpose:** Connects independent networks; inspects destination logical IP addresses in incoming packets, consults its routing table, and forwards packets along optimum paths. It changes physical MAC addresses at each hop.
   * **Ports:** Multi-interface (FastEthernet, GigabitEthernet, Serial WAN interfaces).

4. **Bridge**
   * **OSI Layer:** Layer 2 (Data Link Layer & Physical Layer).
   * **Working Principle & Purpose:** Connects two LAN segments; regenerates signals and filters traffic by checking source and destination MAC addresses before forwarding.

5. **Repeater**
   * **OSI Layer:** Layer 1 (Physical Layer).
   * **Working Principle & Purpose:** Receives weak or attenuated signals over long cable distances, regenerates and retimes the original bit pattern, and retransmits the refreshed signal to extend physical coverage.

6. **Gateway**
   * **OSI Layer:** Operates across all 7 OSI Layers.
   * **Working Principle & Purpose:** Serves as an intermediary converter between two completely different protocol suites or system architectures (e.g., connecting a TCP/IP network to a proprietary mainframe network).

7. **Modem (Modulator-Demodulator)**
   * **OSI Layer:** Layer 1 (Physical Layer).
   * **Working Principle & Purpose:** Converts digital signals from a computer into analog signals for transmission over telephone/cable lines (Modulation) and converts incoming analog signals back into digital bits (Demodulation).

8. **Wireless Access Point (AP)**
   * **OSI Layer:** Layer 2 (Data Link Layer) & Layer 1 (Physical Layer).
   * **Working Principle & Purpose:** Connects wireless stations (gadgets) using radio frequency signals to a wired local area network in an Infrastructure Basic Service Set (BSS).

9. **Firewall**
   * **OSI Layer:** Layers 3, 4, and 7 (Network, Transport, and Application Layers).
   * **Working Principle & Purpose:** Monitors and filters incoming and outgoing network traffic based on predefined security policies to protect against unauthorized access and cyber threats.

10. **Network Interface Card (NIC)**
    * **OSI Layer:** Layer 2 (Data Link Layer) & Layer 1 (Physical Layer).
    * **Working Principle & Purpose:** Hardware circuit board installed inside a computer that provides the physical connection to the network medium and holds the unique 48-bit physical MAC address.

---

### **PART B: TRANSMISSION MEDIA (NETWORK CABLES)**

1. **Twisted-Pair Cable (UTP / STP):**
   * **Construction:** Consists of pairs of color-coded insulated copper conductors twisted together to minimize crosstalk and electromagnetic interference. Available as Unshielded (UTP) or Shielded (STP with metal foil).
   * **Speed & Distance:** 10 Mbps to 10 Gbps (Cat 5e, Cat 6, Cat 7); Maximum distance: **100 meters**.
   * **Connector:** **RJ-45** (Male plug and Female jack).

2. **Coaxial Cable:**
   * **Construction:** Central inner copper conductor surrounded by an insulating layer, outer braided metallic shield, and protective plastic cover.
   * **Speed & Distance:** 10 Mbps (Thinnet / Thicknet); Maximum distance: **185m (10Base2)** to **500m (10Base5)**.
   * **Connector:** **BNC** (BNC T-connector, BNC terminator).

3. **Optical Fiber Cable:**
   * **Construction:** Glass or plastic core surrounded by cladding and a protective buffer, transmitting data as light pulses using total internal reflection.
   * **Speed & Distance:** 100 Mbps to 10+ Gbps; Maximum distance: **2 km to 40+ km**.
   * **Connector:** **ST**, **SC**, **LC**.

4. **Ethernet Cable Pinout Types:**
   * **Straight-Through Cable:** Both ends wired to the same standard (T568B to T568B). Connects **different devices** (e.g., PC to Switch, Switch to Router).
   * **Crossover Cable:** Transmit and Receive pairs swapped at one end (T568A to T568B). Connects **similar devices** (e.g., PC to PC, Switch to Switch).
   * **Rollover (Console) Cable:** Pin 1 to Pin 8, Pin 2 to Pin 7 (completely reversed). Used to connect a PC's serial/USB port to a Cisco Router or Switch **console port** for configuration.

---

### **PART D: COMPARATIVE STUDY MATRIX**

| Parameters | Hub | Switch | Router | Bridge | Gateway |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **OSI Layer** | Layer 1 (Physical) | Layer 2 (Data Link) | Layer 3 (Network) | Layer 2 (Data Link) | Layers 1–7 |
| **Data Unit** | Bits | Frames | Packets / Datagrams | Frames | Messages / Data |
| **Addressing Used** | None | MAC Address | IP Address | MAC Address | Protocol Addresses |
| **Data Forwarding** | Broadcast | Unicast / Filtering | Routing / Unicast | Filtering / Forwarding | Protocol Translation |
| **Collision Domains** | 1 Single Domain | Per-port Domain | Per-port Domain | Separate Domains | Separate Domains |

---

### **PART C: PRACTICAL ACTIVITY (LAB COMPONENT IDENTIFICATION)**

| Sr. No. | Device / Cable | Model / Specifications | Manufacturer | Purpose |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Ethernet Switch | Cisco 2960 24-Port FastEthernet | Cisco Systems | Connects multiple lab PCs in a local star topology. |
| **2** | Network Router | Cisco 1941 Integrated Services Router | Cisco Systems | Provides inter-VLAN routing and default gateway connectivity. |
| **3** | UTP Cable | Category 6 (Cat6) Unshielded Twisted Pair | D-Link / Amp | Transmits 1 Gbps data up to 100 meters between PC and Switch. |
| **4** | Cable Connector | RJ-45 Male Connector | D-Link | Terminates 8-wire UTP cable ends for insertion into NIC ports. |
| **5** | Network Adapter | Realtek PCIe Gigabit Ethernet NIC | Realtek | Hardware card providing 48-bit MAC address for host network access. |

---

### **CONCLUSION**
Students completed a case study on networking devices and transmission media, gaining understanding of device operations across OSI layers (Hub, Switch, Router, Bridge, Gateway) and physical cabling characteristics (UTP, Coaxial, Fiber, Ethernet pinouts).
