import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        print(f"[+] IP Source: {ip_src}, Destination: {ip_dst}, Protocol: {protocol}")

        # Add your analysis logic here
        # For example, you could check for specific patterns or conditions

# Replace 'eth0' with your network interface
sniff("eth0")
