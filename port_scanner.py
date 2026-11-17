import socket
import streamlit as st

st.title("Network Port Scanner")
st.write("A simple tool for checking port connectivity on authorized systems.")

target = st.text_input("Enter the hostname or IP address to scan:")

if st.button("Start Scan"):
    if target:
        connect = target

        st.subheader("Port Scanner Results")
        st.info("Scanning ports 22, 80, 443, 21, 53")

        ports = 22, 80, 443, 21, 53

        total = 0
        open_ports = 0
        close_ports = 0

        for p in ports:
            total += 1

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)

            result = s.connect_ex((connect, p))

            if result == 0:
                open_ports += 1
                st.success(f"Port {p} is open")

                if p == 22:
                    st.write("Service: SSH")
                elif p == 80:
                    st.write("Service: HTTP")
                elif p == 443:
                    st.write("Service: HTTPS")
                elif p == 21:
                    st.write("Service: FTP")
                elif p == 53:
                    st.write("Service: DNS")

            else:
                close_ports += 1
                st.warning(f"Port {p}: Connection failed")

            s.close()

        st.subheader("Scan Summary")
        st.write("Total ports checked:", total)
        st.write("Open ports:", open_ports)
        st.write("Failed connections:", close_ports)

    else:
        st.warning("Please enter a valid hostname or IP address.")