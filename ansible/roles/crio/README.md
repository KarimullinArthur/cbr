# Crio Role
Install cri-o 

## Variables

- `project_path` - version of install crio;
defualt: `prerelease:/main`

# Example to use
`
  tasks:
    - name: Install crio
      include_role:
        name: crio
`
