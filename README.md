## foremap

Shows the big picture configuration map for [theforeman](https://theforeman.org/)

## Goals

1.  Json output to be human readable or also easily displayed on a browser using some JS and CSS.
2.  Foreman configuration `readers` must implement a default query and also specific one if needed for a specific theforeman DB schema version.
3.  KISS to add new configuration `readers`:
    1.  First goal is to add Organizations, Activation Keys, Life Cicles, Content Views…
    2.  More configuration readers should come: Smart Proxies, Host Groups, Compute resources, Compute Profiles…
4.  Implement warning checks? E.g: Not promoted Content Views, Life Cycle not mapped to Smart Proxy…