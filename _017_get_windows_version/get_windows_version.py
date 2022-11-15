
import wmi

# Create the Windows Management Instrumentation (WMI) object
windows_data = wmi.WMI()

# Output the data
for data in windows_data.Win32_OperatingSystem():
    print(data)