# Ansible

Запалняем инвертери
`
[myhosts]
master ansible_ssh_port=22002 ansible_ssh_host=45.9.26.172
worker1 ansible_ssh_port=22003 ansible_ssh_host=45.9.26.172
worker2 ansible_ssh_port=22004 ansible_ssh_host=45.9.26.172
`

Запускаем плейбук 
`ansible-playbook -u root -i inventory.ini playbook.yaml`

