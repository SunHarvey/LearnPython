import logging
import socket
import threading
from dnslib import *

# 配置日志记录器
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DNSHandler:
    def __init__(self, host, port, upstream_dns):
        self.host = host
        self.port = port
        self.upstream_dns = upstream_dns
        self.records = {}

    def add_record(self, name, rtype, data):
        if name not in self.records:
            self.records[name] = {}
        if rtype not in self.records[name]:
            self.records[name][rtype] = []
        self.records[name][rtype].append(data)

    def add_record_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 3:
                    name, rtype, data = parts
                    # 添加末尾的点以确保域名格式正确
                    if not name.endswith('.'):
                        name += '.'
                    if not data.endswith('.'):
                        data += '.'
                    # Map record type strings to type codes
                    if rtype.upper() == 'A':
                        rtype_code = QTYPE.A
                    elif rtype.upper() == 'CNAME':
                        rtype_code = QTYPE.CNAME
                    else:
                        logger.error("Invalid record type: %s", rtype)
                        continue
                    self.add_record(name.lower(), rtype_code, data)  # 将域名转换为小写
                    logger.info("Loaded record: %s %s %s", name, rtype, data)
                else:
                    logger.error("Invalid record format: %s", line)

    def resolve_udp(self, data, client_address):
        request = DNSRecord.parse(data)
        reply = self.process_dns_request(request, client_address)
        return reply.pack()

    def resolve_tcp(self, tcp_connection):
        data = tcp_connection.recv(1024)
        if len(data) < 2:
            logger.error("Incomplete TCP packet received")
            return None
        data_length = int.from_bytes(data[:2], byteorder='big')
        while len(data) < data_length + 2:
            more_data = tcp_connection.recv(1024)
            if not more_data:
                logger.error("Connection closed before complete TCP packet received")
                return None
            data += more_data
        request = DNSRecord.parse(data[2:].strip())
        client_address = tcp_connection.getpeername()  # 获取客户端地址
        reply = self.process_dns_request(request, client_address)
        return reply.pack()

    def process_dns_request(self, request, client_address):
        reply = request.reply()
        qname = str(request.q.qname).lower()  # 将查询的域名转换为小写
        qtype = request.q.qtype

        log_msg = f"Client {client_address[0]} requested {qname} type {QTYPE[qtype]}"

        if qname in self.records:
            if qtype == QTYPE.A:
                for ip in self.records[qname].get(QTYPE.A, []):
                    reply.add_answer(RR(qname, QTYPE.A, rdata=A(ip)))
                    log_msg += f". Resolved {qname} to {ip}"
            elif qtype == QTYPE.CNAME:
                cname = self.records[qname].get(QTYPE.CNAME)
                if cname:
                    reply.add_answer(RR(qname, QTYPE.CNAME, rdata=CNAME(cname[0])))
                    log_msg += f". Resolved {qname} to {cname[0]}"
                else:
                    log_msg += ". No CNAME records found"
                    reply.header.rcode = RCODE.NXDOMAIN
            else:
                log_msg += ". No records found"
                reply.header.rcode = RCODE.NXDOMAIN
        else:
            log_msg += ". No records found, querying upstream DNS server"
            try:
                upstream_response = self.query_upstream_dns(request)
                logger.info(log_msg)
                return upstream_response
            except Exception as e:
                log_msg += f". Error querying upstream DNS server: {e}"
                reply.header.rcode = RCODE.SERVFAIL

        logger.info(log_msg)
        return reply

    def query_upstream_dns(self, request):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)  # 设置超时时间为5秒
        sock.sendto(request.pack(), self.upstream_dns)
        response, _ = sock.recvfrom(1024)
        sock.close()
        return DNSRecord.parse(response)

    def handle_udp(self):
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.bind((self.host, self.port))
        logger.info("DNS server is listening on %s:%d (UDP)", self.host, self.port)
        while True:
            data, client_address = udp_sock.recvfrom(1024)
            udp_response = self.resolve_udp(data, client_address)
            if udp_response:
                udp_sock.sendto(udp_response, client_address)

    def handle_tcp(self):
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.bind((self.host, self.port))
        tcp_sock.listen(5)
        logger.info("DNS server is listening on %s:%d (TCP)", self.host, self.port)
        while True:
            tcp_connection, _ = tcp_sock.accept()
            tcp_response = self.resolve_tcp(tcp_connection)
            if tcp_response:
                tcp_connection.sendall(tcp_response)
                tcp_connection.close()


if __name__ == '__main__':
    # 设置监听地址和端口
    dns_server_ip = "192.168.204.128"
    dns_port = 53
    upstream_dns_server = ("223.5.5.5", 53)  # 上游 DNS 服务器地址

    handler = DNSHandler(dns_server_ip, dns_port, upstream_dns_server)
    handler.add_record_from_file("./dns_records.txt")

    # 启动UDP和TCP处理线程
    udp_thread = threading.Thread(target=handler.handle_udp)
    tcp_thread = threading.Thread(target=handler.handle_tcp)

    udp_thread.start()
    tcp_thread.start()

    udp_thread.join()
    tcp_thread.join()
