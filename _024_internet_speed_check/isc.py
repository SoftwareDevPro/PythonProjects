
import speedtest

st = speedtest.Speedtest()

def bytes_to_megabytes(bytes):
    kilobytes = 1024
    megabytes = kilobytes * 1024
    return bytes / megabytes

down_speed = bytes_to_megabytes(st.download())
print(f"Your download speed is {round(down_speed,2)} MB")
