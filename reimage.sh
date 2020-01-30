if [ "$#" -eq 0 ]
then
	server-manager reimage --no_confirm --server_id nodeg12 centos-7.7
	server-manager reimage --no_confirm --server_id nodeg31 centos-7.7
	server-manager reimage --no_confirm --server_id nodec58 centos-7.7
	server-manager reimage --no_confirm --server_id nodec60 centos-7.7
	server-manager reimage --no_confirm --server_id nodec61 centos-7.7
else
	if [ "$1" == "status" ]
    then
		server-manager status server --server_id nodeg12
		server-manager status server --server nodeg31
		server-manager status server --server nodec58
		server-manager status server --server nodec60
		server-manager status server --server nodec61
		server-manager status server --server nodea4
	else
		server-manager reimage --no_confirm --server_id $1 centos-7.7
	fi
fi
