
import qrcode
import matplotlib.pyplot as plt

# Take input
data = input("Enter text or URL: ")

# Generate QR
qr = qrcode.make(data)

# Show inside VS Code
plt.imshow(qr)
plt.axis("off")   # Hide axis
plt.title("Generated QR Code")
plt.show()

 


