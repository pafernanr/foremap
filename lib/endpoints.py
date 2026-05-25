# Foreman/Satellite API endpoints configuration

endpoints = {
    "ansible": {
        "uri": "/ansible/api/",
        "objects": {
            "ansible_roles": {
                "fields": [],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "ansible_variables": {
                "fields": [],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
        },
    },
    "foreman": {
        "uri": "/api/",
        "objects": {
            "compute_profiles": {
                "fields": ["id", "name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "compute_resources": {
                "fields": ["id", "name", "provider"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "hostgroups": {
                "fields": [
                    "id", "name", "architecture_name", "compute_profile_name",
                    "compute_resource_name", "domain_name", "medium_name",
                    "openscap_proxy", "openscap_proxy_name",
                    "operatingsystem_name", "parent_name", "ptable_name",
                    "puppet_ca_proxy", "puppet_ca_proxy_name", "puppet_proxy",
                    "puppet_proxy_name", "pxe_loader", "realm_name",
                    "subnet6_name", "subnet_name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "locations": {
                "fields": ["id", "name", "parent_id", "parent_name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "plugins": {
                "fields": ["id", "name", "version"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "settings": {
                "fields": ["id", "category", "category_name", "name", "value"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "smart_proxies": {
                "fields": [
                    "id", "name", "download_policy", "lifecycle_environments",
                    "features", "hosts_count"],
                "dicts": [],
                "listdicts": ["lifecycle_environments", "features"],
                "lists": [],
                },
            "subnets": {
                "fields": [
                    "id", "name", "network_address", "network_type", "cidr",
                    "mask", "gateway", "dns_primary", "dns_secondary", "from",
                    "to", "ipam", "boot_mode", "dhcp_name", "tftp_name",
                    "httpboot_name", "externalipam_name", "template_name",
                    "bmc_name", "discovery_name", "dhcp", "tftp", "httpboot",
                    "externalipam", "dns", "template", "bmc", "discovery"],
                "dicts": [
                    "dhcp", "tftp", "httpboot", "dns", "template", "bmc",
                    "discovery"],
                "listdicts": [],
                "lists": [],
                },
            "webhooks": {
                "fields": [],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "architectures": {
                "fields": ["id", "name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            # "audits": {
            #     "fields": [
            #         "id", "user_type", "user_name", "comment", "associated_id",
            #         "associated_type", "remote_address", "associated_name",
            #         "auditable_name", "auditable_type", "action", "locations"],
            #     "dicts": [],
            #     "listdicts": ["locations"],
            #     "lists": [],
            #     },
            "auth_source_externals": {
                "fields": [
                    "id", "name", "locations"],
                "dicts": [],
                "listdicts": ["locations"],
                "lists": [],
                },
            "auth_source_internals": {
                "fields": [
                    "id", "name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "auth_source_ldaps": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "auth_sources": {
                "fields": [
                    "id", "name", "type", "locations"],
                "dicts": [],
                "listdicts": ["locations"],
                "lists": [],
                },
            "bookmarks": {
                "fields": [
                    "id", "name", "owner_id", "owner_type", "public",
                    "controller", "query"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "common_parameters": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "compliance/arf_reports": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "compliance/oval_contents": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "compliance/oval_policies": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "compliance/policies": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "compliance/scap_content_profiles": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "compliance/scap_contents": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "compliance/tailoring_files": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "config_reports": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "domains": {
                "fields": [
                    "id", "name", "fullname", "dns"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            # dictionary usually not needed
            # "fact_values": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "filters": {
                "fields": [
                    "id", "search", "resource_type_label", "unlimited?",
                    "override?", "resource_type", "role", "permissions"],
                    "dicts": ["role"],
                    "listdicts": ["permissions"],
                    "lists": [],
                },
            # "hosts": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            # "host_statuses": {
            #     "fields": [
            #         "id", "name", "ok_total_path", "ok_owned_path",
            #         "warn_total_path", "warn_owned_path",
            #         "error_total_path", "error_owned_path"],
            #     "dicts": [],
            #     "listdicts": [],
            #     "lists": [],
            #     },
            "http_proxies": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "instance_hosts": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "job_invocations": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "job_templates": {
                "fields": [
                    "id", "name", "job_category", "provider_type", "snippet",
                    "description_format"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "mail_notifications": {
                "fields": ["id", "name", "subscription_type"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "media": {
                "fields": ["id", "name", "os_family", "path"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "models": {
                "fields": [
                    "id", "name", "info", "vendor_class", "hardware_model",
                    "hosts_count"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "operatingsystems": {
                "fields": [
                    "id", "name", "major", "minor", "family", "release_name",
                    "password_hash", "title"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "permissions": {
                "fields": [
                    "id", "name", "resource_type"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "permissions/resource_types": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "preupgrade_reports": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "provisioning_templates": {
                "fields": [
                    "id", "name", "snippet", "template_kind_id", "template_kind_name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "ptables": {
                "fields": [
                    "id", "name", "os_family"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "realms": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "remote_execution_features": {
                "fields": [
                    "id", "name", "label", "job_template_name",
                    "host_action_button"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "report_templates": {
                "fields": [
                    "id", "name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "roles": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "template_kinds": {
                "fields": [
                    "id", "name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "usergroups": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "users": {
                "fields": [
                    "id", "login", "firstname", "lastname", "mail",
                    "mail_enabled", "admin", "auth_source_id", "disabled",
                    "auth_source_name", "timezone", "locale", "last_login_on",
                    "description", "ssh_keys", "default_location", "locations",
                    "default_organization", "organizations", "effective_admin"],
                "dicts": ["default_organization", "default_location"],
                "listdicts": ["organizations", "locations"],
                "lists": ["ssh_keys"],
                },
            "discovered_hosts": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "discovery_rules": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "webhooks/events": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "webhook_templates": {
                "fields": [
                    "id", "name"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
        },
    },
    "foreman_tasks": {
        "uri": "/foreman_tasks/api/",
        "objects": {
            "recurring_logics": {
                "fields": [],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            # too many information and already dumped by sos report
            # "tasks": {
            #    "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #    },
            },
    },
    "foreman_virt_who_configure": {
        "uri": "/foreman_virt_who_configure/api/v2/",
        "objects": {
            "configs": {
                "fields": [],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            },
    },
    "katello": {
        "uri": "/katello/api/",
        "objects": {
            "activation_keys": {
                "fields": [
                    "id", "name", "unlimited_hosts", "auto_attach",
                    "content_view", "environment", "release_version",
                    "products", "host_collections"],
                "dicts": ["content_view", "environment"],
                "listdicts": [],
                "lists": [],
            },
            "alternate_content_sources": {
                "fields": [],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "capsules": {
                "fields": [
                    "id", "name", "download_policy",
                    "lifecycle_environments", "supported_pulp_types",
                    "features"],
                "dicts": [],
                "listdicts": ["lifecycle_environments", "features"],
                "lists": ["supported_pulp_types"],
                },
            "content_views": {
                "fields": [
                    "id", "name", "composite", "environments",
                    "activation_keys", "repositories", "related_composite_cvs",
                    "filtered"],
                "dicts": [],
                "listdicts": [
                    "environments", "activation_keys", "repositories",
                    "related_composite_cvs"],
                "lists": [],
                    },
            "environments": {
                "fields": [
                    "id", "name", "content_views", "prior", "successor"],
                "dicts": ["prior", "successor"],
                "listdicts": ["content_views"],
                "lists": [],
                },
            "repositories": {
                "fields": [
                    "id", "name", "content_type", "mirroring_policy",
                    "product", "os_versions", "arch", "kt_environment",
                    "content_view"],
                "dicts": [
                    "os_versions", "kt_environment", "content_view",
                    "product"],
                "listdicts": [],
                "lists": ["os_versions"],
                    },
            "subscriptions": {
                "fields": [
                    "id", "name", "product_name", "start_date", "end_date",
                    "available", "quantity", "consumed", "account_number",
                    "contract_number"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                    },
            "ansible_collections": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "content_credentials": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "content_exports": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "content_imports": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "content_units/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            # 'errors': ['Required param content_type is missing']
            # "content_units": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "content_view_versions": {
                "fields": [
                    "id", "name", "version", "major", "minor",
                    "composite_content_view_ids",
                    "published_in_composite_content_view_ids",
                    "content_view_id", "default", "description",
                    "content_view", "composite_content_views",
                    "composite_content_view_versions",
                    "published_in_composite_content_views",
                    "environments", "repositories", "last_event",
                    "active_history", "ansible_collection_count",
                    "docker_manifest_count", "docker_manifest_list_count",
                    "docker_tag_count", "file_count", "rpm_count",
                    "modulemd_count", "erratum_count", "package_group_count",
                    "srpm_count", "module_stream_count", "package_count",
                    "component_view_count",
                    "ansible_collection_repository_count",
                    "docker_repository_count", "file_repository_count",
                    "yum_repository_count", "errata_counts", "permissions",
                    "filters_applied"],
                "dicts": [],
                "listdicts": ["environments"],
                "lists": [],
                },
            # "debs/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "debs": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "docker_manifest_lists/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "docker_manifest_lists": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "docker_manifests/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "docker_manifests": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "docker_tags/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "docker_tags": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "errata/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            # "errata": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            # "files/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "files": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            "host_collections": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "module_streams/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            # "module_streams": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "organizations": {
                "fields": [
                    "id", "name", "label", "title"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "ostree_refs": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "package_groups/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "package_groups": {
                "fields": [
                    "id", "name", "pulp_id", "uuid", "repository"],
                "dicts": ["repository"],
                "listdicts": [],
                "lists": [],
                },
            #"packages/compare": {
            #    "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #    },
            # "packages": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "products": {
                "fields": [
                    "id", "name", "cp_id", "label", "provider_id",
                    "sync_plan", "sync_summary", "gpg_key_id",
                    "ssl_ca_cert_id", "ssl_client_cert_id",
                    "ssl_client_key_id", "sync_state", "last_sync",
                    "last_sync_words", "repository_count"],
                "dicts": [],
                "listdicts": [],
                "lists": [],
                },
            "python_packages": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
            # "repositories/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "repository_sets": {
                "fields": [
                    "id", "name", "enabled", "product", "content",
                    "repositories", "vendor", "label", "type", "gpgUrl",
                    "contentUrl", "archRestricted", "osRestricted", "override",
                    "overrides", "enabled_content_override", "redhat"],
                "dicts": ["repositories"],
                "listdicts": [],
                "lists": [],
                },
            # "srpms/compare": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            # "srpms": {
            #     "fields": [], "dicts": [], "listdicts": [], "lists": [],
            #     },
            "sync_plans": {
                "fields": [], "dicts": [], "listdicts": [], "lists": [],
                },
        },
    },
}

# NOTE: currently HTTPBasicAuth is used
# TODO(faster): worth to use a diferent auth method to speed up the requests?
# TODO(sos report plugin): Can Satellite cert/token used instead of user/pass?
# BUG(org_id filter): Some objects seem to ignore the organization_id filter
#                     hence all entries are returned.
