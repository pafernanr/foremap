# Foremap - Foreman/Satellite Configuration Export Tool

A Python tool to export Foreman/Red Hat Satellite configuration data via API.

## Features

- 📊 Export configuration from Foreman/Satellite servers
- 📝 Multiple output formats: Text (tab-separated) or HTML
- 🎨 Beautiful HTML reports with Foreman-inspired design
- 🌲 Dynamic hierarchical navigation tree (Organizations → Endpoints → Objects)
- 📈 Real-time progress bar with ETA
- 🔄 Comprehensive error handling
- 🌐 Automatic browser opening for HTML reports
- 📋 Click-to-copy table cells
- 🔍 Smooth scrolling navigation
- 📱 Responsive design

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install requests jinja2 tqdm
```

## Usage

### Basic Usage (Text Output)
```bash
./foremap.py --server https://satellite.example.com --username admin --password secret
```

### HTML Report (Auto-opens in browser)
```bash
./foremap.py --server https://satellite.example.com --username admin --password secret --output html
```

## Arguments

- `--server` (required): Foreman/Satellite server URL (e.g., https://satellite.example.com)
- `--username` (required): Username for authentication
- `--password` (required): Password for authentication
- `--output` (optional): Output format - `text` (default) or `html`

## Output Formats

### Text Output
- Tab-separated values printed to stdout
- Can be redirected to a file: `./foremap.py ... > output.txt`
- Easy to parse with other tools

### HTML Output
- **Modern Foreman-inspired design** matching theforeman.org look & feel
- **Fixed header** with server information and metadata
- **Left sidebar navigation** with hierarchical tree structure:
  - First level: Organizations
  - Second level: Objects (grouped by endpoint)
  - Expandable/collapsible tree nodes
  - Active item highlighting
  - Smooth scroll to sections
- **Content area** with clean, professional tables
- **Interactive features**:
  - Click any table cell to copy its value
  - Visual feedback on copy (orange highlight)
  - Auto-scroll highlighting of current section
  - Hash-based navigation (shareable URLs)
- **Responsive design** works on desktop and mobile
- Creates temporary directory in `/tmp/foremap_XXXXX/`
- Includes `style.css` for Foreman-style theming
- Includes `foremap.js` for all interactivity
- Automatically opens in default browser
- Files preserved in `/tmp/` for later viewing

## Project Structure

```
foremap/
├── foremap.py              # Main script
├── lib/
│   ├── __init__.py        # Module init
│   └── endpoints.py       # API endpoints configuration
├── templates/
│   ├── index.html.j2      # HTML page template
│   ├── error.text.j2      # Text error template
│   ├── error.html.j2      # HTML error template
│   ├── objects.text.j2    # Text objects template
│   ├── objects.html.j2    # HTML objects template
│   ├── style.css          # CSS styling
│   └── foremap.js         # JavaScript functionality
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Customization

### Modify Endpoints
Edit `lib/endpoints.py` to add/remove API endpoints or modify field configurations.

### Customize HTML Output
- Edit `templates/style.css` to change colors, fonts, layout
- Edit `templates/foremap.js` to add interactive features
- Edit `templates/*.j2` to modify HTML structure

## Error Handling

The tool includes comprehensive error handling:
- **Connection errors**: Checks server availability
- **Timeout errors**: Handles slow/unresponsive servers
- **HTTP errors**: Validates credentials
- **Per-endpoint errors**: Continues processing even if individual endpoints fail

## Examples

### Export all data to HTML
```bash
./foremap.py --server https://satellite.lab.example.com --username admin --password P@ssw0rd --output html
```

### Export to text file
```bash
./foremap.py --server https://satellite.lab.example.com --username admin --password P@ssw0rd > satellite-config.txt
```

## Requirements

- Python 3.6+
- Network access to Foreman/Satellite server
- Valid credentials with read access to API

## Based On

Request classes based on: https://github.com/laspavel/foreman-api/

## License

See project license file.
