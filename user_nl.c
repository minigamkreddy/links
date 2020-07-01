#include <linux/netlink.h>
#include <linux/msg.h>
#include <sunrpc/addr.h>
#include <linux/socket.h>
#include <errno.h>
#include <linux/genl/genl.h>
#include <linux/genl/family.h>
#include <linux/genl/ctrl.h>
#include "attr_cmd.h"

#define MSG_SETCFG      0x11


int main(int argc, char *argv[])
{
	struct nl_msg *msg = NULL;
	int err = -ENOMEM;
	int flags = 0;
	struct genl_family *family;
	int gr_id;
	//struct nl_handle *sock;
	

	/* creating netlink Socket */
	//struct nl_sock *sk = nl_handle_alloc();
	struct nl_sock *sk = (void*)nl_socket_alloc();
	if(sk == NULL)
	{
		printf("Failed to Create Netlink socket\n");
		return -1;
	}

	//if(genl_connect(sk)){
	if(nl_connect((void*)sk, NETLINK_GENERIC))
	{
		printf("genl_connect failed\n");
		return -1;
	}

	/* find the family ID of test */
	int familyID = genl_ctrl_resolve((void*)sk, "test");

	if (familyID < 0) {
		printf("negative familyID\n");
		return -1;
	} else {
		printf("test familyID returned by genl_ctrl_resolve :%d\n",familyID);
	}

	msg = nlmsg_alloc();
	if (!msg) {
		return 0;
	}

	//if (nlmsg_put(msg, 0, 0, familyID , 0, flags, MY_CMD_ECHO, 0) == NULL) {
	if (nlmsg_put(msg, 0, NL_AUTO_SEQ, 11 , sizeof(int), NLM_F_CREATE) == NULL) {
		printf("Error return genlMsg_put\n");
	} else {
		printf("Success genlmsg_put\n");
	}

	/* setup the message */
	if (nla_put_u8(msg, MY_ATTR_ECHO, 100)) {
		printf("\nnla_put_failure\n");
		goto out;
	}

	//err = nl_send_auto_complete((void *)sk, msg);
	err = nl_send_auto((void *)sk, msg);

	if (err < 0)
		goto out;
	else
		printf("Sent successfully\n");

	getchar();
	getchar();
	getchar();

#if 0
	struct genlmsghdr *gnlh = nlmsg_data(nlmsg_hdr(msg));
	struct nlattr *tb[__MY_ATTR_MAX + 1];
	int kernval = 0;

	nla_parse(tb, __MY_ATTR_MAX, genlmsg_attrdata(gnlh, 0),
				genlmsg_attrlen(gnlh, 0), NULL);

	if (gnlh->cmd == MY_CMD_ECHO) {
		if (tb[MY_ATTR_ECHO]) {
			kernval = nla_get_u8(tb[MY_ATTR_ECHO]);
			printf("kernel retval : %d\n", kernval);
		}
	}
#endif

out:
	nlmsg_free(msg);

	return err;
}
