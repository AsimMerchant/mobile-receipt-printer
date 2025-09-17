#!/usr/bin/env python3
import socket
import struct
import threading
import subprocess
import re

def get_local_ip():
    """Get the local IP address using multiple methods"""
    try:
        # Method 1: Connect to external address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        pass
    
    try:
        # Method 2: Use hostname
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        if not ip.startswith('127.'):
            return ip
    except:
        pass
    
    try:
        # Method 3: Parse ifconfig/ipconfig output
        import platform
        if platform.system() == "Linux":
            result = subprocess.run(['ip', 'route', 'get', '8.8.8.8'], 
                                  capture_output=True, text=True)
            match = re.search(r'src (\d+\.\d+\.\d+\.\d+)', result.stdout)
            if match:
                return match.group(1)
        elif platform.system() == "Windows":
            result = subprocess.run(['ipconfig'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            for i, line in enumerate(lines):
                if 'IPv4 Address' in line and '192.168.' in line:
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        return match.group(1)
    except:
        pass
    
    return "192.168.29.28"  # Fallback to your phone's IP

def create_dns_response(query_data, domain, ip_address):
    """Create a DNS response packet"""
    # Extract transaction ID from query (first 2 bytes)
    transaction_id = query_data[:2]
    
    # DNS Header for response
    flags = b'\x81\x80'  # Standard query response, no error
    questions = b'\x00\x01'  # 1 question
    answers = b'\x00\x01'    # 1 answer
    authority = b'\x00\x00'  # 0 authority records
    additional = b'\x00\x00' # 0 additional records
    
    header = transaction_id + flags + questions + answers + authority + additional
    
    # Question section (copy from original query)
    # Find the question section (skip header)
    question_start = 12
    question_end = query_data.find(b'\x00', question_start) + 5  # +5 for null + type + class
    question = query_data[question_start:question_end]
    
    # Answer section
    # Name pointer back to question (compression)
    name_pointer = b'\xc0\x0c'  # Points to offset 12 (start of question)
    record_type = b'\x00\x01'   # A record
    record_class = b'\x00\x01'  # IN class
    ttl = b'\x00\x00\x01\x2c'   # TTL: 300 seconds
    data_length = b'\x00\x04'   # 4 bytes for IPv4
    
    # Convert IP address to bytes
    ip_bytes = socket.inet_aton(ip_address)
    
    answer = name_pointer + record_type + record_class + ttl + data_length + ip_bytes
    
    return header + question + answer

def parse_domain_from_query(data):
    """Extract domain name from DNS query"""
    try:
        # Skip DNS header (12 bytes)
        pos = 12
        domain_parts = []
        
        while pos < len(data):
            length = data[pos]
            if length == 0:
                break
            pos += 1
            domain_parts.append(data[pos:pos+length].decode('utf-8'))
            pos += length
        
        return '.'.join(domain_parts)
    except:
        return ""

def forward_dns_query(data, upstream_dns="8.8.8.8"):
    """Forward DNS query to upstream DNS server"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)
        sock.sendto(data, (upstream_dns, 53))
        response, _ = sock.recvfrom(1024)
        sock.close()
        return response
    except:
        return None

def handle_dns_request(data, addr, sock, local_ip):
    """Handle incoming DNS request"""
    try:
        domain = parse_domain_from_query(data)
        print(f"DNS Query from {addr[0]}:{addr[1]} for domain: {domain}")
        
        if domain == "receipt.com":
            # Return our local IP for receipt.com
            response = create_dns_response(data, domain, local_ip)
            print(f"Responding with {local_ip} for receipt.com")
        else:
            # Forward to upstream DNS
            response = forward_dns_query(data)
            if response is None:
                print(f"Failed to forward query for {domain}")
                return
            print(f"Forwarded query for {domain} to upstream DNS")
        
        sock.sendto(response, addr)
        
    except Exception as e:
        print(f"Error handling DNS request: {e}")

def start_dns_server(port=5353):
    """Start the DNS server"""
    local_ip = get_local_ip()
    print(f"Starting DNS server on {local_ip}:{port}")
    print(f"Will respond to receipt.com queries with IP: {local_ip}")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))
    
    print(f"DNS Server listening on port {port}")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            # Handle each request in a separate thread
            thread = threading.Thread(
                target=handle_dns_request, 
                args=(data, addr, sock, local_ip)
            )
            thread.daemon = True
            thread.start()
            
    except KeyboardInterrupt:
        print("\nStopping DNS server...")
    finally:
        sock.close()

if __name__ == "__main__":
    start_dns_server()