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

    // Build tree structure from fileMap
    if (!window.fileMap) {
        console.error('No file map found');
        return;
    }

    // Parse fileMap to build organization structure
    Object.entries(window.fileMap).forEach(([sectionId, filePath]) => {
        // sectionId format: "orgName-endpoint-object"
        const parts = sectionId.split('-');
        if (parts.length < 3) return;

        const orgName = parts[0];
        const endpoint = parts[1];
        const object = parts.slice(2).join('-');  // Handle objects with dashes in name

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
            filePath: filePath,
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
                       data-section="${obj.sectionId}"
                       data-file="${obj.filePath}">
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
        });
    });

    // Expand first organization and first endpoint by default
    const firstOrg = treeMenu.querySelector('.tree-item');
    if (firstOrg) {
        firstOrg.classList.add('expanded');
        const firstEndpoint = firstOrg.querySelector('.tree-children .tree-item');
        if (firstEndpoint) {
            firstEndpoint.classList.add('expanded');
        }
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
 * Handle hash navigation and load HTML files
 */
function handleHashNavigation() {
    // Load HTML file when link is clicked
    document.querySelectorAll('.tree-children a[data-file]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const sectionId = this.dataset.section;
            const filePath = this.dataset.file;

            if (filePath) {
                // Update active state
                document.querySelectorAll('.tree-children a').forEach(a => a.classList.remove('active'));
                this.classList.add('active');

                // Load the HTML file
                loadContent(filePath);

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
 * Load HTML content from file
 */
function loadContent(filePath) {
    const contentArea = document.getElementById('main-content');

    // Show loading indicator
    contentArea.innerHTML = '<div class="loading">Loading...</div>';

    // Fetch the HTML file
    fetch(filePath)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(html => {
            contentArea.innerHTML = html;

            // Re-apply click-to-copy functionality for the new content
            addClickToCopyToElement(contentArea);
        })
        .catch(error => {
            console.error('Error loading content:', error);
            contentArea.innerHTML = `
                <div class="error">
                    <h3>Error Loading Content</h3>
                    <p>Failed to load content from: ${filePath}</p>
                    <p>${error.message}</p>
                </div>
            `;
        });
}

