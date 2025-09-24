# Changelog - MRP-9.html (Mobile Receipt Printer)

## [v1.4] - 2025-09-24

### Added
- **MRP-11-main.html**: New user-facing toggle to enable/disable saving receipts as PNG files.
  - Button label: "Save PNG: On/Off" in Quick Start section.
  - Persists state via `localStorage` key `savePNGEnabled` (default: On).
- **MRP-11.html**: PNG receipt export tuned for 58mm thermal printers (203 DPI ≈ 384px width).
  - Canvas width: 384px; margins: 16px; dynamic height.
  - Font: `'Courier New', monospace`; sizes: 14px (normal), 22px (large); line heights: 22/32.
  - Amount line rendered bold + large for emphasis.

### Changed
- **MRP-11.html**: PNG saving is now gated by the main page toggle. When `savePNGEnabled` is Off, no PNG is saved.
- Supersedes prior PRN prototype work in this branch; PNG export is the current approach.

### Technical Notes
- Shared preference key: `savePNGEnabled` (read/write from both main and receipt pages).
- Gating point: `previewReceipt()` only invokes `saveReceiptAsPNG(...)` if `savePNGEnabled` is true.
- Relevant commits (feature/prn-file-generation):
  - dcbcdb4 — Main page PNG toggle + gated saving
  - 6da5c6b — Switch from PRN to PNG generation for 58mm thermal printer
  - 399248d — Initial PRN generator prototype (now superseded)


## [v1.3] - 2025-09-22

### Changed
- **MRP-11.html**: Improved File System Access API user experience. Now prompts for folder selection only once per session. Removed all user-facing folder controls and status indicators for a cleaner interface.
- **MRP-11-main.html**: Removed Termux setup, testing, diagnostics, troubleshooting, and legacy quick actions sections. UI is now focused on core navigation and receipt management.
- **MRP-11-settings.html**: Removed Quick Actions, Testing & Diagnostics, Advanced Settings, QR Code Generator, and scan network functionality. Streamlined for essential server configuration only.
- **.github/copilot-instructions.md**: Added/updated project-specific Copilot instructions for sequential thinking and evidence-based responses.
- **response.txt**: Deleted obsolete sample response file.

### Technical Improvements
- **Dead Code Removal**: Eliminated 255+ lines of unused or legacy code across main, settings, and landing pages.
- **UI Cleanup**: All advanced, diagnostic, and QR code features removed for a simplified, production-ready interface.
- **File Save Logic**: Receipts now save automatically to the chosen folder (or Downloads as fallback) with no user prompt after initial selection.

---

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
*Last Updated: September 22, 2025*