# .bashrc
#export PS1="\[\e[31m\][\u@\h \W]\$\[\e[0m\]"
export PS1="\[\033[1;33m\]\u@\h \W\$\[\e[0m\]"
#export PS1="\[\033[1;32m\]\u:\[\033[1;34m\] \W \$\[\033[0m\]"
# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

ps1='export PS1="\[\033[1;33m\]\u@\h \W\$\[\e[0m\]"'
alias ps1='echo $ps1'
alias s="source ~/.bashrc"
alias vb="vi ~/.bashrc"
alias cb="code ~/.bashrc"
alias tv='echo "/cs-shared/testbed_locks/testbed_kubernetes_1_ha.py"'
alias reimage="ansible-playbook -i /home/nuthanc/ansible_for_auto/inventory /home/nuthanc/ansible_for_auto/playbooks/reimage.yml"
alias reimagep="ansible-playbook -i /home/nuthanc/ansible_for_auto/inventory /home/nuthanc/ansible_for_auto/playbooks/reimage_prompt.yml"
alias hosts="code /home/nuthanc/ansible_for_auto/inventory/hosts || vi /home/nuthanc/ansible_for_auto/inventory/hosts"
alias playbooks="cd /home/nuthanc/ansible_for_auto/playbooks"
alias rk="bash /home/nuthanc/ansible_for_auto/remove_key.sh"
alias contrail-status="ansible-playbook -i /home/nuthanc/ansible_for_auto/inventory /home/nuthanc/ansible_for_auto/playbooks/contrail_status.yml"
alias start="source /home/nuthanc/only_contrail/start.sh"
alias exports="code /home/nuthanc/only_contrail/exports.sh"
alias hub="python /home/nuthanc/build_numbers/max_hub.py"
alias loc="python /home/nuthanc/build_numbers/max_local.py"
alias down="ansible-playbook -i /home/nuthanc/ansible_for_auto/inventory /homes/nuthanc/ansible_for_auto/playbooks/downgrade_ansible.yml"
alias scrape="vi /homes/nuthanc/scrape/failure_tc.py"
alias cscrape="code /homes/nuthanc/scrape/failure_tc.py"
alias 19="cd /homes/nuthanc/c19_setup"
alias sanity="ansible-playbook -i /home/nuthanc/ansible_for_auto/inventory /home/nuthanc/ansible_for_auto/playbooks/sanity.yml"

a(){
	ansible-playbook -i /home/nuthanc/ansible_for_auto/inventory /home/nuthanc/ansible_for_auto/playbooks/$1
}

