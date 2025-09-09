import speedtest as st

def test_speed():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 1_000_000, 2)  # Convert to Mbps and round to 2 decimal places
    print(f"Download Speed: {down_speed} Mbps")

    up_speed = test.upload()
    up_speed = round(up_speed / 1_000_000, 2)  # Convert to Mbps and round to 2 decimal places
    print(f"Upload Speed: {up_speed} Mbps")

    ping_result = test.results.ping
    print(f"Ping: {ping_result} ms")

test_speed()