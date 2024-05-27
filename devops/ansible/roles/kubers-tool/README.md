# Kubernetes-tools Role
Install kuber's tools

## Variables

- `version` - version of install crio;
defualt: `v1.29`

# Example to use
`
  tasks:
    - name: Install crio
      include_role:
        name: crio
`
