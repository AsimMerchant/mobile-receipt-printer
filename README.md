# 📱 Mobile Receipt Printer (MRP) System

A comprehensive web-based receipt printing system designed for mobile devices, featuring Bluetooth printer integration and network-based server communication.

## 🚀 **Latest Version: MRP-11**

The MRP-11 system features a **clean, mobile-first interface** with **separation of concerns** architecture:

### **🎯 System Components:**

1. **📱 MRP-11.html** - Simplified receipt creation interface
   - Clean 3-button design (Create Receipt, Test Print, Manage Names)
   - Mobile-optimized responsive design
   - Focus on core receipt generation functionality

2. **🏠 MRP-11-main.html** - Comprehensive landing page
   - Termux setup guide and installation instructions
   - Version library with access to all MRP versions
   - Biller reports and data management
   - Testing and diagnostics tools

3. **⚙️ MRP-11-settings.html** - Advanced server configuration
   - Server auto-detection and manual configuration
   - Network diagnostics and connection testing
   - Settings import/export functionality
   - Advanced configuration options

## 📋 **Features**

### **Core Functionality:**
- ✅ **Receipt Generation** - Create formatted receipts with biller, volunteer, and amount data
- ✅ **Bluetooth Printing** - Direct integration with Bluetooth thermal printers
- ✅ **Data Persistence** - Local storage of receipt data and biller information
- ✅ **Server Communication** - Network-based API for receipt processing
- ✅ **Mobile Optimization** - Responsive design for Android smartphones

### **Advanced Features:**
- ✅ **Auto-Detection** - WebRTC-based IP and hostname detection
- ✅ **Report Generation** - Download individual or combined biller reports
- ✅ **Data Management** - View, export, and clear stored receipt data
- ✅ **Connection Testing** - Comprehensive server and network diagnostics
- ✅ **Settings Management** - Import/export configuration for backup

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

### **1. Server Setup (Termux)**
```bash
# Install Termux from F-Droid
# Install PHP
pkg update && pkg install php

# Navigate to your files
cd /storage/emulated/0/

# Start PHP server
php -S 0.0.0.0:8080
```

### **2. Access the System**
- **Main Interface:** `http://[phone-ip]:8080/MRP-11.html`
- **Landing Page:** `http://[phone-ip]:8080/MRP-11-main.html`
- **Settings:** `http://[phone-ip]:8080/MRP-11-settings.html`

### **3. First Time Setup**
1. Open `MRP-11-main.html` for setup guidance
2. Configure server settings if needed
3. Test connection and printer functionality
4. Start creating receipts with `MRP-11.html`

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