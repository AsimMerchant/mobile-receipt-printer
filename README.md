# 📱 Mobile Receipt Printer (MRP) System

A streamlined web-based receipt printing system for mobile devices, featuring Bluetooth printer integration and network-based server communication.

---

## 🚀 **Latest Update: September 2025**

- **Minimal, distraction-free UI:** Only core receipt creation and navigation remain. All advanced, diagnostic, QR code, and test print features have been removed for simplicity and reliability.
- **Automatic receipt saving:** Receipts are saved directly to your chosen folder using the File System Access API. The folder selection prompt appears only once per browser session—no user-facing folder controls or status indicators.
- **Landing and settings pages:** Now focused solely on navigation and essential server configuration. All setup guides, troubleshooting, and advanced options have been removed.
- **No Termux/Android-specific setup required:** The system works in any modern browser (Chrome/Edge recommended for folder saving). The Termux setup guide and related instructions have been removed from the UI.

---

## **System Components:**

1. **📱 MRP-11.html** - Receipt creation interface
   - Clean, mobile-optimized design
   - Focused on core receipt generation
   - Automatic file saving (no user controls)

2. **🏠 MRP-11-main.html** - Landing page
   - Simple navigation to receipt and settings
   - Biller reports and data management

3. **⚙️ MRP-11-settings.html** - Server configuration
   - Manual and auto-detection of server address
   - No advanced/diagnostic/QR features

## 📋 **Features**

### **Core Functionality:**
- ✅ **Receipt Generation** - Create formatted receipts with biller, volunteer, and amount data
- ✅ **Bluetooth Printing** - Direct integration with Bluetooth thermal printers
- ✅ **Data Persistence** - Local storage of receipt data and biller information
- ✅ **Server Communication** - Network-based API for receipt processing
- ✅ **Mobile Optimization** - Responsive design for Android smartphones
- ✅ **Automatic File Saving** - Receipts are saved directly to your chosen folder (one-time prompt per session, no user controls)

## 📥 **Quick Download**

Get all files for your Mobile Receipt Printer system:

<div align="center">

### **Download Options**

**📦 Complete Repository (Recommended)**

<a href="https://github.com/AsimMerchant/mobile-receipt-printer/archive/refs/heads/master.zip">
<img src="https://img.shields.io/badge/Download_ZIP-Complete_Project-4CAF50?style=for-the-badge&logo=download&logoColor=white" alt="Download Complete Project"/>
</a>

**📱 Individual Files** *(Right-click → Save link as...)*

| File | Purpose | Download Link |
|------|---------|---------------|
| 📱 **MRP-11.html** | Main Receipt Interface | [Download](https://raw.githubusercontent.com/AsimMerchant/mobile-receipt-printer/master/MRP-11.html) |
| 🏠 **MRP-11-main.html** | Landing Page & Setup Guide | [Download](https://raw.githubusercontent.com/AsimMerchant/mobile-receipt-printer/master/MRP-11-main.html) |
| ⚙️ **MRP-11-settings.html** | Advanced Configuration | [Download](https://raw.githubusercontent.com/AsimMerchant/mobile-receipt-printer/master/MRP-11-settings.html) |
| 🔧 **response.php** | Server API Backend | [Download](https://raw.githubusercontent.com/AsimMerchant/mobile-receipt-printer/master/response.php) |
| 📊 **MRP-10.html** | Legacy Version 10 | [Download](https://raw.githubusercontent.com/AsimMerchant/mobile-receipt-printer/master/MRP-10.html) |
| 📋 **MRP-9.html** | Original Version | [Download](https://raw.githubusercontent.com/AsimMerchant/mobile-receipt-printer/master/MRP-9.html) |

> **💡 Download Tip:** Right-click any download link above and select "Save link as..." to download the file directly to your device.

</div>

## 🛠 **Technical Stack**

- **Frontend:** HTML5, CSS3 (Glass-morphism design), Vanilla JavaScript
- **Backend:** PHP (response.php API endpoint)
- **Server:** PHP Built-in server or Apache/Nginx
- **Storage:** Browser localStorage for client-side data persistence
- **Communication:** Fetch API for server communication
- **Printing:** Bluetooth URL schemes for printer integration

## 📱 **Mobile Requirements**

- **Android Device** with Termux app
- **PHP Server** running on device (port 8080)
- **Bluetooth Thermal Printer** (ESC/POS compatible)
- **WiFi Network** for device communication

## 🚀 **Quick Start**

1. **Open MRP-11-main.html** in a modern browser (Chrome/Edge recommended)
2. **Select your receipt folder** when prompted (first receipt creation only)
3. **Configure server settings** if needed (MRP-11-settings.html)
4. **Create receipts** with MRP-11.html

> **Note:** All advanced, diagnostic, QR code, and test print features have been removed for a streamlined experience. The system is now focused on fast, reliable receipt creation and saving.

## 📊 **Version History**

| Version | Description | Key Features |
|---------|-------------|--------------|
| **MRP-11** | Simplified UI with separation of concerns | Clean interface, mobile-first, advanced settings |
| MRP-10 | Enhanced functionality | Improved features and stability |
| MRP-9 | Original version | Basic receipt printing functionality |

## 🔧 **Configuration**

### **Server Settings:**
- **Default Port:** 8080
- **API Endpoint:** `/response.php`
- **Server Address:** Auto-detected or manually configured
- **Connection Timeout:** 5 seconds (configurable)

### **Storage:**
- **Receipt Data:** Stored per biller in localStorage
- **Server Settings:** Persistent configuration storage
- **Name Lists:** Auto-completion for billers and volunteers

## 📖 **Documentation**

- **📋 MRP-11-Checklist.md** - Development progress and testing checklist
- **📝 Setup Guides** - Comprehensive installation and configuration guides
- **🔍 Troubleshooting** - Common issues and solutions built into landing page

## 🔒 **Security Notes**

- Server runs on local network only
- No external dependencies or cloud services
- All data stored locally on device
- HTTPS recommended for production use

## 🤝 **Contributing**

This is a specialized mobile receipt printing system. For issues or enhancements:

1. Check the built-in diagnostics tools
2. Review the troubleshooting guide
3. Test with different network configurations
4. Verify printer compatibility

## 📄 **License**

This project is designed for personal and small business use. Modify as needed for your specific requirements.

## 🏷️ **Tags**

`mobile-receipt-printer` `bluetooth-printing` `php-server` `termux` `android-app` `receipt-generation` `pos-system` `thermal-printer` `mobile-web-app` `javascript`

---

**🎯 Ready to print receipts on the go!** 📱🖨️