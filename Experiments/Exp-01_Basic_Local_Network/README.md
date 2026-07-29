# Exp 01: Basic Local Network Setup & PC Configuration

## 🎯 Objectives
- Understand basic LAN (Local Area Network) concepts.
- Configure IP addresses, subnet masks, and default gateways on end-host PCs.
- Verify node-to-node connectivity using `ping` and `traceroute` commands in Cisco Packet Tracer.

---

## 📐 Network Topology
Below is the network topology configured in Cisco Packet Tracer containing 2 PCs connected via a 2960 Ethernet Switch.

![Topology Screenshot](topology.png)

---

## 💻 Addressing Table

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
| :--- | :--- | :--- | :--- | :--- |
| **PC-A** | FastEthernet0 | `192.168.1.10` | `255.255.255.0` | `192.168.1.1` |
| **PC-B** | FastEthernet0 | `192.168.1.20` | `255.255.255.0` | `192.168.1.1` |

---

## 🔍 Verification & Output
Executing ping from PC-A to PC-B:
```text
C:\> ping 192.168.1.20

Pinging 192.168.1.20 with 32 bytes of data:
Reply from 192.168.1.20: bytes=32 time=1ms TTL=128
Reply from 192.168.1.20: bytes=32 time=1ms TTL=128
Reply from 192.168.1.20: bytes=32 time=1ms TTL=128
Reply from 192.168.1.20: bytes=32 time=1ms TTL=128

Ping statistics for 192.168.1.20:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
```
*Result: Successful 0% loss ping verification.*
