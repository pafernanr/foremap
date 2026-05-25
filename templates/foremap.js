// Foreman/Satellite Configuration Export JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Foremap report loaded');

    // Build navigation tree from sections
    buildNavigationTree();

    // Add click-to-copy functionality for table cells
    addClickToCopy();

    // Handle hash navigation
    handleHashNavigation();
});

/**
 * Build the hierarchical navigation tree
 */
function buildNavigationTree() {
    const treeMenu = document.getElementById('tree-menu');
    const orgMap = new Map();

    // Build tree structure from embedded data
    if (!window.foremapData) {
        console.error('No foremap data found');
        return;
    }

    // Parse foremapData to build organization structure
    Object.entries(window.foremapData).forEach(([sectionId, dataObj]) => {
        const orgName = dataObj.org_name;
        const endpoint = dataObj.endpoint;
        const object = dataObj.object;

        if (!orgMap.has(orgName)) {
            orgMap.set(orgName, {
                name: orgName,
                endpoints: new Map()
            });
        }

        const org = orgMap.get(orgName);
        if (!org.endpoints.has(endpoint)) {
            org.endpoints.set(endpoint, []);
        }

        org.endpoints.get(endpoint).push({
            object: object,
            sectionId: sectionId,
            displayName: object.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())
        });
    });

    // Sort organizations alphabetically (Level 1)
    const sortedOrgs = Array.from(orgMap.entries()).sort((a, b) =>
        a[1].name.localeCompare(b[1].name)
    );

    // Build HTML tree with 3 levels
    sortedOrgs.forEach(([orgId, org]) => {
        // Level 1: Organization (expandable)
        const orgItem = document.createElement('li');
        orgItem.className = 'tree-item';
        orgItem.innerHTML = `
            <div class="tree-label">${org.name}</div>
            <ul class="tree-children"></ul>
        `;

        const orgChildren = orgItem.querySelector('.tree-children');

        // Sort endpoints alphabetically (Level 2)
        const sortedEndpoints = Array.from(org.endpoints.entries()).sort((a, b) =>
            a[0].localeCompare(b[0])
        );

        // Level 2: Endpoint/Object Type (expandable)
        sortedEndpoints.forEach(([endpoint, objects]) => {
            const endpointItem = document.createElement('li');
            endpointItem.className = 'tree-item';
            endpointItem.innerHTML = `
                <div class="tree-label">${endpoint}</div>
                <ul class="tree-children"></ul>
            `;

            const endpointChildren = endpointItem.querySelector('.tree-children');

            // Sort objects alphabetically (Level 3)
            const sortedObjects = objects.sort((a, b) =>
                a.displayName.localeCompare(b.displayName)
            );

            // Level 3: Object names (leaf nodes)
            sortedObjects.forEach(obj => {
                const objItem = document.createElement('li');
                objItem.innerHTML = `
                    <a href="#${obj.sectionId}"
                       data-section="${obj.sectionId}">
                        ${obj.displayName}
                    </a>
                `;
                endpointChildren.appendChild(objItem);
            });

            orgChildren.appendChild(endpointItem);
        });

        treeMenu.appendChild(orgItem);
    });

    // Add toggle functionality for all tree labels (levels 1 and 2)
    document.querySelectorAll('.tree-label').forEach(label => {
        label.addEventListener('click', function() {
            this.parentElement.classList.toggle('expanded');
            // Adjust content position in case sidebar width changed
            setTimeout(() => adjustContentPosition(), 10);
        });
    });

    // Expand all level-1 items (organizations) by default
    const allOrgs = treeMenu.querySelectorAll(':scope > .tree-item');
    allOrgs.forEach(org => {
        org.classList.add('expanded');
    });

    // Adjust content area position based on actual sidebar width
    adjustContentPosition();
}

/**
 * Adjust content area position to match sidebar width
 */
function adjustContentPosition() {
    const sidebar = document.querySelector('.sidebar');
    const content = document.querySelector('.content');

    if (sidebar && content) {
        // Get the actual width of the sidebar after rendering
        const sidebarWidth = sidebar.offsetWidth;

        // Update content area's margin to start where sidebar ends
        // (left is handled by CSS as fixed position from viewport)
        content.style.marginLeft = `${sidebarWidth}px`;
    }
}

/**
 * Add click-to-copy functionality for table cells in a given element
 */
function addClickToCopyToElement(element) {
    const tables = element.querySelectorAll('table');
    tables.forEach(table => {
        table.addEventListener('click', function(e) {
            if (e.target.tagName === 'TD') {
                const text = e.target.textContent;
                if (text && text.trim()) {
                    navigator.clipboard.writeText(text).then(() => {
                        // Visual feedback
                        const originalBg = e.target.style.backgroundColor;
                        e.target.style.backgroundColor = '#e67e22';
                        e.target.style.color = 'white';
                        setTimeout(() => {
                            e.target.style.backgroundColor = originalBg;
                            e.target.style.color = '';
                        }, 300);
                    }).catch(err => {
                        console.log('Copy failed:', err);
                    });
                }
            }
        });
    });
}

/**
 * Add click-to-copy functionality for table cells (legacy - kept for backward compatibility)
 */
function addClickToCopy() {
    addClickToCopyToElement(document);
}

/**
 * Handle hash navigation and load content from embedded data
 */
function handleHashNavigation() {
    // Load content when link is clicked
    document.querySelectorAll('.tree-children a[data-section]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const sectionId = this.dataset.section;

            if (sectionId) {
                // Update active state
                document.querySelectorAll('.tree-children a').forEach(a => a.classList.remove('active'));
                this.classList.add('active');

                // Load content from embedded data
                loadContent(sectionId);

                // Update URL hash
                history.pushState(null, null, `#${sectionId}`);
            }
        });
    });

    // Handle initial hash on page load
    if (window.location.hash) {
        const hash = window.location.hash.substring(1);
        const link = document.querySelector(`a[data-section="${hash}"]`);
        if (link) {
            setTimeout(() => {
                link.click();
            }, 100);
        }
    }
}

/**
 * Load content from embedded data (no file loading - avoids CORS)
 */
function loadContent(sectionId) {
    const contentArea = document.getElementById('main-content');

    // Get data from embedded object
    const dataObj = window.foremapData[sectionId];

    if (!dataObj) {
        contentArea.innerHTML = `
            <div class="error">
                <h3>Error Loading Content</h3>
                <p>No data found for section: ${sectionId}</p>
            </div>
        `;
        return;
    }

    // Check if this is an error response
    if (dataObj.error) {
        contentArea.innerHTML = `
            <div class="error">
                <h3>Error</h3>
                <p><strong>Organization:</strong> ${dataObj.org_name}</p>
                <p><strong>Endpoint:</strong> ${dataObj.endpoint}</p>
                <p><strong>Object:</strong> ${dataObj.object}</p>
                <p><strong>Status:</strong> ${dataObj.status}</p>
                <p><strong>Error:</strong> ${dataObj.error_message}</p>
            </div>
        `;
        return;
    }

    // Generate HTML from data
    const html = generateTableFromData(dataObj);
    contentArea.innerHTML = html;

    // Re-apply click-to-copy functionality for the new content
    addClickToCopyToElement(contentArea);
}

/**
 * Generate HTML table from embedded data object
 * (Data is already sorted and field-ordered by Python)
 */
function generateTableFromData(dataObj) {
    const objectTitle = dataObj.object.replace(/_/g, ' ')
        .replace(/\b\w/g, l => l.toUpperCase());

    let html = `
        <div class="object-section">
            <h2>${objectTitle}</h2>
            <div class="section-info">
                Organization: <strong>${dataObj.org_name}</strong> (ID: ${dataObj.org_id}) |
                Endpoint: <strong>${dataObj.endpoint}</strong> |
                Records: <strong>${dataObj.record_count}</strong>
            </div>
    `;

    // Check if we have data to display
    if (!dataObj.fields || dataObj.fields.length === 0 || !dataObj.rows || dataObj.rows.length === 0) {
        html += `
            <div class="table-wrapper">
                <p style="padding: 20px; text-align: center; color: #7f8c8d;">
                    No data available
                </p>
            </div>
        `;
    } else {
        // Data is already sorted and fields are already ordered by Python
        html += `
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
        `;

        // Add table headers (already ordered)
        dataObj.fields.forEach(field => {
            html += `<th>${escapeHtml(field)}</th>`;
        });

        html += `
                        </tr>
                    </thead>
                    <tbody>
        `;

        // Add table rows (already sorted)
        dataObj.rows.forEach(row => {
            html += '<tr>';
            dataObj.fields.forEach(field => {
                const value = row[field] !== undefined ? row[field] : '';
                html += `<td>${escapeHtml(String(value))}</td>`;
            });
            html += '</tr>';
        });

        html += `
                    </tbody>
                </table>
            </div>
        `;
    }

    html += '</div>';

    return html;
}

/**
 * Escape HTML special characters
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

