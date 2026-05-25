#!/usr/bin/python3
"""
Foreman API mapper - exports Foreman/Satellite configuration.
Request related classes based on https://github.com/laspavel/foreman-api/
"""
import argparse
import os
import shutil
import sys
import tempfile
import webbrowser
from datetime import datetime
from urllib.parse import urljoin

import urllib3
import requests
from jinja2 import Environment
from jinja2 import FileSystemLoader
from requests.auth import HTTPBasicAuth
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import Timeout
from tqdm import tqdm

from lib.endpoints import endpoints

# Set up Jinja2 environment (module level)
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=True,
    lstrip_blocks=True
)


class Foremap:

    def __init__(self, apihost, apiuri, login, pwd):
        """Initialize Foremap API client."""
        # Connect to foreman server
        self.apihost = apihost
        self.apiuri = apiuri
        self.login = login
        self.password = pwd
        # TODO(disable_warnings): disable only InsecureRequestWarning
        urllib3.disable_warnings()
        self.auth = HTTPBasicAuth(login, pwd)

    def __getattr__(self, attribute):
        return ForemapAPIObject(attribute, self)

    def api_request(self, api_method='', **params):
        """Make an API request to Foreman/Satellite."""
        api_method_url = urljoin(f"{self.apihost}{self.apiuri}", api_method)
        fapi = requests.get(
            api_method_url, verify=False, auth=self.auth, timeout=90,
            params=params, headers={'Accept': 'application/json'},
            allow_redirects=True).json()
        return fapi

    def print_obj(self, context, records, print_fn=print):
        """Print or save object data.

        Args:
            context: Dictionary containing endpoint, org_id, org_name, obj,
                     attr, output_format, output_dir, file_map
            records: API response records
            print_fn: Function to use for printing (default: print)
        """
        # pylint: disable=too-many-branches
        endpoint = context['endpoint']
        org_id = context['org_id']
        org_name = context['org_name']
        obj = context['obj']
        attr = context['attr']
        output_format = context.get('output_format', 'text')
        output_dir = context.get('output_dir')
        file_map = context.get('file_map')

        if "error" in records and records['error'] is not None:
            if records['status'] != 404:
                tmpl = jinja_env.get_template(f'error.{output_format}.j2')
                output = tmpl.render(
                    org_name=org_name,
                    org_id=org_id,
                    endpoint=endpoint,
                    obj=obj,
                    status=records['status'],
                    error=records['error']
                )
                if output_format == 'html' and output_dir is not None:
                    # Create individual HTML file
                    self._write_html_file(org_id, org_name, endpoint, obj,
                                          output, output_dir, file_map)
                else:
                    print_fn(output)
        elif len(records['results']) > 0:
            if len(attr['fields']) == 0:
                attr['fields'] = list(records['results'][0].keys())

            # Process records into structured data
            rows = []
            for record in records['results']:
                fields = {}
                for name in attr['fields']:
                    if name in record.keys():
                        val = ""
                        if name in attr['dicts']:
                            val = record[name]['name'] if record[name] else ""
                        elif name in attr['lists']:
                            val = ",".join(str(item) for item in record[name])
                        elif name in attr['listdicts']:
                            val = ",".join(
                                [item['name'] for item in record[name]]
                            )
                        else:
                            val = record[name]
                        fields[name] = val
                rows.insert(0, fields)

            tmpl = jinja_env.get_template(f'objects.{output_format}.j2')
            output = tmpl.render(
                org_name=org_name,
                org_id=org_id,
                endpoint=endpoint,
                obj=obj,
                field_names=attr['fields'],
                rows=rows
            )
            if output_format == 'html' and output_dir is not None:
                # Create individual HTML file
                self._write_html_file(org_id, org_name, endpoint, obj,
                                      output, output_dir, file_map)
            else:
                print_fn(output)

    def _write_html_file(self, org_id, org_name, endpoint, obj_name,
                         content, output_dir, file_map):
        """Write individual HTML file for an object."""
        # pylint: disable=too-many-arguments,too-many-positional-arguments
        # Sanitize names for file paths
        safe_org = org_name.replace(' ', '_').replace('/', '_')
        safe_endpoint = endpoint.replace(' ', '_').replace('/', '_')
        safe_obj = obj_name.replace(' ', '_').replace('/', '_')

        # Create directory structure: output_dir/org/endpoint/
        obj_dir = os.path.join(output_dir, safe_org, safe_endpoint)
        os.makedirs(obj_dir, exist_ok=True)

        # Create file path
        file_path = os.path.join(obj_dir, f"{safe_obj}.html")

        # Write the HTML content
        with open(file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(content)

        # Store relative path for JavaScript (use same section_id format as template)
        if file_map is not None:
            section_id = f"{org_id}-{endpoint}-{obj_name}"
            rel_path = os.path.join(safe_org, safe_endpoint, f"{safe_obj}.html")
            file_map[section_id] = rel_path


class ForemapAPIObject:  # pylint: disable=too-few-public-methods
    """Dynamic API object for Foreman API calls."""

    def __init__(self, name, parent):
        """Initialize API object."""
        self.name = name
        self.parent = parent

    def __getattr__(self, attribute):
        """Create dynamic API method wrapper."""
        def wrapper(*_args, **kw):
            return self.parent.api_request(
                api_method=str(attribute),
                **kw)
        return wrapper


def main():  # pylint: disable=too-many-branches,too-many-statements
    """Main function to run Foremap."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Foreman API mapper - exports Foreman/Satellite configuration'
    )
    parser.add_argument(
        '--server', required=True,
        help='Foreman/Satellite server URL (e.g., https://satellite.example.com)'
    )
    parser.add_argument(
        '--username', required=True,
        help='Username for authentication'
    )
    parser.add_argument(
        '--password', required=True,
        help='Password for authentication'
    )
    parser.add_argument(
        '--output', choices=['text', 'html'], default='text',
        help='Output format: text or html (default: text)'
    )
    args = parser.parse_args()

    server = args.server
    username = args.username
    user_password = args.password
    output_format = args.output

    # Storage for HTML output - will be individual files in HTML mode
    html_file_map = {}  # Maps section IDs to file paths

    # get organizations
    orgs = {}
    fm_foreman = Foremap(server, endpoints['foreman']['uri'], username, user_password)

    try:
        print(f"Connecting to {server}...")
        api_records = fm_foreman.get.organizations()
        for org_record in api_records['results']:
            orgs[org_record['id']] = org_record['name']
        print(f"Successfully connected. Found {len(orgs)} organization(s).")
    except RequestsConnectionError as conn_err:
        print(f"\n❌ Connection Error: Unable to connect to {server}")
        print("   Please check that:")
        print("   - The server is running and accessible")
        print("   - The hostname/URL is correct")
        print("   - You have network connectivity")
        print("   - No firewall is blocking the connection")
        print(f"\n   Technical details: {conn_err}")
        sys.exit(1)
    except Timeout:
        print(f"\n❌ Timeout Error: Connection to {server} timed out")
        print("   The server might be slow or unresponsive.")
        sys.exit(1)
    except requests.exceptions.HTTPError as http_err:
        print(f"\n❌ HTTP Error: {http_err}")
        print("   Please check your credentials (username/password)")
        sys.exit(1)
    except Exception as ex:
        print(f"\n❌ Unexpected Error: {ex}")
        print(f"   Type: {type(ex).__name__}")
        sys.exit(1)

    # Calculate total number of requests
    total_requests = sum(
        len(details['objects']) * len(orgs)
        for details in endpoints.values()
    )

    print(f"\nFetching data from {total_requests} endpoints "
          f"across {len(orgs)} organization(s)...\n")

    # Create output directory for HTML mode
    temp_dir = None
    if output_format == 'html':
        temp_dir = tempfile.mkdtemp(prefix='foremap_', dir='/tmp')

    # get the endpoints for each organization with progress bar
    print()  # Blank line before progress starts

    # Create progress bar on first line
    pbar = tqdm(total=total_requests, unit="req", dynamic_ncols=True, position=0,
                bar_format='{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} '
                           '[{elapsed}<{remaining}, {rate_fmt}]')

    # Create status line display on second line
    status_bar = tqdm(total=0, position=1, bar_format='{desc}', leave=False)

    try:
        for api_endpoint, details in endpoints.items():
            fm_api = Foremap(server, details['uri'], username, user_password)
            for org_id, org_name in orgs.items():
                for obj_name, obj_attr in details['objects'].items():
                    # Update status line with current request BEFORE making the request
                    status_bar.set_description_str(
                        f"[{api_endpoint}] {org_name}: {obj_name}"
                    )
                    status_bar.refresh()  # Force display update immediately

                    # katello API doesn't support 'all' so using 999999
                    try:
                        # Use getattr instead of eval for safety
                        api_method = getattr(fm_api.get, obj_name)
                        api_records = api_method(organization_id=org_id, per_page=999999)

                        context = {
                            'endpoint': api_endpoint,
                            'org_id': org_id,
                            'org_name': org_name,
                            'obj': obj_name,
                            'attr': obj_attr,
                            'output_format': output_format,
                            'output_dir': temp_dir,
                            'file_map': html_file_map
                        }
                        fm_api.print_obj(context, api_records, tqdm.write)
                    except RequestsConnectionError:
                        tqdm.write(f"⚠️  Connection lost while fetching "
                                   f"'{obj_name}' at {details['uri']}")
                    except Timeout:
                        tqdm.write(f"⚠️  Timeout while fetching "
                                   f"'{obj_name}' at {details['uri']}")
                    except Exception as exc:
                        tqdm.write(f"⚠️  ERROR: '{obj_name}' at "
                                   f"{details['uri']}: {exc}")
                    finally:
                        # Update progress bar
                        pbar.update(1)
    finally:
        # Close both progress bars
        status_bar.close()
        pbar.close()

    print("\n✅ Data collection completed!")

    # If HTML output, generate files and open browser
    if output_format == 'html':
        # Copy CSS and JS files to temp directory
        shutil.copy(
            os.path.join(TEMPLATE_DIR, 'style.css'),
            os.path.join(temp_dir, 'style.css')
        )
        shutil.copy(
            os.path.join(TEMPLATE_DIR, 'foremap.js'),
            os.path.join(temp_dir, 'foremap.js')
        )

        # Generate the complete HTML page using Jinja2 template
        index_template = jinja_env.get_template('index.html.j2')
        html_content = index_template.render(
            server=server,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            output_dir=temp_dir,
            file_map=html_file_map
        )

        # Write the HTML file
        index_path = os.path.join(temp_dir, 'index.html')
        with open(index_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"HTML output generated in: {temp_dir}")
        print(f"Opening {index_path} in browser...")

        # Open in default browser
        webbrowser.open(f'file://{index_path}')


if __name__ == '__main__':
    main()
