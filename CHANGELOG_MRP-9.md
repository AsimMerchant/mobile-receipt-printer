# Changelog - MRP-9.html (Mobile Receipt Printer)

## [v1.2] - 2025-09-11

### Added
- **Test Print Feature**: Comprehensive testing functionality for printer connectivity
  - Auto-fills form with dummy test data
  - Automatically creates receipt preview
  - Triggers Bluetooth print workflow
  - Tests complete end-to-end functionality
- **Enhanced Hostname Detection**: Improved WebRTC-based hostname discovery
  - Added filtering for network metadata (network-cost, ufrag)
  - Better validation to prevent false positives
  - Debug capabilities for troubleshooting detection issues

### Enhanced
- **Hostname Detection Reliability**: 
  - Filters out ICE candidate metadata that was causing false detections
  - Prevents single characters and short strings from being detected as hostnames
  - Added validation for minimum hostname length requirements

### Fixed
- **Hostname Detection Bug**: Resolved issue where "k" was being detected from "network-cost" metadata
- **Port Validation**: Added proper port number validation (1-65535 range)
- **False Positive Filtering**: Enhanced filtering to ignore WebRTC technical data

### Technical Improvements
- **Debug Functionality**: Temporarily added debugging alerts to identify hostname detection issues
- **Code Cleanup**: Removed debug logging for production use
- **Validation Enhancement**: Improved input validation and error handling

---

## [v1.1] - 2025-09-11

### Changed
- **Server Address Input**: Enhanced server configuration to support both IP addresses and hostnames
- **User Interface Labels**: Updated terminology from IP-specific to generic address terminology
- **Input Validation Messages**: Modified alert messages to reflect hostname support

### Added
- **Hostname Support**: System now accepts hostnames in addition to IP addresses
  - Examples: `my-computer.local`, `desktop-pc`, `server01.domain.com`
- **Enhanced Placeholder Text**: Shows both IP and hostname examples for better user guidance
- **Backwards Compatibility**: Existing IP addresses in localStorage continue to work

### Technical Changes
- **Input Field Updates**:
  - Label: "Server IP Address:" → "Server Address:"
  - Placeholder: `"e.g., 192.168.1.100"` → `"e.g., 192.168.1.100 or my-computer.local"`
  - Alert: `"Please enter a server IP address."` → `"Please enter a server address (IP or hostname)."`

### Supported Address Formats
**IP Addresses (Existing):**
- `192.168.1.100`
- `10.0.0.5`
- `127.0.0.1`

**Hostnames (New):**
- `my-computer`
- `desktop-pc`
- `my-computer.local`
- `printer-server.domain.com`

### URL Construction
The system constructs valid URLs for both formats:
- **IP**: `http://192.168.1.100:8080/response.php`
- **Hostname**: `http://my-computer.local:8080/response.php`

### Backwards Compatibility
- ✅ Existing IP addresses stored in localStorage continue to work
- ✅ "Use My IP" button functionality unchanged
- ✅ All existing features and workflows preserved
- ✅ No migration required for existing users

### Benefits
- **Easier Network Configuration**: Users can use memorable hostnames instead of IP addresses
- **Network Flexibility**: Works across different network configurations
- **User-Friendly**: Hostnames are easier to remember and share
- **Professional Setup**: Supports enterprise environments with DNS/mDNS

### Future Considerations
- Hostname resolution depends on network DNS/mDNS configuration
- Local network discovery protocols (Bonjour/Zeroconf) may be utilized
- Consider adding hostname validation in future versions

---

## [v1.0] - Initial Release
### Features
- Mobile receipt printing interface
- Bluetooth printer integration
- Local server communication
- IP address configuration
- Receipt preview and sharing
- Biller and volunteer name management
- Local data storage and reporting

---
*Changelog maintained by: Development Team*
*Last Updated: September 11, 2025*