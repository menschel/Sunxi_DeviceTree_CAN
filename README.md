# Sunxi_DeviceTree_CAN
Enable CAN via device tree on Sunxi Platform with mainline kernel

# Patching the board file
As SUNXI kernel repositories do not feature device tree overlays
like the raspberry pi repos do, this is a quick hack to activate CAN
for the board by patching the board file.

# Using the device tree overlay
The other way is to use the device tree overlay for the CAN bus. 
