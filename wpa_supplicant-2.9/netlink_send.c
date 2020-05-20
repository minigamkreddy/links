//https://people.redhat.com/nhorman/papers/netlink.pdf
//https://www.infradead.org/~tgr/libnl/doc/core.html#core_send_recv
//https://gist.github.com/arunk-s/c897bb9d75a6c98733d6
//http://epic-alfa.kavli.tudelft.nl/share/doc/libnl-devel-1.1.4/html/nl_8c_source.html#l00373

//http://www.linuxfromscratch.org/blfs/view/svn/basicnet/wpa_supplicant.html

#include <sys/types.h>
#include <sys/socket.h>
#include <linux/netlink.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define NETLINK_TEST  17
#define MAX_PAYLOAD 1024  /* maximum payload size*/

struct sockaddr_nl src_addr, dest_addr;
struct msghdr msg;
struct nlmsghdr *nlh = NULL;
struct iovec iov;
int sock_fd;

void main() {
 sock_fd = socket(PF_NETLINK, SOCK_RAW,NETLINK_TEST);

 memset(&src_addr, 0, sizeof(src_addr));
 src_addr.nl_family = AF_NETLINK;
 src_addr.nl_pid = getpid();  /* self pid */
 src_addr.nl_groups = 0;  /* not in mcast groups */
 bind(sock_fd, (struct sockaddr*)&src_addr,
      sizeof(src_addr));

 memset(&dest_addr, 0, sizeof(dest_addr));
 dest_addr.nl_family = AF_NETLINK;
 dest_addr.nl_pid = 0;   /* For Linux Kernel */
 dest_addr.nl_groups = 0; /* unicast */

 nlh=(struct nlmsghdr *)malloc(
		         NLMSG_SPACE(MAX_PAYLOAD));
 /* Fill the netlink message header */
 nlh->nlmsg_len = NLMSG_SPACE(MAX_PAYLOAD);
 nlh->nlmsg_pid = getpid();  /* self pid */
 nlh->nlmsg_flags = 0;
 /* Fill in the netlink message payload */
 strcpy(NLMSG_DATA(nlh), "Hello you!");

 iov.iov_base = (void *)nlh;
 iov.iov_len = nlh->nlmsg_len;
 
msg.msg_name = "manoj";
msg.msg_namelen = sizeof(msg.msg_name);
// msg.msg_name = (void *)&dest_addr;
// msg.msg_namelen = sizeof(dest_addr);
 msg.msg_iov = &iov;
 msg.msg_iovlen = 1;

 send(sock_fd, &msg, 0);

 /* Read message from kernel */
 memset(nlh, 0, NLMSG_SPACE(MAX_PAYLOAD));
 recv(sock_fd, &msg, 0);
 printf(" Received message payload: %s %s\n",
	NLMSG_DATA(nlh),msg.msg_name);

 /* Close Netlink Socket */
 close(sock_fd);
}
